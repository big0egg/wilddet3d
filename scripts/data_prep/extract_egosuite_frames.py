#!/usr/bin/env python3
"""Copy EgoSuite EgoRaw videos from an OSS mount, then sample local RGB frames.

Defaults: two different tasks, head_left_camera, one frame per second, at most
ten frames per video. Set --interval-seconds 0 --max-frames 0 for every frame.
Depth sensor metadata and actual depth payload files are reported separately.
Only RGB frames are decoded; depth candidates need their own format, units and
alignment verified before use as metric depth. Existing output is not cleared.
"""

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import shutil

import cv2
import numpy as np


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".part")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def copy_local(source, destination):
    """Always finish the local copy before a decoder can open it."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(destination.name + ".part")
    shutil.copyfile(source, temporary)
    if temporary.stat().st_size != source.stat().st_size:
        raise RuntimeError(f"复制后的文件大小不一致：{source}")
    temporary.replace(destination)
    return destination


def select_videos(raw_root, camera, count):
    # Visit tasks lazily; do not recursively scan the whole OSS dataset.
    selected = []
    for task in sorted(p for p in raw_root.iterdir() if p.is_dir()):
        for episode in sorted(p for p in task.iterdir() if p.is_dir()):
            video = episode / camera / f"{camera}_undistorted.mp4"
            if video.is_file():
                selected.append(video)
                break  # Pick distinct tasks for the initial sample.
        if len(selected) == count:
            return selected
    raise RuntimeError(f"只找到 {len(selected)} 段 {camera} 视频，需要 {count} 段")


def extract_video(source, args):
    episode = source.parent.parent
    task = episode.parent.name
    slug = re.sub(r"[^A-Za-z0-9_-]+", "_", task).strip("_") or "task"
    sample_id = f"{slug}__{episode.name}__{args.camera}"
    episode_files = sorted(p for p in episode.rglob("*") if p.is_file())
    depth_candidates = [
        p for p in episode_files
        if any("depth" in part.lower() or "disparity" in part.lower()
               for part in p.relative_to(episode).parts)
        and p.suffix.lower() not in {".json", ".md", ".txt", ".csv"}
    ]
    local_dir = args.local_video_dir / sample_id
    print(f"复制到本地：{task} / {source.name}", flush=True)
    local_video = copy_local(source, local_dir / source.name)
    copied = [local_video]
    # Preserve metadata and potential depth payloads without decoding them.
    for item in episode_files:
        if item.suffix.lower() == ".json" or item in depth_candidates:
            copied.append(copy_local(item, local_dir / item.relative_to(episode)))

    metadata_path = local_dir / "metadata.json"
    metadata = json.loads(metadata_path.read_text()) if metadata_path.is_file() else {}
    devices = metadata.get("capture_devices", {}).get("devices", [])
    depth_devices = [d for d in devices if d.get("modality") == "depth"]
    camera_devices = [d for d in devices if d.get("device_type") == args.camera]
    params_path = local_dir / args.camera / f"{args.camera}_params.json"
    params = json.loads(params_path.read_text()) if params_path.is_file() else {}
    intrinsics = params.get("undistorted_intrinsics")
    intrinsics_path = None
    if intrinsics and all(k in intrinsics for k in ("fx", "fy", "cx", "cy")):
        matrix = np.array([
            [intrinsics["fx"], 0, intrinsics["cx"]],
            [0, intrinsics["fy"], intrinsics["cy"]],
            [0, 0, 1],
        ], dtype=np.float32)
        if not np.isfinite(matrix).all() or min(matrix[0, 0], matrix[1, 1]) <= 0:
            raise ValueError(f"无效的去畸变内参：{params_path}")
        intrinsics_path = args.output_root / "calibration" / sample_id / "intrinsics.npy"
        intrinsics_path.parent.mkdir(parents=True, exist_ok=True)
        np.save(intrinsics_path, matrix)

    cap = cv2.VideoCapture(str(local_video))
    if not cap.isOpened():
        cap.release()
        raise RuntimeError(f"无法打开本地视频：{local_video}")
    records = []
    try:
        fps = float(cap.get(cv2.CAP_PROP_FPS))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if not math.isfinite(fps) or fps <= 0:
            raise RuntimeError(f"无法读取有效帧率：{local_video}")
        output_dir = args.output_root / "images" / sample_id
        output_dir.mkdir(parents=True, exist_ok=True)
        target_index = int(round(args.start_seconds * fps))
        index = 0
        while cap.grab():
            if index < target_index:
                index += 1
                continue
            ok, frame = cap.retrieve()
            if not ok or frame is None:
                raise RuntimeError(f"视频第 {index} 帧解码失败：{local_video}")
            height, width = frame.shape[:2]
            if camera_devices:
                resolution = camera_devices[0].get("resolution", {})
                if resolution and (height, width) != (resolution.get("height"), resolution.get("width")):
                    raise RuntimeError("视频分辨率与相机元数据不一致，需先核对内参")
            image = output_dir / f"frame_{index:06d}.jpg"
            temporary = image.with_name(image.stem + ".part.jpg")
            if not cv2.imwrite(str(temporary), frame, [cv2.IMWRITE_JPEG_QUALITY, 95]):
                raise RuntimeError(f"图片保存失败：{image}")
            temporary.replace(image)
            records.append({
                "image": image.relative_to(args.output_root / "images").as_posix(),
                "source_video": str(source),
                "local_video": str(local_video),
                "frame_index": index,
                "timestamp_seconds": index / fps,
                "timestamp_basis": "frame_index / nominal_fps",
                "image_hw": [height, width],
                "intrinsics": str(intrinsics_path) if intrinsics_path else None,
                "depth": None,
            })
            if args.max_frames and len(records) >= args.max_frames:
                break
            if args.interval_seconds == 0:
                target_index = index + 1
            else:
                target_index = max(index + 1, int(round(
                    (args.start_seconds + len(records) * args.interval_seconds) * fps
                )))
            index += 1
        if not records:
            raise RuntimeError(f"没有抽取到帧，请检查起始时间或视频：{local_video}")
    finally:
        cap.release()

    # Hash the local video so extraction provenance does not require another OSS read.
    digest = hashlib.sha256()
    with local_video.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    result = {
        "sample_id": sample_id,
        "task": task,
        "episode_uuid": episode.name,
        "camera": args.camera,
        "source_video": str(source),
        "local_video": str(local_video),
        "local_video_sha256": digest.hexdigest(),
        "copied_files": [str(p) for p in copied],
        "fps": fps,
        "video_frame_count": total_frames,
        "extracted_frames": len(records),
        "intrinsics": str(intrinsics_path) if intrinsics_path else None,
        "intrinsics_source": "undistorted_intrinsics" if intrinsics_path else None,
        "depth_sensor_metadata": depth_devices,
        "depth_payload_candidates": [str(p) for p in depth_candidates],
        "depth_search_scope": str(episode),
        "depth_status": "candidates_require_format_and_alignment_checks" if depth_candidates
                        else "no_depth_payload_in_selected_episode",
        "frames": records,
    }
    write_json(args.output_root / "metadata" / f"{sample_id}.json", result)
    print(f"已抽取 {len(records)} 帧；实际深度文件候选 {len(depth_candidates)} 个", flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset-root", type=Path,
                        default=Path("/mnt/data/opendatasets/EgoSuite-Open100K"))
    parser.add_argument("--local-video-dir", type=Path,
                        default=Path("/mnt/workspace/TEMP-FILE-STATION/egosuite_videos"))
    parser.add_argument("--output-root", type=Path, default=Path("/mnt/workspace/ego"))
    parser.add_argument("--camera", choices=["head_left_camera", "head_right_camera"],
                        default="head_left_camera")
    parser.add_argument("--num-videos", type=int, default=2)
    parser.add_argument("--interval-seconds", type=float, default=1.0,
                        help="抽帧时间间隔；0 表示逐帧输出")
    parser.add_argument("--max-frames", type=int, default=10,
                        help="每段视频最多输出几帧；0 表示不限制")
    parser.add_argument("--start-seconds", type=float, default=0.0)
    args = parser.parse_args()
    if args.num_videos <= 0 or args.max_frames < 0:
        parser.error("num-videos 必须为正数，max-frames 必须非负")
    if any(not math.isfinite(v) or v < 0 for v in (args.interval_seconds, args.start_seconds)):
        parser.error("interval-seconds 和 start-seconds 必须是非负有限数值")
    args.dataset_root = args.dataset_root.resolve()
    args.local_video_dir = args.local_video_dir.resolve()
    args.output_root = args.output_root.resolve()
    for destination in (args.local_video_dir, args.output_root):
        if destination.is_relative_to(args.dataset_root):
            parser.error("本地缓存和输出目录不能位于 OSS 数据集目录内")
    raw_root = args.dataset_root / "EgoDemo" / "EgoRaw" / "mp4"
    if not raw_root.is_dir():
        parser.error(f"未找到 EgoRaw 视频目录：{raw_root}")
    selected = select_videos(raw_root, args.camera, args.num_videos)
    reports = [extract_video(video, args) for video in selected]
    write_json(args.output_root / "extraction_manifest.json", {
        "dataset_root": str(args.dataset_root),
        "selection": "first_available_episode_per_task_sorted_by_task_name",
        "interval_seconds": args.interval_seconds,
        "max_frames_per_video": args.max_frames,
        "start_seconds": args.start_seconds,
        "videos": reports,
    })
    print(f"完成：{len(reports)} 段视频，{sum(r['extracted_frames'] for r in reports)} 张图片")
    print(f"图片目录：{args.output_root / 'images'}")
    print(f"转换记录：{args.output_root / 'extraction_manifest.json'}")


if __name__ == "__main__":
    main()
