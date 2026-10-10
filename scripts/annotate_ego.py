"""Annotate RGB images with WildDet3D using local checkpoints.

Run ``python scripts/annotate_ego.py --help`` for arguments. Model imports are
delayed so help and validated prediction reuse do not require a visible PPU.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
from importlib.metadata import PackageNotFoundError, version
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import sys
import tempfile
import time
import traceback


REPO_ROOT = Path(__file__).resolve().parents[1]
WEIGHT_ROOT = Path("/mnt/workspace/TEMP-FILE-STATION")
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tif", ".tiff"}
PREDICTION_FIELDS = ("boxes2d_xyxy", "boxes3d", "scores", "scores_2d", "scores_3d", "class_ids")
BOX3D_FIELDS = ["cx", "cy", "cz", "W", "L", "H", "qw", "qx", "qy", "qz"]
SCHEMA_VERSION = 1


def probability(text):
    value = float(text)
    if not math.isfinite(value) or not 0 <= value <= 1:
        raise argparse.ArgumentTypeError("分数阈值必须在 0 到 1 之间")
    return value


def positive_int(text):
    value = int(text)
    if value <= 0:
        raise argparse.ArgumentTypeError("数量必须为正整数")
    return value


def cuda_device(text):
    if not re.fullmatch(r"cuda(?::\d+)?", text):
        raise argparse.ArgumentTypeError("新推理使用 cuda 或 cuda:N；本模型不支持 CPU 前向")
    return text


def parser():
    result = argparse.ArgumentParser(description="RGB 图片 → WildDet3D 预标注 JSON 与 3D 框预览")
    result.add_argument("--input", required=True, type=Path, help="单张图片或图片目录，目录递归扫描")
    result.add_argument("--output", required=True, type=Path, help="结果根目录，自动创建")
    result.add_argument("--classes", nargs="+", default=["cardboard box", "basket", "shelf"], help="类别提示，含空格的类别加引号")
    result.add_argument("--checkpoint", type=Path, default=WEIGHT_ROOT / "wilddet3d_alldata_all_prompt_v1.0.pt", help="WildDet3D 本地权重")
    result.add_argument("--lingbot-checkpoint", type=Path, default=WEIGHT_ROOT / "model.pt", help="LingBot 本地 model.pt")
    result.add_argument("--score-2d", type=probability, default=0.5, help="最终 2D 分数阈值，默认 0.5")
    result.add_argument("--score-3d", type=probability, default=0.5, help="最终 3D 分数阈值，默认 0.5")
    result.add_argument("--model-score-threshold", type=probability, default=0.3, help="模型综合分数初筛阈值，默认 0.3")
    result.add_argument("--intrinsics", type=Path, help="统一的 3×3 内参 .npy 文件，优先于 manifest")
    result.add_argument("--manifest", type=Path, help="抽帧 extraction_manifest.json，提供每张图片的内参")
    result.add_argument("--max-images", type=positive_int, help="最多处理几张；不填写则处理全部")
    result.add_argument("--device", type=cuda_device, default="cuda", help="cuda 或 cuda:N，默认 cuda")
    result.add_argument("--no-vis", action="store_true", help="只保存 JSON，清除所选图片已有的预览图")
    result.add_argument("--resume", action="store_true", help="校验并复用已有预测，继续未完成的图片")
    return result


def read_json(path):
    def reject_constant(value):
        raise ValueError(f"JSON 含有非有限数值：{value}")

    with path.open(encoding="utf-8") as stream:
        return json.load(stream, parse_constant=reject_constant)


def atomic_json(path, value, *, replace=False):
    # Serialize before touching the destination; a failed dump leaves no output.
    content = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, prefix=".annotate-", suffix=".tmp", delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        if replace:
            os.replace(temporary, path)
        else:
            # Unlike replace(), link() refuses to overwrite an existing prediction.
            os.link(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def signature(value):
    content = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(content.encode()).hexdigest()


def source_signature():
    digest = hashlib.sha256()
    paths = [Path(__file__).resolve()]
    for directory in ("wilddet3d", "third_party/sam3/sam3", "third_party/lingbot_depth/mdm"):
        paths.extend(sorted((REPO_ROOT / directory).rglob("*.py")))
    paths.append(REPO_ROOT / "third_party/sam3/sam3/assets/bpe_simple_vocab_16e6.txt.gz")
    for path in paths:
        digest.update(path.relative_to(REPO_ROOT).as_posix().encode())
        digest.update(bytes.fromhex(sha256_file(path)))
    return digest.hexdigest()


def collect_images(input_path, output_path, limit):
    if input_path.is_file():
        if input_path.suffix.lower() not in IMAGE_EXTENSIONS:
            raise ValueError(f"输入不是支持的图片：{input_path}；视频请先抽帧")
        return input_path.parent, [input_path]
    if not input_path.is_dir():
        raise ValueError(f"输入路径不存在：{input_path}")
    if input_path == output_path or input_path.is_relative_to(output_path):
        raise ValueError("输出目录不能等于输入目录或包含输入目录")
    paths = sorted(
        (path for path in input_path.rglob("*")
         if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
         and not path.resolve().is_relative_to(output_path)),
        key=lambda path: path.relative_to(input_path).as_posix(),
    )
    if not paths:
        raise ValueError(f"输入目录没有支持的图片：{input_path}")
    return input_path, paths[:limit] if limit is not None else paths


def load_manifest(path):
    if path is None:
        return {}
    content = read_json(path)
    frames = {}
    if not isinstance(content, dict) or not isinstance(content.get("videos"), list):
        raise ValueError("manifest 需要包含 videos 列表及各视频的 frames 列表")
    for video in content["videos"]:
        if not isinstance(video, dict) or not isinstance(video.get("frames"), list):
            raise ValueError("manifest 中的视频缺少 frames 列表")
        for frame in video["frames"]:
            if not isinstance(frame, dict) or not isinstance(frame.get("image"), str):
                raise ValueError("manifest 中的帧缺少 image 路径")
            key = PurePosixPath(frame["image"])
            if key.is_absolute() or ".." in key.parts or not key.parts:
                raise ValueError(f"manifest image 必须为相对图片路径：{key}")
            key = key.as_posix()
            if key in frames:
                raise ValueError(f"manifest 中图片路径重复：{key}")
            frames[key] = frame
    return frames


def validate_intrinsics(matrix):
    import numpy as np

    value = np.asarray(matrix, dtype=np.float32)
    if (value.shape != (3, 3) or not np.isfinite(value).all()
            or value[0, 0] <= 0 or value[1, 1] <= 0
            or not np.allclose(value[2], [0, 0, 1])):
        raise ValueError("内参必须为有限的 3×3 矩阵，fx/fy 为正，最后一行为 [0, 0, 1]")
    return value


def image_intrinsics(args, image_path, relative, image_hw, frames):
    import numpy as np

    selected = args.intrinsics
    source = "provided" if selected is not None else "default_placeholder"
    if selected is None and args.manifest is not None:
        keys = {relative.as_posix()}
        for root in (args.manifest.parent / "images", args.manifest.parent):
            if image_path.is_relative_to(root):
                keys.add(image_path.relative_to(root).as_posix())
        matching = [key for key in keys if key in frames]
        if len(matching) > 1:
            raise ValueError(f"manifest 匹配不唯一：{relative}")
        frame = frames[matching[0]] if matching else {}
        if frame.get("image_hw") is not None and frame["image_hw"] != list(image_hw):
            raise ValueError(f"图片尺寸与 manifest 不一致：{relative}")
        if frame.get("intrinsics") is not None:
            selected = Path(frame["intrinsics"])
            if not selected.is_absolute():
                selected = args.manifest.parent / selected
            source = "extraction_manifest"
    if selected is not None:
        selected = selected.resolve()
        return validate_intrinsics(np.load(selected, allow_pickle=False)), source, str(selected)
    height, width = image_hw
    focal = max(height, width)
    return validate_intrinsics([[focal, 0, width / 2], [0, focal, height / 2], [0, 0, 1]]), source, None


def validate_prediction(record):
    import numpy as np

    if not isinstance(record, dict):
        raise ValueError("预测 JSON 必须为对象")
    count = len(record["boxes3d"])
    for name in PREDICTION_FIELDS:
        values = record[name]
        if not isinstance(values, list) or len(values) != count:
            raise ValueError(f"预测字段数量不一致：{name}")
        array = np.asarray(values, dtype=np.float64)
        expected = (count, 4 if name == "boxes2d_xyxy" else 10) if name in ("boxes2d_xyxy", "boxes3d") else (count,)
        if count == 0 and name in ("boxes2d_xyxy", "boxes3d"):
            array = array.reshape(expected)
        if array.shape != expected or not np.isfinite(array).all():
            raise ValueError(f"预测字段形状错误或含 NaN/Inf：{name}")
    if count and not (np.asarray(record["boxes3d"])[:, 3:6] > 0).all():
        raise ValueError("3D 框尺寸必须为正")
    for value in record["class_ids"]:
        if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value < len(record["class_names"]):
            raise ValueError(f"预测类别编号无效：{value}")
    validate_intrinsics(record["intrinsics_original"])


def filtered_prediction(record, args, target):
    keep = [index for index, (s2d, s3d) in enumerate(zip(record["scores_2d"], record["scores_3d"]))
            if s2d >= args.score_2d and s3d >= args.score_3d]
    result = dict(record)
    for name in PREDICTION_FIELDS:
        result[name] = [record[name][index] for index in keep]
    result["score_filter"] = {"score_2d_min": args.score_2d, "score_3d_min": args.score_3d,
                              "condition": "scores_2d >= score_2d_min AND scores_3d >= score_3d_min"}
    result["source_prediction"] = str(target)
    return result


class InferenceBackend:
    def __init__(self, args):
        os.environ["SAM3_COMPILE"] = "0"
        os.environ["XFORMERS_DISABLED"] = "1"
        os.environ["HF_HUB_OFFLINE"] = "1"
        sys.path.insert(0, str(REPO_ROOT))
        import torch

        if not torch.cuda.is_available():
            raise RuntimeError("PPU/CUDA 不可用；请先在实际 DSW 终端完成 README 的设备检查")
        from wilddet3d import build_model, preprocess

        self.torch = torch
        # set_device() requires an explicit index even though .to("cuda") does not.
        self.device = torch.device(args.device if ":" in args.device else f"cuda:{torch.cuda.current_device()}")
        torch.cuda.set_device(self.device)
        self.preprocess = preprocess
        self.classes = args.classes
        print(f"加载模型到 {args.device}：{torch.cuda.get_device_name(self.device)}", flush=True)
        self.model = build_model(
            checkpoint=str(args.checkpoint),
            lingbot_pretrained_model=str(args.lingbot_checkpoint),
            skip_pretrained=True,
            canonical_rotation=True,
            score_threshold=args.model_score_threshold,
            score_3d_threshold=0.1,
            device=str(self.device),
        )

    def predict(self, image, intrinsics):
        torch = self.torch
        data = self.preprocess(image, intrinsics)
        torch.cuda.synchronize(self.device)
        torch.cuda.reset_peak_memory_stats(self.device)
        started = time.perf_counter()
        with torch.inference_mode():
            result = self.model(
                images=data["images"].to(self.device),
                intrinsics=data["intrinsics"].to(self.device)[None],
                input_hw=[data["input_hw"]],
                original_hw=[data["original_hw"]],
                padding=[data["padding"]],
                input_texts=self.classes,
            )
        torch.cuda.synchronize(self.device)
        metrics = {"forward_seconds": time.perf_counter() - started,
                   "peak_tensor_memory_gib": torch.cuda.max_memory_allocated(self.device) / (1024 ** 3)}
        # The predictor returns six lists plus the optional depth map.
        prediction = {name: values[0].detach().cpu().tolist()
                      for name, values in zip(PREDICTION_FIELDS, result[:6])}
        return prediction, metrics


def render_preview(image, record, destination):
    sys.path.insert(0, str(REPO_ROOT))
    import numpy as np
    from wilddet3d.vis.visualize import draw_3d_boxes

    rendered = draw_3d_boxes(
        image=image,
        boxes3d=np.asarray(record["boxes3d"], dtype=np.float32).reshape(-1, 10),
        intrinsics=np.asarray(record["intrinsics_original"], dtype=np.float32),
        scores_2d=np.asarray(record["scores_2d"], dtype=np.float32),
        scores_3d=np.asarray(record["scores_3d"], dtype=np.float32),
        class_ids=np.asarray(record["class_ids"], dtype=np.int64),
        class_names=record["class_names"],
        draw_predicted_2d_boxes=False,
        score_2d_threshold=0.0,
        score_3d_threshold=0.0,
        line_width=3,
        font_size=20,
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(dir=destination.parent, prefix=".annotate-", suffix=".tmp")
    os.close(handle)
    try:
        rendered.save(temporary, format="PNG")
        os.replace(temporary, destination)
    finally:
        Path(temporary).unlink(missing_ok=True)


def prepare(args):
    for name in ("input", "output", "checkpoint", "lingbot_checkpoint", "intrinsics", "manifest"):
        value = getattr(args, name)
        if value is not None:
            setattr(args, name, value.expanduser().resolve())
    args.classes = [value.strip() for value in args.classes]
    if not args.classes or any(not value for value in args.classes) or len(set(args.classes)) != len(args.classes):
        raise ValueError("类别列表不能为空，也不能包含空白或重复类别")
    for name in ("checkpoint", "lingbot_checkpoint", "intrinsics", "manifest"):
        value = getattr(args, name)
        if value is not None and (not value.is_file() or value.stat().st_size == 0):
            raise ValueError(f"文件不存在或为空：--{name.replace('_', '-')} {value}")
    root, paths = collect_images(args.input, args.output, args.max_images)
    frames = load_manifest(args.manifest)
    if args.output.exists() and not args.output.is_dir():
        raise ValueError(f"输出路径不是目录：{args.output}")
    config_path = args.output / "run_config.json"
    previous = read_json(config_path) if config_path.exists() else None
    if previous is not None and not args.resume:
        raise ValueError("输出已有运行记录；使用 --resume 校验复用，或指定新的 --output")
    if previous is None and args.output.exists() and any(
        path.name != ".annotate_ego.lock" for path in args.output.iterdir()
    ):
        raise ValueError("输出目录非空且没有本工具的运行记录，请指定新的 --output")
    print("校验本地权重与代码 SHA256…", flush=True)
    packages = {}
    for name in ("torch", "torchvision", "numpy", "Pillow", "vis4d", "utils3d", "timm"):
        try:
            packages[name] = version(name)
        except PackageNotFoundError:
            packages[name] = None
    prediction_config = {
        "schema_version": SCHEMA_VERSION,
        "input": str(args.input),
        "classes": args.classes,
        "checkpoint": {"path": str(args.checkpoint), "sha256": sha256_file(args.checkpoint)},
        "lingbot_checkpoint": {"path": str(args.lingbot_checkpoint), "sha256": sha256_file(args.lingbot_checkpoint)},
        "model_score_threshold": args.model_score_threshold,
        "model_score_3d_threshold": 0.1,
        "device": args.device,
        "precision": "fp32", "compile": False, "xformers": False,
        "canonical_rotation": True,
        "source_sha256": source_signature(),
        "package_versions": packages,
    }
    if previous is not None and previous.get("prediction_config") != prediction_config:
        raise ValueError("已有结果的输入、权重、类别、模型参数、代码或依赖版本不同，请指定新的 --output")
    return root, paths, frames, prediction_config, previous


@contextmanager
def output_lock(output):
    output.mkdir(parents=True, exist_ok=True)
    with (output / ".annotate_ego.lock").open("a") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RuntimeError("同一输出目录已有预标注任务在运行") from error
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def run(args, *, backend_factory=None, preview_renderer=None):
    import numpy as np
    from PIL import Image

    os.environ["SAM3_COMPILE"] = "0"
    os.environ["XFORMERS_DISABLED"] = "1"
    os.environ["HF_HUB_OFFLINE"] = "1"
    root, paths, frames, prediction_config, previous = prepare(args)
    backend_factory = backend_factory or InferenceBackend
    preview_renderer = preview_renderer or render_preview
    # Preflight cached images before overwriting any derived output or run record.
    items = []
    for path in paths:
        relative = path.relative_to(root)
        with Image.open(path) as image:
            image.load()
            image_hw = (image.height, image.width)
        intrinsics, intrinsics_source, intrinsics_path = image_intrinsics(args, path, relative, image_hw, frames)
        image_sha = sha256_file(path)
        prediction_signature = signature({"config": prediction_config, "image_sha256": image_sha,
                                          "image_hw": image_hw, "intrinsics": intrinsics.tolist()})
        target = args.output / "predictions" / relative.parent / (relative.name + ".json")
        if target.exists():
            if not args.resume:
                raise ValueError(f"预测文件已存在：{target}")
            record = read_json(target)
            if (record.get("prediction_signature") != prediction_signature
                    or record.get("image") != relative.as_posix()
                    or record.get("image_hw") != list(image_hw)
                    or record.get("class_names") != args.classes
                    or record.get("intrinsics_original") != intrinsics.tolist()):
                raise ValueError(f"已有预测与当前图片、内参或配置不匹配：{relative}；请使用新输出目录")
            validate_prediction(record)
        items.append((path, relative, image_hw, intrinsics, intrinsics_source, intrinsics_path, image_sha, prediction_signature, target))

    with output_lock(args.output):
        # A second process may have completed between prepare() and lock().
        current = args.output / "run_config.json"
        if (read_json(current) if current.exists() else None) != previous:
            raise RuntimeError("输出运行记录在校验期间发生变化，请重新执行")
        atomic_json(current, {
            "prediction_config": prediction_config,
            "parameters": {key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()},
            "started_at": datetime.now(timezone.utc).isoformat(),
        }, replace=previous is not None)
        summary = {"status": "running", "selected": len(items), "succeeded": 0, "inferred": 0,
                   "reused": 0, "failed": 0, "not_processed": len(items), "images": []}
        started = time.perf_counter()
        backend = None
        active_image = None
        try:
            for index, item in enumerate(items, 1):
                path, relative, image_hw, intrinsics, source, intrinsic_path, image_sha, prediction_signature, target = item
                active_image = relative.as_posix()
                # Do not pair predictions with pixels changed after preflight.
                if sha256_file(path) != image_sha:
                    raise ValueError(f"图片在校验后发生变化：{relative}")
                with Image.open(path) as stream:
                    image = np.asarray(stream.convert("RGB"), dtype=np.uint8)
                reused = target.exists()
                if reused:
                    record = read_json(target)
                    if record.get("prediction_signature") != prediction_signature:
                        raise ValueError(f"预测在校验后发生变化：{relative}")
                    validate_prediction(record)
                else:
                    if backend is None:
                        backend = backend_factory(args)
                    prediction, metrics = backend.predict(image, intrinsics)
                    record = {
                        "schema_version": SCHEMA_VERSION,
                        "prediction_signature": prediction_signature,
                        "image_sha256": image_sha,
                        "image": relative.as_posix(), "image_hw": list(image_hw),
                        "class_names": args.classes,
                        "coordinate_system": "camera_opencv", "length_unit": "meter",
                        "box3d_fields": BOX3D_FIELDS,
                        "intrinsics_source": source, "intrinsics_path": intrinsic_path,
                        "intrinsics_original": intrinsics.tolist(),
                        "metrics": metrics,
                        **prediction,
                    }
                    validate_prediction(record)
                    atomic_json(target, record)
                filtered = filtered_prediction(record, args, target)
                filtered_target = args.output / "filtered" / relative.parent / (relative.name + ".json")
                atomic_json(filtered_target, filtered, replace=True)
                preview_target = args.output / "previews" / relative.parent / (relative.name + ".png")
                if args.no_vis:
                    # Old previews could show targets rejected by the new thresholds.
                    preview_target.unlink(missing_ok=True)
                else:
                    preview_renderer(image, filtered, preview_target)
                metrics = record.get("metrics", {})
                entry = {"image": active_image, "action": "reused" if reused else "inferred",
                         "predictions": len(record["boxes3d"]), "retained": len(filtered["boxes3d"]),
                         "metrics": metrics, "metrics_reused": reused}
                summary["images"].append(entry)
                summary["succeeded"] += 1
                summary["reused" if reused else "inferred"] += 1
                summary["not_processed"] -= 1
                timing = "复用预测" if reused else f"前向 {metrics['forward_seconds']:.3f}s，峰值张量显存 {metrics['peak_tensor_memory_gib']:.3f} GiB"
                print(f"[{index}/{len(items)}] {relative}：目标 {entry['predictions']}，保留 {entry['retained']}；{timing}", flush=True)
            summary["status"] = "complete"
        except BaseException as error:
            summary["status"] = "interrupted" if isinstance(error, KeyboardInterrupt) else "failed"
            summary["failed"] = 1
            summary["not_processed"] = max(0, summary["not_processed"] - 1)
            summary["images"].append({"image": active_image, "action": "failed",
                                      "error": str(error) or type(error).__name__,
                                      "traceback": traceback.format_exc()})
            raise
        finally:
            summary["elapsed_seconds"] = time.perf_counter() - started
            atomic_json(args.output / "summary.json", summary, replace=True)
    print(f"完成：成功 {summary['succeeded']}，新推理 {summary['inferred']}，复用 {summary['reused']}；输出 {args.output}")
    return summary


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        run(args)
    except KeyboardInterrupt:
        print("任务已中断；已有完整预测可通过 --resume 继续。", file=sys.stderr)
        return 130
    except Exception as error:
        print(f"预标注失败：{error}", file=sys.stderr)
        if not isinstance(error, (ValueError, FileNotFoundError, FileExistsError)):
            traceback.print_exc()
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
