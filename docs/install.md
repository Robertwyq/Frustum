# Step-by-step installation instructions

**a. Create a conda virtual environment and activate it.**
```shell
conda create -n frustum python=3.8 -y
conda activate frustum
```

**b. Install PyTorch and torchvision following the [official instructions](https://pytorch.org/).**
```shell
pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html

```
**c. Install mmcv series**
```shell
pip install mmcv-full==1.4.0 -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.9.0/index.html
pip install mmdet==2.14.0
pip install mmsegmentation==0.14.1

# install mmdetection3d
cd mmdetection3d
pip install -v -e .
```
