<div align="center">
  <img src="assets/wilddet3d_banner.svg" alt="WildDet3D" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
  <br>

<a href="https://youtu.be/RgHKmOqb7I4">观看完整演示视频</a>

# WildDet3D：<br>面向真实场景的大规模提示式 3D 检测

<a href="https://allenai.org/papers/wilddet3d" target="_blank">
    <img alt="论文" src="https://img.shields.io/badge/%E8%AE%BA%E6%96%87-WildDet3D-red" height="25" />
</a>
<a href="https://huggingface.co/allenai/WildDet3D" target="_blank">
    <img alt="HF 模型：WildDet3D" src="https://img.shields.io/badge/%F0%9F%A4%97%20_%E6%A8%A1%E5%9E%8B-WildDet3D-ffc107?color=ffc107&logoColor=white" height="25" />
</a>
<a href="https://huggingface.co/datasets/allenai/WildDet3D-Data" target="_blank">
    <img alt="HF 数据集：WildDet3D 数据" src="https://img.shields.io/badge/%F0%9F%A4%97%20_%E6%95%B0%E6%8D%AE-WildDet3D--Data-ffc107?color=ffc107&logoColor=white" height="25" />
</a>
<a href="https://huggingface.co/spaces/allenai/WildDet3D" target="_blank">
    <img alt="HF 演示：WildDet3D" src="https://img.shields.io/badge/%F0%9F%A4%97%20_%E6%BC%94%E7%A4%BA-WildDet3D-ffc107?color=ffc107&logoColor=white" height="25" />
</a>
<a href="https://huggingface.co/collections/allenai/wilddet3d-69d42220ec4f942f1951263e" target="_blank">
    <img alt="HF 合集" src="https://img.shields.io/badge/%F0%9F%A4%97%20_%E5%90%88%E9%9B%86-WildDet3D-ffc107?color=ffc107&logoColor=white" height="25" />
</a>
<a href="https://apps.apple.com/us/app/wilddet3d/id6760861157" target="_blank">
    <img alt="iPhone 应用" src="https://img.shields.io/badge/%E5%BA%94%E7%94%A8%E5%95%86%E5%BA%97-WildDet3D-blue?logo=apple&logoColor=white" height="25" />
</a>
<a href="https://allenai.github.io/WildDet3D/" target="_blank">
    <img alt="项目主页" src="https://img.shields.io/badge/%E9%A1%B9%E7%9B%AE%E4%B8%BB%E9%A1%B5-WildDet3D-blue" height="25" />
</a>
<a href="https://allenai.org/blog/wilddet3d" target="_blank">
    <img alt="博客" src="https://img.shields.io/badge/%E5%8D%9A%E5%AE%A2-WildDet3D-green" height="25" />
</a>

<p style="width:80%; margin:auto">
    <a href="https://weikaih04.github.io/" target="_blank">Weikai Huang</a><sup style="color:#FF69B4">&#9829;</sup><sup>1,2</sup>&nbsp;&nbsp;
    <a href="https://jieyuz2.github.io/" target="_blank">Jieyu Zhang</a><sup style="color:#FF69B4">&#9829;</sup><sup>1,2</sup>
    <br>
    <a href="https://github.com/Silicon23" target="_blank">Sijun Li</a><sup>2</sup>&nbsp;&nbsp;
    <a href="https://github.com/taoyangJ" target="_blank">Taoyang Jia</a><sup>2</sup>&nbsp;&nbsp;
    <a href="https://duanjiafei.com/" target="_blank">Jiafei Duan</a><sup>1,2</sup>&nbsp;&nbsp;
    <a href="https://scholar.google.com/citations?user=Li5XdUsAAAAJ" target="_blank">Yunqian Cheng</a><sup>1</sup>&nbsp;&nbsp;
    <a href="https://j-min.io/" target="_blank">Jaemin Cho</a><sup>1,2</sup>&nbsp;&nbsp;
    <a href="https://mattwallingford.github.io/" target="_blank">Matthew Wallingford</a><sup>1</sup>&nbsp;&nbsp;
    <a href="https://github.com/RustinS" target="_blank">Rustin Soraki</a><sup>1,2</sup>&nbsp;&nbsp;
    <a href="https://cdjkim.github.io/" target="_blank">Chris Dongjoo Kim</a><sup>1</sup>&nbsp;&nbsp;
    <a href="https://shuoliu1024.github.io/" target="_blank">Shuo Liu</a><sup>1,2</sup>&nbsp;&nbsp;
    <a href="https://www.linkedin.com/in/donovanclay/" target="_blank">Donovan Clay</a><sup>1,2</sup>&nbsp;&nbsp;
    <a href="https://www.linkedin.com/in/taira-anderson/" target="_blank">Taira Anderson</a><sup>1</sup>&nbsp;&nbsp;
    <a href="https://winsonhan.com/" target="_blank">Winson Han</a><sup>1</sup>
    <br>
    <a href="https://homes.cs.washington.edu/~ali/" target="_blank">Ali Farhadi</a><sup>1,2</sup>&nbsp;&nbsp;
    <a href="https://www.cs.cornell.edu/~bharathh/" target="_blank">Bharath Hariharan</a><sup>3</sup>&nbsp;&nbsp;
    <a href="https://jason718.github.io/" target="_blank">Zhongzheng Ren</a><sup style="color:#FF69B4">&#9829;</sup><sup>1,2,4</sup>&nbsp;&nbsp;
    <a href="https://ranjaykrishna.com/" target="_blank">Ranjay Krishna</a><sup style="color:#FF69B4">&#9829;</sup><sup>1,2</sup>
</p>

<p>
<span style="color:#FF69B4">&#9829;</span> 核心贡献者 &nbsp;&nbsp;
<sup>1</sup>艾伦人工智能研究所&nbsp;&nbsp;&nbsp;&nbsp;<sup>2</sup>华盛顿大学&nbsp;&nbsp;&nbsp;&nbsp;<sup>3</sup>康奈尔大学&nbsp;&nbsp;&nbsp;&nbsp;<sup>4</sup>北卡罗来纳大学教堂山分校
</p>

</div>

<a id="demo--applications"></a>

## 演示与应用

<table>
<tr>
<td align="center">
<a href="demo/huggingface/README.md"><img src="assets/demo_huggingface.png" height="200"></a>
</td>
<td align="center">
<a href="demo/iphone/README.md"><img src="assets/demo_iphone.png" height="200"></a>
</td>
</tr>
<tr>
<td align="center">
<b>HuggingFace 交互式演示</b>
<br>支持文本、点和框提示的交互式网页演示
<br><a href="https://huggingface.co/spaces/allenai/WildDet3D">在线演示</a> | <a href="demo/huggingface/README.md">本地运行</a>
</td>
<td align="center">
<b>iPhone 应用</b>
<br>设备端实时 3D 检测
<br><a href="https://apps.apple.com/us/app/wilddet3d/id6760861157">应用商店</a> | <a href="https://youtu.be/LJPNJ8jpOao">视频</a> | <a href="demo/iphone/README.md">说明文档</a>
</td>
</tr>
<tr><td colspan="2"></td></tr>
<tr>
<td align="center">
<a href="demo/vlm/README.md"><img src="assets/demo_vlm.png" height="200"></a>
</td>
<td align="center">
<a href="demo/tracking/README.md"><img src="assets/demo_tracking.gif" height="200"></a>
</td>
</tr>
<tr>
<td align="center">
<b>与视觉语言模型集成</b>
<br>结合视觉语言模型使用
<br><a href="demo/vlm/README.md">说明文档</a>
</td>
<td align="center">
<b>零样本跟踪</b>
<br>无需额外训练的 3D 目标跟踪
<br><a href="demo/tracking/README.md">说明文档</a>
</td>
</tr>
<tr><td colspan="2"></td></tr>
<tr>
<td align="center">
<a href="demo/meta_quest/README.md"><img src="assets/demo_meta_quest.gif" height="200"></a>
</td>
<td align="center">
<a href="demo/robotics/README.md"><img src="assets/demo_robotics.gif" height="200"></a>
</td>
</tr>
<tr>
<td align="center">
<b>Meta Quest</b>
<br>增强现实／虚拟现实中的 3D 检测
<br><a href="assets/demo_meta_quest.mp4">视频</a>
</td>
<td align="center">
<b>机器人应用</b>
<br>用于机器人操作的 3D 感知
<br><a href="assets/demo_robotics.mp4">视频</a>
</td>
</tr>
<tr><td colspan="2"></td></tr>
<tr>
<td align="center" colspan="2">
<a href="demo/boxer/README.md"><img src="assets/demo_boxer.gif" height="200"></a>
</td>
</tr>
<tr>
<td align="center" colspan="2">
<b>集成 Meta FAIR 的 Boxer 演示，用于室内标注</b>
<br>WildDet3D 在面向 Project Aria 的 <a href="https://github.com/facebookresearch/boxer">Meta FAIR Boxer</a> 室内标注流程中替代 OWL + BoxerNet。Boxer 的 AriaLoader、离线融合、在线跟踪器及 3D 查看器均可直接使用本项目输出，无需修改。
<br><a href="demo/boxer/README.md">说明文档</a>
</td>
</tr>
</table>

<a id="news"></a>

## 更新动态

