# <center>FrustumFormer<center>
> [CVPR 2023] [**FrustumFormer: Adaptive Instance-aware Resampling for Multi-view 3D Detection**](https://arxiv.org/pdf/2301.04467.pdf).

> Authors: Yuqi Wang, Yuntao Chen, Zhaoxiang Zhang

> [Video](https://www.bilibili.com/video/BV1mM4y1i7vd/), [Paper](https://arxiv.org/pdf/2301.04467.pdf)

<div align="center">
<img src="figs/frustum.png" alt="alt text" width="80%">
</div>

# News
- **[2023/3/26]** We release the camera ready version.
- **[2023/2/28]** *FrustumFormer* was accepted by CVPR 2023.

# Catalog
- [x] Initialization

# Getting Started
- [Installation](docs/install.md) 
- [Dataset](docs/prepare_data.md)

# Model Zoo
### NuScenes Val
| Backbone | Method | Epoch | Img |  mAP| NDS |memroy | Config | Download |
| :---: | :---: | :---: | :---: | :---:|:---:| :---: | :---: |:---: |
| R101-DCN | FrustumFormer | 24 | 640*1600 |0.472 |0.553 | 40G | [Frustum_r101](./projects/configs/frustumformer/val/temporal/frustumformer_r101.py) |  |

### NuScenes Test
| Backbone | Method | Epoch | Img |  mAP| NDS|memroy | Config | Download |
| :---: | :---: | :---: | :---: | :---:|:---:| :---: | :---: |:---: |
| VoV99 | FrustumFormer | 24 | 640*1600 | 0.530 | 0.595 | 40G | [Frustum_vov99](./projects/configs/frustumformer/test/frustumformer_vov99.py)

# Bibtex
If this work is helpful for your research, please consider citing the following BibTeX entry.

```
@inproceedings{wang2023frustumformer,
  title={FrustumFormer: Adaptive Instance-aware Resampling for Multi-view 3D Detection},
  author={Wang, Yuqi and Chen, Yuntao and Zhang, Zhaoxiang},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={5096--5105},
  year={2023}
}
```

# Acknowledgement 
Many thanks to the following open-source projects:
* [mmdetection3d](https://github.com/open-mmlab/mmdetection3d)
* [BEVFormer](https://github.com/fundamentalvision/BEVFormer)