- **2026-05-20** — 发布 Omni3D、ScanNet、Argoverse 2 评测配置（文本／框提示 × 单目／真实深度，每个数据集各 4 种模式）。 ([#15](https://github.com/allenai/WildDet3D/pull/15))
- **2026-05-18** — 新增 Boxer 演示：将 WildDet3D 作为检测器接入面向 Project Aria 的 [Meta FAIR Boxer](https://github.com/facebookresearch/boxer) 室内标注流程。 ([#13](https://github.com/allenai/WildDet3D/pull/13))
- **2026-05-17** — 发布 FoundationPose 数据准备脚本（数据提取、3D 包围框、Qwen-VLM 分类）。 ([#12](https://github.com/allenai/WildDet3D/pull/12))
- **2026-04-27** — 修复跟踪及 HuggingFace／VLM 演示中的坐标变换问题。 ([#8](https://github.com/allenai/WildDet3D/pull/8), [#9](https://github.com/allenai/WildDet3D/pull/9))
- **2026-04-19** — 发布训练代码、WildDet3D-Data 数据准备脚本，并修复推理与可视化问题。 ([#6](https://github.com/allenai/WildDet3D/pull/6))
- **2026-04-07** — 首次发布：推理代码、WildDet3D-Bench 评测、HuggingFace Space、iPhone 应用及项目主页。

<a id="todo"></a>

## 开发计划

- [x] 发布推理代码
- [x] 发布 WildDet3D-Bench 评测
- [x] 发布训练代码
- [x] 发布其他基准的评测（Omni3D、Argoverse2、ScanNet）
- [ ] 发布 WildDet3D-Embodied：在 Droid 等机器人数据上微调 WildDet3D，使其更适合机器人应用或用作机器人模型的骨干网络。

<a id="contents"></a>

## 目录

- [演示与应用](#demo--applications)
- [更新动态](#news)
- [模型权重](#model-weights)
- [安装](#installation)
- [阿里云 PPU 推理环境](#aliyun-ppu)
- [ego 数据预标注](#ego-preannotation)
- [VS Code SSH 与网页演示](#vscode-ssh)
- [推理](#inference)
- [评测](#evaluation)
  - [WildDet3D-Bench](#wilddet3d-bench)
  - [WildDet3D-Stereo4D-Bench](#wilddet3d-stereo4d-bench)
- [训练](#training)
  - [训练数据准备](#training-data-preparation) &rarr; 参阅 [docs/TRAINING_DATA.md](docs/TRAINING_DATA.md)
- [实验结果](#results)
  - [WildDet3D-Bench（真实场景）](#wilddet3d-bench-in-the-wild)
  - [Omni3D](#omni3d)
  - [零样本迁移（Argoverse 2 + ScanNet）](#zero-shot-transfer-argoverse-2--scannet)
- [WildDet3D 数据集](#wilddet3d-data)
- [引用](#citation)
- [致谢](#acknowledgements)
- [许可证](#license)

<a id="model-weights"></a>

## 模型权重

PPU 用户先完成[专用安装流程](#aliyun-ppu)，再按其中第 5 步从 OSS 挂载复制阶段 3 权重和 LingBot 的 `model.pt` 到本地。以下保留原项目命令；`huggingface-cli` 取决于已安装的 Hub 版本。

| 权重文件 | 阶段 | 训练方案 | 大小 | 下载 |
|---|---|---|---|---|
| `wilddet3d_alldata_all_prompt_v1.0.pt` | 阶段 3（论文模型） | 阶段 2 权重 &rarr; Omni3D + ITW-human 混合提示微调，3 轮 | ~4.7 GB | [allenai/WildDet3D](https://huggingface.co/allenai/WildDet3D/resolve/main/wilddet3d_alldata_all_prompt_v1.0.pt) |
| `wilddet3d_stage2_alldata_12e_v1.0.pt` | 阶段 2（中间权重） | 阶段 1 权重 &rarr; 8 个数据集的全量数据微调，12 轮 | ~4.7 GB | [allenai/WildDet3D](https://huggingface.co/allenai/WildDet3D/resolve/main/wilddet3d_stage2_alldata_12e_v1.0.pt) |
| `wilddet3d_stage1_omni3d_12e_v1.0.pt` | 阶段 1（中间权重） | 仅使用 Omni3D、规范旋转表示，从头训练 12 轮 | ~4.7 GB | [allenai/WildDet3D](https://huggingface.co/allenai/WildDet3D/resolve/main/wilddet3d_stage1_omni3d_12e_v1.0.pt) |

三个权重采用相同架构（SAM3 ViT 骨干网络 + LingBot-Depth DINOv2 ViT-L/14 几何后端，约 12 亿参数），保存格式均为移除优化器状态后的 `state_dict` + `epoch`/`step` + `hparams`。按需要选择相应阶段；复现论文结果或直接推理时，使用 `wilddet3d_alldata_all_prompt_v1.0.pt`。

```bash
# 下载论文发布权重（约 4.7 GB）
pip install huggingface_hub
huggingface-cli download allenai/WildDet3D wilddet3d_alldata_all_prompt_v1.0.pt --local-dir ckpt/
```

**中间阶段权重（用于部分复现三阶段训练，直接推理无需下载）：**

```bash
# 阶段 1：仅使用 Omni3D、规范旋转，12 轮（约 4.7 GB）
huggingface-cli download allenai/WildDet3D wilddet3d_stage1_omni3d_12e_v1.0.pt --local-dir ckpt/

# 阶段 2：从阶段 1 开始，在 8 个数据集上全量微调 12 轮（约 4.7 GB）
huggingface-cli download allenai/WildDet3D wilddet3d_stage2_alldata_12e_v1.0.pt --local-dir ckpt/
```

如何将这些权重作为下一阶段的起点，请参阅 [`docs/TRAINING.md`](docs/TRAINING.md)。

<a id="installation"></a>

## 安装

阿里云 PPU 用户请先阅读下方专用流程，**不要执行本节 NVIDIA 安装命令**。

### 原项目 NVIDIA 环境（参考）

```bash
git clone --recurse-submodules https://github.com/allenai/WildDet3D.git
cd WildDet3D
# 克隆时若忘记 --recurse-submodules，执行下一行：
# git submodule update --init --recursive

# 训练还需要 MoGe（深度后端损失函数）；仅推理不需要：
# git clone https://github.com/microsoft/moge.git third_party/moge

conda create -n wilddet3d python=3.11 -y
conda activate wilddet3d

# 1. PyTorch（原项目测试的 CUDA／版本组合，仅用于 NVIDIA）
pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu121

# 2. vis4d（固定原项目使用的版本，复用上述 torch）
pip install vis4d==1.0.0

# 3. vis4d CUDA 算子（从源码编译，供 wilddet3d/ops 使用）
pip install git+https://github.com/SysCV/vis4d_cuda_ops.git --no-build-isolation --no-cache-dir

# 4. 其余依赖（包含 sam3 的间接依赖；
#    wilddet3d/__init__.py 通过 sys.path 加载 third_party/sam3，
#    因此不需要单独安装 sam3）
pip install -r requirements.txt
```

<a id="aliyun-ppu"></a>

### 阿里云 PPU 推理环境

本节面向**直接加载已发布权重，对第一人称（ego）图像进行推理、生成预标注**的场景，不涉及训练。目标镜像为 `2.1.0-pytorch2.6.0-ppu-py312-cu128-ubuntu24.04`，通过 VS Code Remote SSH 连接 DSW 实例。

**验证状态（2026-09-30）：已在当前虚拟环境验证 WildDet3D 导入，并在 `HF_HUB_OFFLINE=1` 下读取两个本地模型文件、在 CPU 上完成完整模型构建与权重加载；尚未完成 PPU 扩展运行或真实图像推理验证，不能视为 PPU 推理已经跑通。** 已获准将 SAM3 的 EDT 导入改为按需加载，并为 `build_model()` 增加 LingBot 本地文件参数；未修改依赖清单。下方 PPU 算子与推理检查仍需在实际 DSW 终端执行。

| 项目 | 当前确认的信息 |
|---|---|
| 加速卡 | 单卡 PPU-ZW810E，98304 MiB（96 GiB）设备内存 |
| 设备状态 | 用户在 DSW 终端执行 `ppu-smi` 可正常识别设备 |
| 驱动／管理工具 | 驱动 `2.0.0-2e1b14`；PPU-SMI `1.28`；工具显示 HGGC `13.0` |
| 操作系统／Python | 目标镜像 Ubuntu 24.04；当前 Python 3.12.3 |
| PyTorch 包版本 | `2.6.0+v0.1.0.ppu2.1.0.oe` |
| torchvision 包版本 | `0.21.0+v0.1.0.ppu2.1.0.ce` |
| PyTorch CUDA API／编译入口 | `torch.version.cuda` 为 `12.8`；`/usr/local/PPU_SDK/CUDA_SDK/bin/nvcc` |
| 初始仓库状态 | SAM3、LingBot-Depth 子模块未初始化；未安装 vis4d、vis4d_cuda_ops、Gradio |

PPU 的兼容层允许继续使用 `device="cuda"`、`.cuda()` 等接口，不应仅因硬件名称是 PPU 就把它们改为 `.ppu()`。**保留镜像预装的 PPU 专用 torch／torchvision**；镜像名称中的 `cu128` 不代表可以安装普通 NVIDIA CUDA wheel。PPU 提供源码级兼容，其设备二进制不能与 NVIDIA 混用；CUDA 扩展需经 PPU 工具链重新编译。参阅[阿里云 SDK 兼容性说明](https://help.aliyun.com/en/document_detail/2997009.html)及[PPU 编译器指南](https://help.aliyun.com/zh/document_detail/3030344.html)。这些通用说明并不等于 WildDet3D 已获得 PPU 兼容认证。

#### 1. 在实际 DSW 终端检查设备和基础算子

以下命令在 VS Code 的**远程终端**中执行，而不是本地电脑终端。先检查镜像的原始 Python，再建立虚拟环境。`ppu-smi` 的 HGGC 版本与 PyTorch 的 CUDA API 版本含义不同，不需要因为两者不同就更换 SDK。

```bash
cd /mnt/workspace/WildDet3D
ppu-smi
command -v python nvcc
nvcc --version
python -m pip show torch torchvision

python -B - <<'PY'
import torch
import torchvision
from torchvision.ops import nms
from torch.utils.cpp_extension import CUDA_HOME

print("PyTorch:", torch.__version__)
print("torchvision:", torchvision.__version__)
print("CUDA API:", torch.version.cuda)
print("CUDA_HOME:", CUDA_HOME)
assert torch.cuda.is_available(), "当前 Python 无法访问 PPU，请先检查实例设备挂载和驱动"
print("设备:", torch.cuda.get_device_name(0))

x = torch.ones((16, 16), device="cuda")
assert torch.allclose(x @ x, torch.full_like(x, 16))
boxes = torch.tensor([[0., 0., 10., 10.], [1., 1., 9., 9.]], device="cuda")
scores = torch.tensor([0.9, 0.8], device="cuda")
assert nms(boxes, scores, 0.5).tolist() == [0]
torch.cuda.synchronize()
print("PPU 矩阵运算与 torchvision NMS 检查通过")
PY
```

必须同时确认设备查询和 Python 算子检查通过。若受限工具环境报告驱动未加载，而 DSW 终端正常，应以实际运行项目的终端继续验证；不要据此重装驱动。源码中使用了 CUDA Stream，不能把 CPU 回退当作已适配 PPU。

#### 2. 建立复用 PPU 包的虚拟环境

使用镜像自带的 Python 3.12 创建环境，并通过 `--system-site-packages` 读取预装的 PPU 包。不要按 NVIDIA 路径另建 Python 3.11 环境再安装普通 torch。首次使用下列环境目录；如目录已存在，先确认它确实属于本项目。

```bash
python -m venv --system-site-packages /mnt/workspace/venvs/wilddet3d-ppu
source /mnt/workspace/venvs/wilddet3d-ppu/bin/activate
python -m pip --version
python -m pip check  # 记录安装前已有的依赖冲突，供后续对比

cd /mnt/workspace/WildDet3D
git submodule update --init --recursive
git submodule status
```

子模块版本应与主仓库记录一致，不要额外执行 `git submodule update --remote`。仅推理不需要克隆 MoGe；其损失函数在训练时才延迟导入。VS Code 中将 Python 解释器选择为 `/mnt/workspace/venvs/wilddet3d-ppu/bin/python`。

#### 3. 生成安装清单，保护镜像的 PPU 包

根目录 `requirements.txt` 固定 `torch==2.5.1`、`torchvision==0.20.1`，因此**不要在此环境直接执行 `pip install -r requirements.txt`**。以下命令在虚拟环境目录生成临时安装材料，过滤这两个固定版本及仅数据准备使用的 `pyarrow`，不改仓库原文件；同时按已安装包的完整版本约束 PPU 组件。

```bash
python - <<'PY'
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import re
import sys

target = Path(sys.prefix)
assert sys.prefix != sys.base_prefix, "请先激活 wilddet3d-ppu 虚拟环境"
constraints = []
for name in ("torch", "torchvision", "torchaudio", "triton"):
    try:
        constraints.append(f"{name}=={version(name)}")
    except PackageNotFoundError:
        if name in ("torch", "torchvision"):
            raise
# 与 vis4d 的 NumPy 1.x 约束、SAM3 的 pkg_resources 导入保持一致。
# 其余范围用于减少上游大版本变化；仍须通过后面的实际导入／推理验证。
constraints += [
    "numpy<2", "setuptools<80", "opencv-python<4.12",
    "transformers<5", "huggingface_hub<1",
]
(target / "ppu-constraints.txt").write_text("\n".join(constraints) + "\n")
lines = Path("requirements.txt").read_text().splitlines()
filtered = []
for line in lines:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        continue
    if re.match(r"^(torch|torchvision|pyarrow)(?:\s|[<>=!~;\[]|$)", stripped):
        continue
    filtered.append(line)
(target / "wilddet3d-inference-requirements.txt").write_text("\n".join(filtered) + "\n")
print((target / "ppu-constraints.txt").read_text())
PY

export PIP_CONSTRAINT="$VIRTUAL_ENV/ppu-constraints.txt"

# 先查看解析结果；如果提出替换 torch／torchvision，先停止并检查环境。
python -m pip install --dry-run vis4d==1.0.0 \
    -r "$VIRTUAL_ENV/wilddet3d-inference-requirements.txt" ninja wheel psutil

# 确认解析结果后，再执行实际安装。
python -m pip install vis4d==1.0.0 \
    -r "$VIRTUAL_ENV/wilddet3d-inference-requirements.txt" ninja wheel psutil
```

约束文件的作用是遇到不兼容依赖时让 pip 报错，而不是悄悄替换 PPU 包。`--system-site-packages` 并不意味着虚拟环境完全隔离：新增版本会在虚拟环境中遮蔽系统包，仍应核对解析结果。若提示找不到这些带 PPU 后缀的版本，先核实是否正在使用正确的镜像 Python 和虚拟环境，不要删除保护约束改装普通包。

`utils3d` 必须来自 `EasternJournalist/utils3d` Git 仓库，不能以 PyPI 上同名的无关包替代。这里沿用根目录依赖清单的 Git 地址。不要直接叠加 `demo/huggingface/requirements.txt`：它的 `pydantic>=2` 与 vis4d 的约束冲突，也包含不适合直接照搬的 `utils3d` 条目，详见[网页演示说明](#vscode-ssh)。

<a id="ppu-opencv-system-libs"></a>

**补充 OpenCV 系统运行库（Ubuntu 24.04）**

当前使用的 `opencv-python` 包依赖 OpenGL 和 GLib 系统动态库。精简的 DSW 镜像可能未包含这些库，使 `import cv2` 失败，并通过 `vis4d.data.transforms.resize` 阻断 WildDet3D 导入。已确认本实例缺少以下库：

| 缺失动态库 | Ubuntu 24.04 对应软件包 |
|---|---|
| `libGL.so.1` | `libgl1` |
| `libgthread-2.0.so.0`、`libglib-2.0.so.0` | `libglib2.0-0t64` |

在服务器 SSH 终端执行以下命令；当前用户为 root，无需 `sudo`。可以保持虚拟环境激活，但 `apt-get` 安装的是实例的系统运行库，不是虚拟环境中的 Python 包。这一步无需修改项目代码或重装 PyTorch，也不要同时混装多个提供 `cv2` 的 OpenCV 包。

```bash
apt-get update
apt-get install -y --no-install-recommends libgl1 libglib2.0-0t64

# 使用已激活的 wilddet3d-ppu 环境，先单独验证 OpenCV。
python -B -c 'import cv2; print("OpenCV 导入通过:", cv2.__version__)'
```

完成后继续第 4 步的扩展编译与项目导入检查。如果之前已经编译过扩展，只因缺少上述动态库而导入失败，则不需要因此重新编译，可直接重新执行：

```bash
cd /mnt/workspace/WildDet3D
python -B -c 'from wilddet3d import build_model, preprocess; print("WildDet3D 导入通过")'
python -m pip check
```

上述命令用于修复并验证 OpenCV 的动态库问题；出现新的异常时，应按新的完整堆栈继续定位，不能将补齐系统库等同于模型推理已通过。

#### 4. 用 PPU 工具链编译 vis4d_cuda_ops

仅在第 1 步的 `torch.cuda.is_available()` 和算子检查通过后编译。上游构建脚本依据设备可见性选择 CUDA 或 CPU 扩展，设备不可见时“安装成功”并不代表编译出了 PPU 算子。参阅[上游构建脚本](https://github.com/SysCV/vis4d_cuda_ops/blob/main/setup.py)。

```bash
export CUDA_HOME=/usr/local/PPU_SDK/CUDA_SDK
export PATH="$CUDA_HOME/bin:$PATH"
export MAX_JOBS=4
command -v nvcc
nvcc --version

# ninja 已在上一步安装；--no-deps 防止扩展安装再次解析核心依赖。
# --no-build-isolation 使编译使用当前环境的 PPU PyTorch。
python -m pip install \
    git+https://github.com/SysCV/vis4d_cuda_ops.git \
    --no-build-isolation --no-cache-dir --no-deps
```

这里的 `nvcc` 应是 PPU SDK 的兼容编译入口，不是另行安装的 NVIDIA Toolkit。不要照抄其他 GPU 的 `TORCH_CUDA_ARCH_LIST`。若发生架构、PTX、编译选项或未支持算子错误，保留完整编译日志后再评估补丁；当前文档不保证该扩展能无修改编译。

编译后运行小规模检查，验证 3D IoU 在 PPU 上执行，而不只检查模块能否导入：

```bash
python -B - <<'PY'
import torch
from vis4d_cuda_ops import iou_box3d

corners = torch.tensor([
    [0., 0., 0.], [1., 0., 0.], [1., 1., 0.], [0., 1., 0.],
    [0., 0., 1.], [1., 0., 1.], [1., 1., 1.], [0., 1., 1.],
], device="cuda").unsqueeze(0).contiguous()
volume, iou = iou_box3d(corners, corners)
torch.cuda.synchronize()
assert torch.allclose(iou, torch.ones_like(iou), atol=1e-4), (volume, iou)
print("PPU 3D IoU 检查通过")
PY

export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"
export SAM3_COMPILE=0
python -B -c 'from wilddet3d import build_model, preprocess; print("WildDet3D 导入通过")'
python -m pip check
```

`pip check` 可能同时报告继承自基础镜像的包冲突，应与安装前环境区分，但不能把新出现的项目依赖冲突当作验证通过。若 SAM3 或其他模块报 Triton／FlashAttention／xFormers 相关错误，需检查准确的导入路径并使用匹配当前 PPU SDK 的包；**不要直接安装 NVIDIA 版本，也不要用空模块绕过错误**。关闭 `SAM3_COMPILE` 不能消除所有可能的底层加速库依赖。

本实例的基础环境还存在 `mkl==2021.1.1` 缺少 `intel-openmp==2021.*`、`tbb==2021.*` 的依赖问题，虚拟环境会通过 `--system-site-packages` 继承这些信息。这与 OpenCV 缺少 `libGL.so.1` 是两件事，安装 OpenGL／GLib 不会消除 MKL 的提示；应单独评估处理，不能宣称 `pip check` 已全部通过。`libjpeg.so.8` 的 torchvision 警告及 `timm.models.layers` 的弃用警告也不是此次 OpenCV 导入中断的原因。

#### 5. 从 OSS 挂载复制推理权重到本地，并准备深度模型配置来源

只需要阶段 3 的 WildDet3D 权重，以及 LingBot-Depth 的 `model.pt`，不需要阶段 1／2 或训练数据集。由于 DSW 访问外网下载较慢，这两个文件已存放在 OSS 挂载中；本流程每次运行前将它们复制到本地暂存目录，再通过显式文件路径加载。

| 用途 | 路径 |
|---|---|
| WildDet3D 的 OSS 源文件 | `/mnt/lvyifan/wilddet3d_alldata_all_prompt_v1.0.pt` |
| WildDet3D 的本地文件 | `/mnt/workspace/TEMP-FILE-STATION/wilddet3d_alldata_all_prompt_v1.0.pt` |
| LingBot-Depth 的 OSS 源文件 | `/mnt/lvyifan/model.pt` |
| LingBot-Depth 的本地文件 | `/mnt/workspace/TEMP-FILE-STATION/model.pt` |

**先复制两个模型文件。** 以下命令在服务器 SSH 终端执行。每次执行都会重新从 OSS 读取并复制，不会因为本地已有文件而跳过。每个文件先写入 `.part` 临时文件，复制成功且文件大小一致后，再替换本地正式文件；中途中断时，该文件已有的正式副本仍保留，下次重新执行即可。WildDet3D 权重约 4.7 GB，LingBot 文件约 1.28 GB；若已有旧文件，复制期间还需预留当前文件的一份临时副本空间。大小核对只用于检查长度一致，不代替校验和验证。

```bash
(
    set -e
    mkdir -p /mnt/workspace/TEMP-FILE-STATION
    for weight_name in wilddet3d_alldata_all_prompt_v1.0.pt model.pt; do
        oss_weight="/mnt/lvyifan/$weight_name"
        local_weight="/mnt/workspace/TEMP-FILE-STATION/$weight_name"
        test -s "$oss_weight"
        cp -- "$oss_weight" "${local_weight}.part"
        test "$(stat -c %s "$oss_weight")" -eq "$(stat -c %s "${local_weight}.part")"
        mv -f -- "${local_weight}.part" "$local_weight"
        ls -lh "$local_weight"
    done
)
```

`/mnt/lvyifan` 是 OSS 挂载，复制过程仍会读取 OSS 数据，但不需要从外网下载。后续推理的 `checkpoint` 和 `lingbot_pretrained_model` 必须使用上表中的本地路径；不要将指向 OSS 源文件的软链接当成本地副本。

**检查 LingBot 本地文件。** `build_model()` 已增加 `lingbot_pretrained_model` 参数，可以直接传入本地 `model.pt` 路径；省略参数时仍使用原来的 HuggingFace 仓库地址。`skip_pretrained=True` 仍需读取此文件中的 `model_config`，随后模型权重由 WildDet3D 阶段 3 文件加载。

下面直接读取本地文件，不查询 HuggingFace 缓存。下载到暂存目录的文件无需转换成 Hub 缓存结构，也不再需要执行之前的 `hf_hub_download(..., local_files_only=True)` 检查。

```bash
source /mnt/workspace/venvs/wilddet3d-ppu/bin/activate
cd /mnt/workspace/WildDet3D
python -B - <<'PY'
from pathlib import Path
import torch

path = Path("/mnt/workspace/TEMP-FILE-STATION/model.pt")
assert path.is_file(), f"LingBot 文件不存在：{path}"
ckpt = torch.load(path, map_location="cpu", weights_only=True)
assert isinstance(ckpt, dict) and isinstance(ckpt.get("model_config"), dict), \
    "文件中缺少有效的 model_config，请确认下载的是对应 LingBot 模型的 model.pt"
print("LingBot 本地配置读取通过：", path)
PY
```

**调用本地权重。** 完成两个文件的本地复制后，可以先单独检查模型加载。下面使用 `HF_HUB_OFFLINE=1` 禁止本次命令访问 Hub，并通过两个路径参数直接读取本地文件。

```bash
source /mnt/workspace/venvs/wilddet3d-ppu/bin/activate
cd /mnt/workspace/WildDet3D
export SAM3_COMPILE=0
HF_HUB_OFFLINE=1 python -B - <<'PY'
from wilddet3d import build_model

model = build_model(
    checkpoint="/mnt/workspace/TEMP-FILE-STATION/wilddet3d_alldata_all_prompt_v1.0.pt",
    lingbot_pretrained_model="/mnt/workspace/TEMP-FILE-STATION/model.pt",
    skip_pretrained=True,
    canonical_rotation=True,
    score_threshold=0.3,
    device="cuda",
)
print("本地权重模型加载通过")
PY
```

模型加载通过后，继续运行下方的 ego 数据预标注示例，它已使用相同的两个本地路径。这种调用无需预先准备 LingBot 的 Hub 缓存；若遗漏 `lingbot_pretrained_model`，仍会走默认的仓库／缓存查找流程。加载成功只是检查权重与模型构建，完成单张图的前向推理和输出核对后才算跑通最小流程。

#### 6. 首次推理与故障定位

先运行[ego 数据预标注示例](#ego-preannotation)，从单张图开始。采用 FP32、`SAM3_COMPILE=0`，不调用 `optimize_for_inference()`。完成图像输入、模型加载、前向推理和输出核对后，才算跑通最小流程。96 GiB 是设备容量，不是已经测得的模型峰值占用。

| 现象 | 优先检查 |
|---|---|
| DSW 能看到 PPU，Python 看不到 | 当前解释器、设备挂载及可见设备设置；不要把受限工具的失败直接等同于驱动损坏 |
| pip 要求安装 torch 2.5.1 | 是否误用原 `requirements.txt`，或未设置保护约束 |
| `No module named sam3`／`mdm` | 子模块是否完整，以及是否从项目根目录执行 |
| `No module named vis4d_cuda_ops`／`undefined symbol` | 扩展是否在当前 PPU PyTorch 环境重新编译；是否混入 NVIDIA 二进制 |
| NMS 无法在 CUDA 设备执行 | 检查是否仍在使用镜像提供的 PPU torchvision，并重跑基础算子检查 |
| `utils3d` 缺少 `pt`／`np` | 核实是否装成了 PyPI 同名包，应使用项目指定的 Git 仓库版本 |
| `pkg_resources` 无法导入 | 核实当前环境是否保持 `setuptools<80` |
| torchvision 提示缺少 `libjpeg.so.8` | 当前镜像的图像扩展警告；本页用 Pillow 读取图像，仍须单独验证 NMS，不能据此忽略所有 torchvision 错误 |
| 缺少 `libGL.so.1`／`libgthread-2.0.so.0`／`libglib-2.0.so.0` | 按[OpenCV 系统运行库步骤](#ppu-opencv-system-libs)安装 `libgl1`、`libglib2.0-0t64`，先验证 `import cv2`，再验证 WildDet3D 导入 |
| `mkl 2021.1.1 requires intel-openmp`／`tbb` | 已确认是基础镜像已有的依赖缺失，与 OpenCV 动态库错误分开处理；安装 OpenGL／GLib 不会修复此项 |
| 从 OSS 复制权重后仍访问 HuggingFace | `checkpoint` 与 `lingbot_pretrained_model` 是否都传入本地暂存路径；是否设置 `skip_pretrained=True`；网页仍需检查其默认 LingBot 缓存及本地 WildDet3D 文件名 |
| 编译／Triton／注意力算子报错 | 记录具体堆栈，确认 PPU 软件栈支持情况，再决定是否需要获准修改代码 |
| 图像能推理但 3D 框尺度或投影不正确 | 检查相机内参、图像旋转／裁剪、畸变、深度单位、尺寸顺序与坐标系 |

每次重新连接 SSH 后，至少恢复以下环境变量；安装新依赖时仍保留 `PIP_CONSTRAINT`：

```bash
source /mnt/workspace/venvs/wilddet3d-ppu/bin/activate
cd /mnt/workspace/WildDet3D
export PIP_CONSTRAINT="$VIRTUAL_ENV/ppu-constraints.txt"
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"
export HF_HOME=/mnt/workspace/.cache/wilddet3d-huggingface
export SAM3_COMPILE=0
```

<a id="ego-preannotation"></a>

### ego 数据预标注

当前目标是使用已训练权重生成预标注，无需执行后文的训练或基准评测。下面提供**普通 RGB 图片目录 → 逐张推理 → 项目自定义 JSON + 画框预览图**的入口。此 JSON 是便于后续转换的中间结果，并非某个标注平台可直接导入的标准格式。当前已从 EgoSuite 的 OSS 挂载复制两段去畸变头戴视频到本地并抽取 19 张图片，保存在 `/mnt/workspace/ego/images`；所选 episode 中没有实际深度数据，可以先使用单目模式。

| 数据情况 | 使用方式 |
|---|---|
| 普通 RGB 图片 | 先对少量图片运行文本提示，检查类别与框质量 |
| 普通视频 | 先按任务需要抽帧并保留原视频名、帧号、时间戳；逐帧检测不自动产生跨帧实例 ID |
| 已有 2D 框 | 使用 `input_boxes` 与 `prompt_text="geometric"`；提示框坐标为原图像素 xyxy；首次先对单张图中的单个框验证 |
| 有真实内参 | 传入与当前图像分辨率、裁剪和旋转一致的 3×3 内参矩阵 |
| 无内参 | 可先用默认内参观察结果，但不能将预测尺度视为标定真值；若启用 `use_predicted_intrinsics=True`，还需正确保存和还原预测内参 |
| 有深度 | 将深度对齐到输入 RGB，保持原图分辨率、float32、单位米，同时设置 `use_depth_input_test=True`、`preprocess(..., depth=...)`、`depth_gt=...` |
| 鱼眼／广角 ego 相机 | 先使用真实标定将图像转换到合适的针孔视图，并使用变换后的内参；仅填写四个内参数值不能替代去畸变 |
| Project Aria VRS／位姿数据 | 参阅 [Boxer 集成说明](demo/boxer/README.md)，涉及额外依赖和坐标变换，尚未在本 PPU 实例验证 |

下面的示例可直接复制到激活了 `wilddet3d-ppu` 的服务器终端执行。`max_images = None` 会处理全部图片（当前抽帧样本共 19 张）；设为 `1` 则只处理排序后的第一张，即使这张已有 JSON，也不会自动继续到第二张。新推理会从抽帧脚本生成的 `extraction_manifest.json` 按图片查找对应内参；也可用 `intrinsics_path` 显式指定统一内参，但仅适用于同一相机和图像几何处理。没有标定时仍使用默认内参，并在 JSON 中记录来源。

结果 JSON 保存在 `/mnt/workspace/ego/wilddet3d_predictions`，画框图片保存在 `/mnt/workspace/ego/wilddet3d_visualizations`，都保留输入的子目录结构。**已有 JSON 会直接用于画图，不会重复推理或覆盖预测记录。** 若要改类别或使用真实内参重新推理，设置新的 `output_dir` 和 `visualization_dir`（例如各加 `_calibrated` 后缀），避免复用旧结果。旧 JSON 的 3D 框必须用它保存的 `intrinsics_original` 投影，不能只换绘图内参来修正预测。

本示例明确要求 **2D 分数和 3D 分数都不低于 0.5**，满足条件的目标另存到 `/mnt/workspace/ego/wilddet3d_predictions_filtered`。原始 JSON 保留用于复用和调整阈值；筛选后的 JSON 与预览图使用同一批目标。这里调整的是置信度阈值，不会更改模型权重。预览图叠加彩色 3D 框，并保留类别和分数文字标签，不显示 2D 矩形。

```bash
python - <<'PY'
import json
from itertools import islice
from pathlib import Path

import numpy as np
import torch
from PIL import Image
from wilddet3d import build_model, preprocess
from wilddet3d.vis.visualize import draw_3d_boxes

image_dir = Path("/mnt/workspace/ego/images")  # 改为真实图片目录
output_dir = Path("/mnt/workspace/ego/wilddet3d_predictions")
filtered_output_dir = Path("/mnt/workspace/ego/wilddet3d_predictions_filtered")
visualization_dir = Path("/mnt/workspace/ego/wilddet3d_visualizations")
manifest_path = Path("/mnt/workspace/ego/extraction_manifest.json")
intrinsics_path = None  # None：优先按抽帧记录读取各张图片的内参
class_names = ["cardboard box", "basket", "shelf"]
max_images = None  # 处理全部图片；设为 1 则只处理第一张
score_2d_threshold = 0.5
score_3d_threshold = 0.5

assert image_dir.is_dir(), f"图片目录不存在：{image_dir}"
paths = sorted(p for p in image_dir.rglob("*")
               if p.suffix.lower() in {".jpg", ".jpeg", ".png"})
assert paths, "目录中没有找到图片"
frame_metadata = {}
if manifest_path.is_file():
    manifest = json.loads(manifest_path.read_text())
    frame_metadata = {
        frame["image"]: frame
        for video in manifest["videos"] for frame in video["frames"]
    }

# 仅在某张图片没有预测 JSON 时加载模型；已有结果画图只需要 CPU。
model = None

def cpu_list(tensor):
    return tensor.detach().cpu().tolist()

with torch.inference_mode():
    for path in islice(paths, max_images):
        relative = path.relative_to(image_dir)
        # 保留子目录和原始扩展名，避免不同图像的同名结果相互覆盖。
        target = output_dir / relative.parent / (relative.name + ".json")
        filtered_target = filtered_output_dir / relative.parent / (relative.name + ".json")
        visualization_target = visualization_dir / relative.parent / (relative.name + ".png")
        image = np.asarray(Image.open(path).convert("RGB"), dtype=np.uint8)
        if target.exists():
            record = json.loads(target.read_text())
            assert record["image"] == relative.as_posix()
            assert record["image_hw"] == list(image.shape[:2])
            print("使用已有预测：", target, "类别：", record["class_names"])
        else:
            frame = frame_metadata.get(relative.as_posix(), {})
            selected_intrinsics_path = intrinsics_path or frame.get("intrinsics")
            intrinsics = None
            intrinsics_source = "default_placeholder"
            if selected_intrinsics_path is not None:
                intrinsics = np.load(selected_intrinsics_path).astype(np.float32)
                assert intrinsics.shape == (3, 3) and np.isfinite(intrinsics).all()
                if intrinsics_path is None and frame.get("image_hw") is not None:
                    assert frame["image_hw"] == list(image.shape[:2]), "图片尺寸与标定记录不一致"
                intrinsics_source = "provided" if intrinsics_path is not None else "extraction_manifest"
            if model is None:
                assert torch.cuda.is_available(), "当前环境无法访问 PPU"
                model = build_model(
                    checkpoint="/mnt/workspace/TEMP-FILE-STATION/wilddet3d_alldata_all_prompt_v1.0.pt",
                    lingbot_pretrained_model="/mnt/workspace/TEMP-FILE-STATION/model.pt",
                    skip_pretrained=True,
                    canonical_rotation=True,
                    score_threshold=0.3,
                    device="cuda",
                )
            data = preprocess(image.astype(np.float32), intrinsics)
            results = model(
                images=data["images"].cuda(),
                intrinsics=data["intrinsics"].cuda()[None],
                input_hw=[data["input_hw"]],
                original_hw=[data["original_hw"]],
                padding=[data["padding"]],
                input_texts=class_names,
            )
            boxes, boxes3d, scores, scores_2d, scores_3d, class_ids, depth_maps = results
            record = {
                "image": relative.as_posix(),
                "image_hw": list(image.shape[:2]),
                "class_names": class_names,
                "coordinate_system": "camera_opencv",
                "length_unit": "meter",
                "box3d_fields": ["cx", "cy", "cz", "W", "L", "H", "qw", "qx", "qy", "qz"],
                "intrinsics_source": intrinsics_source,
                "intrinsics_path": str(selected_intrinsics_path) if selected_intrinsics_path else None,
                "intrinsics_original": cpu_list(data["original_intrinsics"]),
                "boxes2d_xyxy": cpu_list(boxes[0]),
                "boxes3d": cpu_list(boxes3d[0]),
                "scores": cpu_list(scores[0]),
                "scores_2d": cpu_list(scores_2d[0]),
                "scores_3d": cpu_list(scores_3d[0]),
                "class_ids": cpu_list(class_ids[0]),
            }
            payload = json.dumps(record, ensure_ascii=False, indent=2, allow_nan=False)
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("x", encoding="utf-8") as stream:
                stream.write(payload)
            print("已保存预测：", target)

        # 显式分别判断两种分数；build_model 的 score_threshold 是综合分数阈值。
        keep = (
            (np.asarray(record["scores_2d"]) >= score_2d_threshold)
            & (np.asarray(record["scores_3d"]) >= score_3d_threshold)
        )
        filtered_record = dict(record)
        for key in ("boxes2d_xyxy", "boxes3d", "scores", "scores_2d", "scores_3d", "class_ids"):
            assert len(record[key]) == len(keep), f"预测字段长度不一致：{key}"
            filtered_record[key] = [value for value, retained in zip(record[key], keep) if retained]
        filtered_record["score_filter"] = {
            "score_2d_min": score_2d_threshold,
            "score_3d_min": score_3d_threshold,
            "condition": "scores_2d >= score_2d_min AND scores_3d >= score_3d_min",
        }
        filtered_record["source_prediction"] = str(target)
        filtered_target.parent.mkdir(parents=True, exist_ok=True)
        filtered_target.write_text(
            json.dumps(filtered_record, ensure_ascii=False, indent=2, allow_nan=False),
            encoding="utf-8",
        )

        # 在原图上投影：使用预测时保存的原图内参，不使用缩放补边后的内参。
        rendered = draw_3d_boxes(
            image=image,
            boxes3d=np.asarray(filtered_record["boxes3d"], dtype=np.float32).reshape(-1, 10),
            intrinsics=np.asarray(filtered_record["intrinsics_original"], dtype=np.float32),
            scores_2d=np.asarray(filtered_record["scores_2d"], dtype=np.float32),
            scores_3d=np.asarray(filtered_record["scores_3d"], dtype=np.float32),
            class_ids=np.asarray(filtered_record["class_ids"], dtype=np.int64),
            class_names=filtered_record["class_names"],
            draw_predicted_2d_boxes=False,
            score_2d_threshold=0.0,  # 已按上面的双阈值筛选，绘图不再额外筛选
            score_3d_threshold=0.0,
            line_width=3,
            font_size=20,
        )
        visible_count = len(filtered_record["boxes3d"])
        visualization_target.parent.mkdir(parents=True, exist_ok=True)
        rendered.save(visualization_target)
        print("已保存画框图片：", visualization_target,
              "预测目标数：", len(record["boxes3d"]), "满足画图阈值：", visible_count)
        print("已保存筛选后 JSON：", filtered_target)
PY
```

运行后，可在 VS Code 远程文件浏览器中直接打开 `wilddet3d_visualizations` 下的 PNG，彩色线框表示投影到图像上的 3D 包围框，标签显示类别及 2D／3D 分数。修改 `score_2d_threshold`、`score_3d_threshold` 可调整筛选标准；没有目标满足条件时仍保存原图，并在筛选后的 JSON 中保存空列表。这些预览图适合检查投影、漏检和误检，并不代表 3D 尺寸或朝向已通过验证。

**文本提示与设备：** 提示词由上面代码中的 `class_names` 定义，通过 `input_texts=class_names` 传入。它是可自行修改的开放词汇提示列表，不是固定类别白名单；识别效果仍取决于图像和模型能力。新推理通过 `device="cuda"` 和 `.cuda()` 在 PPU 镜像的兼容接口上运行；读取已有 JSON、筛选和画图则在 CPU 上进行。`SAM3_COMPILE=0` 只关闭编译优化，不会关闭 PPU 推理。可在另一个 DSW 终端运行 `ppu-smi` 查看实际设备内存和利用率。

当前源码 `wilddet3d/head/coder_3d.py` 的 3D 框排列为 **`[cx, cy, cz, W, L, H, qw, qx, qy, qz]`**，中心在相机坐标系中，长度单位为米，四元数为 `wxyz`；不要按子文档中不同的尺寸顺序读取。相机坐标使用 x 向右、y 向下、z 向前的约定；规范物体局部轴为 x 对应 L、y 对应 H、z 对应 W。转换到世界坐标、机器人坐标或其他标注格式时，需要真实外参和明确的轴约定，不能仅交换尺寸字段。

保存预测不等于完成准确标注。先人工检查代表性 ego 帧的漏检、误检、尺度和朝向，再扩展到全量数据；遮挡、运动模糊和视角差异会影响结果。若需要跨帧 ID、人工调整 3D 框、指定数据集格式或完整视频批处理，应另行确定需求并在修改代码前取得同意。

<a id="vscode-ssh"></a>

### VS Code SSH 与网页演示

VS Code SSH 既可以运行上面的命令行推理，也能转发网页端口。**当前网页环境存在需要先处理的依赖冲突：** [vis4d 1.0.0 发布元数据](https://pypi.org/pypi/vis4d/1.0.0/json)要求 `pydantic<2.0.0`；项目演示依赖清单要求 `pydantic>=2.0`，Gradio 5 也使用 Pydantic 2（参见 [Gradio 5.49.1 发布元数据](https://pypi.org/pypi/gradio/5.49.1/json)）。因此不能把根目录安装流程与演示依赖直接叠加，也不能声称当前环境已支持一键启动网页。

当前推荐先完成 Python 接口推理和 JSON 预标注。需要网页时，应在独立环境中评估 vis4d 的实际运行时依赖或前后端拆分方案；仅创建另一个虚拟环境不会自动解决上述冲突。不要通过忽略全部依赖、强制升级 Pydantic 或降到不匹配当前演示 API 的旧 Gradio 来掩盖问题。涉及依赖方案或代码改动时，先确认具体修改范围。

**以下为网页依赖兼容问题解决、导入与推理验证通过后的启动方式，并非当前已验证可执行的完整安装流程：**

第 5 步和 Python 推理示例通过新参数直接读取 LingBot 本地文件；现有 `demo/huggingface/app.py` 尚未传入该参数，网页仍使用默认的 LingBot 仓库／Hub 缓存来源。因此，下面的软链接仅解决网页的 WildDet3D 权重路径；网页还需准备 LingBot 的 Hub 缓存，或另行修改其模型构建调用以传入本地文件。

```bash
cd /mnt/workspace/WildDet3D

# 网页只查找 ckpt/wilddet3d.pt，否则会调用 HuggingFace 下载。
# 完成第 5 步的本地复制后，为网页建立指向本地副本的软链接。
# 若目标已存在，先检查它的路径，不要强制覆盖。
mkdir -p ckpt
ln -s /mnt/workspace/TEMP-FILE-STATION/wilddet3d_alldata_all_prompt_v1.0.pt ckpt/wilddet3d.pt

export SAM3_COMPILE=0
export HF_HOME=/mnt/workspace/.cache/wilddet3d-huggingface
export GRADIO_SERVER_PORT=7860
python demo/huggingface/app.py
```

服务启动后，在 VS Code 的“端口（Ports）”面板选择“转发端口”，输入 `7860`，然后在**本地电脑**浏览器打开 VS Code 显示的转发地址，通常为 `http://127.0.0.1:7860`。若本地端口被占用，以面板实际分配的端口为准。现有代码绑定 `0.0.0.0`，`share=False`；使用 SSH 转发不需要设置 `share=True` 或开放新的公网端口。

也可以在本地电脑终端使用已有 SSH 配置中的主机别名建立隧道：

```bash
# 将 your-dsw-host 替换为 VS Code 已经使用的 SSH 主机别名。
ssh -N -L 127.0.0.1:7860:127.0.0.1:7860 your-dsw-host
```

网页支持文本、框和点提示，可查看叠加图、深度图及鸟瞰视图。已知内参时勾选 `Use Actual Intrinsics`，填写 `fx`、`fy`、`cx`、`cy`；文本类别可输入 `person.chair.table`。当前页面中的类别附加控件被隐藏，也没有人工拖拽编辑 3D 框、批量任务管理及标准标注文件导出功能。网页适合抽样检查，保存预标注请使用前面的 Python 接口。

<a id="inference"></a>

## 推理

```python
from wilddet3d import build_model, preprocess
from wilddet3d.vis.visualize import draw_3d_boxes
import numpy as np
from PIL import Image

# 构建模型
model = build_model(
    checkpoint="/mnt/workspace/TEMP-FILE-STATION/wilddet3d_alldata_all_prompt_v1.0.pt",
    lingbot_pretrained_model="/mnt/workspace/TEMP-FILE-STATION/model.pt",
    score_threshold=0.3,
    skip_pretrained=True,
    # 仅在后续向 model(...) 传入 depth_gt=... 时开启，
    # 即预处理时使用了 depth= 参数。纯单目推理
    # 保持关闭。
    # use_depth_input_test=True,
)

# 读取并预处理图像
image = np.array(Image.open("image.jpg")).astype(np.float32)

# 已知相机内参
intrinsics = np.load("intrinsics.npy")  # (3, 3)
data = preprocess(image, intrinsics)

# 未知内参时使用默认值：focal=max(H,W)，主点位于图像中心
# data = preprocess(image)

# 如有激光雷达或双目等测得的深度图，传给同一预处理函数。
# 深度形状为 (H, W)，类型为 float32，单位为米，
# 分辨率须与原图一致。预处理会缩放并居中填充深度图，
# 使其与模型 input_hw 对齐（与评测时的变换一致）。
#   depth = np.load("depth.npy")  # (H, W)，float32，单位为米
#   data = preprocess(image, intrinsics, depth=depth)
# 省略 depth 或传入 None 时，模型使用 LingBot-Depth 的
# 单目预测。提供深度时，以下每次 model(...) 调用还须传入
# depth_gt=data["depth_gt"].cuda()。

# 文本提示：检测指定类别的全部实例
results = model(
    images=data["images"].cuda(),
    intrinsics=data["intrinsics"].cuda()[None],
    input_hw=[data["input_hw"]],
    original_hw=[data["original_hw"]],
    padding=[data["padding"]],
    input_texts=["car", "person", "bicycle"],
    # depth_gt=data["depth_gt"].cuda(),  # 仅在 preprocess 使用了 depth=... 时传入
)
boxes, boxes3d, scores, scores_2d, scores_3d, class_ids, depth_maps = results

# 几何框提示：将 2D 框提升为 3D 框（一对一）
results = model(
    images=data["images"].cuda(),
    intrinsics=data["intrinsics"].cuda()[None],
    input_hw=[data["input_hw"]],
    original_hw=[data["original_hw"]],
    padding=[data["padding"]],
    input_boxes=[[100, 200, 300, 400]],  # 原图像素坐标 xyxy
    prompt_text="geometric",
    # depth_gt=data["depth_gt"].cuda(),  # 仅在 preprocess 使用了 depth=... 时传入
)

# 示例提示：以 2D 框作为视觉样例，查找所有相似对象（一对多）
results = model(
    images=data["images"].cuda(),
    intrinsics=data["intrinsics"].cuda()[None],
    input_hw=[data["input_hw"]],
    original_hw=[data["original_hw"]],
    padding=[data["padding"]],
    input_boxes=[[100, 200, 300, 400]],
    prompt_text="visual",
    # depth_gt=data["depth_gt"].cuda(),  # 仅在 preprocess 使用了 depth=... 时传入
)

# 点提示
results = model(
    images=data["images"].cuda(),
    intrinsics=data["intrinsics"].cuda()[None],
    input_hw=[data["input_hw"]],
    original_hw=[data["original_hw"]],
    padding=[data["padding"]],
    input_points=[[(150, 250, 1), (200, 300, 0)]],  # (x, y, label)：1 为正样本点，0 为负样本点
    prompt_text="geometric",
    # depth_gt=data["depth_gt"].cuda(),  # 仅在 preprocess 使用了 depth=... 时传入
)

# 可视化结果
boxes, boxes3d, scores, scores_2d, scores_3d, class_ids, depth_maps = results
draw_3d_boxes(
    image=image.astype(np.uint8),
    boxes3d=boxes3d[0],
    intrinsics=intrinsics,
    scores_2d=scores_2d[0],
    scores_3d=scores_3d[0],
    class_ids=class_ids[0],
    class_names=["car", "person", "bicycle"],
    save_path="output.png",
    # 可选调试叠加层（默认均关闭）：
    #   预测 2D 框（绿色）：
    # boxes_2d=boxes[0],
    # draw_predicted_2d_boxes=True,
    #   用户提示框（红色）／提示点（正样本红色，负样本灰色）：
    # input_boxes=[[100, 200, 300, 400]],
    # input_points=[[(150, 250, 1)]],
    # draw_prompt=True,
)
```

**说明：**

- 未提供 `intrinsics` 时，使用默认内参矩阵（`focal=max(H,W)`，主点位于图像中心）。这不是相机标定结果；`use_predicted_intrinsics` 默认关闭，不能将默认内参与模型预测内参混为一谈。
- 可选深度输入：传入 `depth_gt=depth_tensor`（形状 `(B, 1, H, W)`，单位为米），利用稀疏或稠密深度（如激光雷达）改善 3D 定位；同时需要在构建模型时开启 `use_depth_input_test=True`。

完整 API 说明见 **[docs/INFERENCE.md](docs/INFERENCE.md)**。子文档尚未同步本次翻译；内参默认行为、尺寸排列等以当前源码及本页说明为准。

<a id="faster-inference"></a>

### 加速推理（BF16 自动混合精度与 `torch.compile`）

`optimize_for_inference()` 使用 `torch.autocast` 包装预测器，并可选用 `torch.compile`。原项目在 H100 80GB 上测得相对 FP32 即时执行约 **3.0 倍加速**，检测输出与 FP32 的余弦相似度保留四位小数为 1.0000。这些结果来自 NVIDIA 环境，不代表 PPU 的兼容性或性能；PPU 首次验证保持 FP32 且不启用编译。

```python
from wilddet3d import build_model, optimize_for_inference, preprocess

model = build_model(
    checkpoint="/mnt/workspace/TEMP-FILE-STATION/wilddet3d_alldata_all_prompt_v1.0.pt",
    lingbot_pretrained_model="/mnt/workspace/TEMP-FILE-STATION/model.pt",
    skip_pretrained=True,
)

# BF16 自动混合精度 + torch.compile（默认 max-autotune-no-cudagraphs，原测试约 3 倍加速）
model = optimize_for_inference(model)
# 等价于：
# model = optimize_for_inference(model, dtype="bf16", compile_mode="max-autotune-no-cudagraphs")

# 首次调用触发编译（原测试中 max-autotune 约 17 分钟，default 约 2 分钟）。
# 后续调用复用 Inductor 缓存。
# 使用前面推理示例中同样的输入参数调用优化后的 model。
```

**延迟**（1008×1008 输入、文本提示、H100 80GB）：

| 配置 | 延迟中位数 | 加速比 | 相对 FP32（余弦相似度／相对 L2 误差） |
|---|---|---|---|
| FP32 即时执行（基线） | 219 ms | 1.00x | — |
| BF16 自动混合精度 | 132 ms | **1.66x** | 1.0000 / 5e-4 |
| BF16 自动混合精度 + `torch.compile("default")` | 83 ms | **2.64x** | 1.0000 / 7e-4 |
| BF16 自动混合精度 + `torch.compile("max-autotune-no-cudagraphs")` **（默认）** | 73 ms | **3.01x** | 1.0000 / 7e-4 |

**说明：**

- 对 Ampere 及更新的 NVIDIA 架构（A100／H100／RTX 30xx+），原项目推荐 `dtype="bf16"`。自动混合精度按算子策略保留部分敏感运算的 FP32 精度；表中结果显示数值接近，但不应理解为逐位相同，也不能直接外推到 PPU。
- `compile_mode="max-autotune-no-cudagraphs"` 为默认模式，在原项目测试中端到端速度最快。首次编译约 17 分钟，后续可复用 Inductor 缓存。
- `compile_mode="default"` 在原项目测试中提供约 2.6 倍加速，首次编译约 2 分钟，适合频繁迭代。
- **不支持** `compile_mode="reduce-overhead"` / `"max-autotune"` 等启用 CUDA 图的模式：检测头中的 NMS 和规范旋转掩码会产生动态形状。
- 可用 `python scripts/benchmark_inference.py` 复现上述测试。

<a id="evaluation"></a>

## 评测

以下为原项目基准评测流程，给自有 ego 数据生成预标注时无需执行。PPU 上的评测尚未验证。

### WildDet3D-Bench

从 [allenai/WildDet3D-Data](https://huggingface.co/datasets/allenai/WildDet3D-Data) 下载评测数据，将 `InTheWild_v3_val.json` 放到评测配置要求的 `data/in_the_wild/annotations/`。使用 [vis4d](https://github.com/SysCV/vis4d) 框架评测：

WildDet3D 使用的第三方图像数据仅供个人／学术用途，不得重新分发！[下载地址](https://huggingface.co/collections/weikaih/wilddet3d-images)。



```bash
# 设置 PYTHONPATH，使 configs/ 可被导入
export PYTHONPATH=$(pwd):$PYTHONPATH

# 文本提示
vis4d test --config configs/eval/in_the_wild/text.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt

# 文本提示 + 真实深度
vis4d test --config configs/eval/in_the_wild/text_with_depth.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt

# 框提示（使用真实 2D 框）
vis4d test --config configs/eval/in_the_wild/box_prompt.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt

# 框提示 + 真实深度
vis4d test --config configs/eval/in_the_wild/box_prompt_with_depth.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt
```

| 模式 | 配置 |
|---|---|
| 文本提示 | `configs/eval/in_the_wild/text.py` |
| 文本提示 + 深度 | `configs/eval/in_the_wild/text_with_depth.py` |
| 框提示 | `configs/eval/in_the_wild/box_prompt.py` |
| 框提示 + 深度 | `configs/eval/in_the_wild/box_prompt_with_depth.py` |

### WildDet3D-Stereo4D-Bench

从 [allenai/WildDet3D-Stereo4D-Bench-Images](https://huggingface.co/datasets/allenai/WildDet3D-Stereo4D-Bench-Images) 下载评测数据，将 `Stereo4D_val.json` / `Stereo4D_test.json` 放到 `data/in_the_wild/annotations/`。评测包含 383 张具有真实双目深度的图像：

```bash
# 设置 PYTHONPATH，使 configs/ 可被导入
export PYTHONPATH=$(pwd):$PYTHONPATH

# 文本提示
vis4d test --config configs/eval/stereo4d/text.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt

# 文本提示 + 真实深度
vis4d test --config configs/eval/stereo4d/text_with_depth.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt

# 框提示（使用真实 2D 框）
vis4d test --config configs/eval/stereo4d/box_prompt.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt

# 框提示 + 真实深度
vis4d test --config configs/eval/stereo4d/box_prompt_with_depth.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt
```

| 模式 | 配置 |
|---|---|
| 文本提示 | `configs/eval/stereo4d/text.py` |
| 文本提示 + 深度 | `configs/eval/stereo4d/text_with_depth.py` |
| 框提示 | `configs/eval/stereo4d/box_prompt.py` |
| 框提示 + 深度 | `configs/eval/stereo4d/box_prompt_with_depth.py` |

<a id="other-benchmarks"></a>

### Omni3D 域内评测与 Argoverse 2／ScanNet 零样本评测

Omni3D 是主要训练分布；Argoverse 2 和 ScanNet 不参与训练，用于零样本评测。评测协议（数据集、划分、ODS 指标以及基础／新类别划分）遵循 **3D-MOOD**（[cvg/3D-MOOD](https://github.com/cvg/3D-MOOD)），因此可以直接对比其报告的结果。每个基准都有四种配置：`text`、`text_with_depth`、`box_prompt`、`box_prompt_with_depth`。

```bash
export PYTHONPATH=$(pwd):$PYTHONPATH

# Omni3D：报告各子数据集的 AP（KITTI / nuScenes / SUNRGBD /
# Hypersim / ARKitScenes / Objectron），以及宏平均 AP_3D。
vis4d test --config configs/eval/omni3d/text.py             --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt
vis4d test --config configs/eval/omni3d/text_with_depth.py  --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt
vis4d test --config configs/eval/omni3d/box_prompt.py       --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt
vis4d test --config configs/eval/omni3d/box_prompt_with_depth.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt

# ScanNet（零样本）：报告 AP / mATE / mASE / mAOE / ODS，
# 18 个室内类别划分为基础／新类别，其中 15 个常见室内类别
# 作为基础类别。
vis4d test --config configs/eval/scannet/text.py            --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt
vis4d test --config configs/eval/scannet/text_with_depth.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt
vis4d test --config configs/eval/scannet/box_prompt.py      --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt
vis4d test --config configs/eval/scannet/box_prompt_with_depth.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt

# Argoverse 2（零样本）：报告同一组指标，
# 基础类别为 AV2 中 11 个常见驾驶类别。
vis4d test --config configs/eval/argoverse/text.py            --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt
vis4d test --config configs/eval/argoverse/text_with_depth.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt
vis4d test --config configs/eval/argoverse/box_prompt.py      --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt
vis4d test --config configs/eval/argoverse/box_prompt_with_depth.py --gpus 1 --ckpt ckpt/wilddet3d_alldata_all_prompt_v1.0.pt
```

指标定义、数据准备以及各基准的配置表见 **[docs/EVALUATION.md](docs/EVALUATION.md)**。

<a id="training"></a>

## 训练

WildDet3D 分为三个训练阶段，每个阶段都使用 `vis4d fit`。本节保留原项目训练说明；当前 PPU 适配目标仅为推理，以下多卡训练流程未在本实例验证，也无需为预标注执行：

```bash
# 设置 PYTHONPATH，使 configs/ 可被导入
export PYTHONPATH=$(pwd):$PYTHONPATH

# 阶段 1（12 轮）：Omni3D 规范旋转预训练
vis4d fit --config configs/training/stage1_omni3d.py --gpus 8

# 阶段 2（12 轮）：全量数据密集微调（Omni3D + CA1M + Waymo + 3EED + FoundationPose + ITW-human + V3Det-human），采用五模式批次整理器（不含掩码）
vis4d fit --config configs/training/stage2_alldata.py --gpus 8

# 阶段 3（3 轮）：使用高质量人工核验数据，混合框／点／文本提示微调
vis4d fit --config configs/training/stage3_mix_box_point_text_ft.py --gpus 8
```

多节点训练增加 `--num_nodes N`。默认每张 GPU 的批量为 4；每节点 8 张 GPU、共 4 个节点时，全局批量为 128。

<a id="training-data-preparation"></a>

### 训练数据准备

各数据集的下载、转换及 HDF5 打包步骤见 **[docs/TRAINING_DATA.md](docs/TRAINING_DATA.md)**，包括 Omni3D、CA1M、Waymo v2、3EED、FoundationPose、ITW、Stereo4D、掩码标注及预训练权重。`scripts/data_prep/` 下的抽帧脚本具有确定性，按原文流程可复现相同的训练／验证划分。

WildDet3D 使用的第三方图像数据仅供个人／学术用途，不得重新分发！[下载地址](https://huggingface.co/collections/weikaih/wilddet3d-images)。

<a id="results"></a>

## 实验结果

<a id="wilddet3d-bench-in-the-wild"></a>

### WildDet3D-Bench（真实场景）

AP 使用中心距离匹配计算。AP_r、AP_c、AP_f 分别表示稀有（<5）、常见（5–20）和高频（>20）类别划分的结果。

| 方法 | 数据 | AP_r | AP_c | AP_f | AP |
|---|---|---|---|---|---|
| **文本提示** | | | | | |
| 3D-MOOD | Omni3D | 2.4 | 2.1 | 2.6 | 2.3 |
| WildDet3D | Omni3D | 9.0 | 6.5 | 5.2 | 6.8 |
| WildDet3D + 深度 | Omni3D | 23.0 | 21.5 | 16.1 | 20.7 |
| WildDet3D | Omni3D, 其他数据, WildDet3D-Data | 28.3 | 21.6 | 18.7 | 22.6 |
| WildDet3D + 深度 | Omni3D, 其他数据, WildDet3D-Data | **47.4** | **40.7** | **37.2** | **41.6** |
| **框提示** | | | | | |
| OVMono3D-LIFT | Omni3D | 7.4 | 8.8 | 5.1 | 7.7 |
| DetAny3D | Omni3D, 其他数据 | 9.9 | 7.4 | 6.3 | 7.8 |
| WildDet3D | Omni3D | 12.0 | 7.9 | 5.3 | 8.4 |
| WildDet3D + 深度 | Omni3D | 26.4 | 24.4 | 19.6 | 23.9 |
| WildDet3D | Omni3D, 其他数据, WildDet3D-Data | 30.0 | 24.2 | 20.3 | 24.8 |
| WildDet3D + 深度 | Omni3D, 其他数据, WildDet3D-Data | **53.7** | **46.1** | **42.5** | **47.2** |

### Omni3D

AP 在 3D IoU [0.5:0.95] 上计算。

| 方法 | KITTI | nuScenes | SUNRGBD | Hypersim | ARKitScenes | Objectron | AP |
|---|---|---|---|---|---|---|---|
| **文本提示** | | | | | | | |
| Cube R-CNN | 32.6 | 30.1 | 15.3 | 7.5 | 41.7 | 50.8 | 23.3 |
| 3D-MOOD Swin-T | 32.8 | 31.5 | 21.9 | 10.5 | 51.0 | 64.3 | 28.4 |
| 3D-MOOD Swin-B | 31.4 | 35.8 | 23.8 | 9.1 | 53.9 | 67.9 | 30.0 |
| WildDet3D | **37.0** | 31.7 | 38.9 | 16.5 | 64.6 | 60.5 | 34.2 |
| WildDet3D + 深度 | 36.1 | 32.0 | **51.1** | **26.6** | **73.3** | **68.3** | **41.6** |
| **框提示** | | | | | | | |
| OVMono3D-LIFT | 31.4 | 32.5 | 23.2 | 11.9 | 54.2 | 63.5 | 29.6 |
| DetAny3D | 38.7 | **37.6** | 46.1 | 16.0 | 50.6 | 56.8 | 34.4 |
| WildDet3D | **44.3** | 35.3 | 43.1 | 17.3 | 66.6 | 60.8 | 36.4 |
| WildDet3D + 深度 | 42.8 | 35.9 | **58.7** | **30.4** | **76.6** | **68.5** | **45.8** |

<a id="zero-shot-transfer-argoverse-2--scannet"></a>

### 零样本迁移（Argoverse 2 + ScanNet）

仅使用 Omni3D + In-the-Wild 训练，在 Argoverse 2（室外驾驶，26 类）和 ScanNet（室内，18 类）上进行零样本评测。数据划分、ODS 指标及基础／新类别分组均遵循 [3D-MOOD](https://github.com/cvg/3D-MOOD)，因此可以直接比较下表与其基线结果。

采用规范旋转的 AOE 约定，ODS = (3·AP + (1 - mATE) + (1 - mASE) + (1 - mAOE)) / 6。AP、ODS 越高越好；mATE、mASE、mAOE 越低越好。

| 方法 | Argoverse2 AP | mATE | mASE | mAOE | ODS | ScanNet AP | mATE | mASE | mAOE | ODS |
|---|---|---|---|---|---|---|---|---|---|---|
| Cube R-CNN | 8.6 | 0.903 | 0.867 | 0.953 | 8.9 | 20.0 | 0.733 | 0.774 | 0.921 | 19.5 |
| 3D-MOOD Swin-T | 14.8 | 0.782 | 0.697 | 0.612 | 22.5 | 27.3 | 0.630 | 0.726 | 0.650 | 30.2 |
| 3D-MOOD Swin-B | 14.7 | 0.755 | 0.680 | 0.580 | 23.8 | 28.8 | 0.612 | **0.706** | 0.655 | 31.5 |
| WildDet3D | 43.4 | 0.714 | 0.645 | 0.526 | 40.3 | 56.5 | 0.601 | 0.720 | 0.437 | 48.9 |
| WildDet3D + 深度 | **43.4** | **0.701** | **0.645** | **0.526** | **40.4** | **57.6** | **0.589** | 0.707 | **0.422** | **50.2** |

真实深度对 ScanNet 有明显帮助（ODS 提升 1.3），室内场景受益于具有真实尺度的深度。Argoverse 2 上的提升较小，表明单目深度头在室外驾驶场景中已具备较好的尺度校准。

<a id="qualitative-results"></a>

### 可视化结果

**框提示效果对比**（WildDet3D、OVMono3D 与 DetAny3D）：
<p align="center">
  <img src="assets/qualitative_box_prompt.jpg" width="100%" />
</p>

**文本提示效果对比**：
<p align="center">
  <img src="assets/qualitative_text_prompt.jpg" width="100%" />
</p>

<a id="wilddet3d-data"></a>

## WildDet3D 数据集

**WildDet3D-Data** 是面向真实场景单目 3D 检测的大规模数据集，包含经过人工核验的 3D 包围框标注，图像来自 COCO、LVIS、Objects365 和 V3Det。

| 划分 | 说明 | 图像数 | 标注数 | 类别数 |
|---|---|---|---|---|
| 验证集 | 人工标注验证集 | 2,470 | 9,256 | 785 |
| 测试集 | 人工标注测试集 | 2,433 | 5,596 | 633 |
| 训练集（人工） | 仅人工核验标注 | 102,979 | 229,934 | 11,879 |
| 训练集（精选） | 人工标注 + 通过 VLM 筛选的小目标 | 102,979 | 412,711 | 12,064 |
| 训练集（合成） | VLM 自动筛选 | 896,004 | 3,483,292 | 11,896 |
| **合计** | | **1,003,886** | **3,910,855** | **13,499** |

数据集托管于 HuggingFace：[allenai/WildDet3D-Data](https://huggingface.co/datasets/allenai/WildDet3D-Data)。下载说明与数据格式见[数据集说明](https://huggingface.co/datasets/allenai/WildDet3D-Data)。

<a id="citation"></a>

## 引用

如果本项目对你的工作有所帮助，请引用以下文献（保留原始 BibTeX 信息）：

```bibtex
@misc{huang2026wilddet3dscalingpromptable3d,
      title={WildDet3D: Scaling Promptable 3D Detection in the Wild}, 
      author={Weikai Huang and Jieyu Zhang and Sijun Li and Taoyang Jia and Jiafei Duan and Yunqian Cheng and Jaemin Cho and Matthew Wallingford and Rustin Soraki and Chris Dongjoo Kim and Shuo Liu and Donovan Clay and Taira Anderson and Winson Han and Ali Farhadi and Bharath Hariharan and Zhongzheng Ren and Ranjay Krishna},
      year={2026},
      eprint={2604.08626},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2604.08626}, 
}
```

<a id="acknowledgements"></a>

## 致谢

- [Omni3D](https://github.com/facebookresearch/omni3d) —— 3D 检测基准与基线
- [vis4d](https://github.com/SysCV/vis4d) —— 训练与评测框架
- [SAM 3](https://github.com/facebookresearch/sam3) —— 通用分割模型 SAM 3
- [LingBot-Depth](https://github.com/Robbyant/lingbot-depth) —— 单目深度估计
- [3D-MOOD](https://github.com/cvg/3D-MOOD) —— 开放词汇单目 3D 检测
- [DetAny3D](https://github.com/OpenDriveLab/DetAny3D) —— 通用 3D 目标检测
- [OVMono3D](https://github.com/UVA-Computer-Vision-Lab/ovmono3d) —— 开放词汇单目 3D 检测
- [LabelAny3D](https://github.com/UVA-Computer-Vision-Lab/LabelAny3D) —— 3D 包围框标注工具

<a id="license"></a>

## 许可证

**代码：** 本代码库包含 [SAM 3](https://github.com/facebookresearch/sam3) 的代码，采用 [SAM 许可证](https://github.com/facebookresearch/sam3/blob/main/LICENSE)，面向研究和教育用途，使用时应遵守 [Ai2 负责任使用指南](https://allenai.org/responsible-use)。

**模型：** 本模型基于 [SAM 3](https://github.com/facebookresearch/sam3) 和 [LingBot-Depth](https://github.com/Robbyant/lingbot-depth)，采用 [SAM 许可证](https://github.com/facebookresearch/sam3/blob/main/LICENSE)，面向研究和教育用途，使用时应遵守 [Ai2 负责任使用指南](https://allenai.org/responsible-use)。
