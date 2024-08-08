# nuScenes dataset

## 1.Prepare data
```shell
mkdir data
cd data
ln -s path-to-nuscenes ./
```

## 2. Generate 2D masks (frustum prior)
```shell
# Box
python  tools/frustum_generate/generate_box.py --config projects/configs/nuimages/htc_x101_64x4d_fpn_dconv_c3-c5_coco-20e_16x1_20e_nuim.py --checkpoint ckpts/htc_x101_64x4d_fpn_dconv_c3-c5_coco-20e_16x1_20e_nuim_20201008_211222-0b16ac4b.pth
# Mask
python tools/frustum_generate/generate_mask.py --config projects/configs/nuimages/htc_x101_64x4d_fpn_dconv_c3-c5_coco-20e_16x1_20e_nuim.py  --checkpoint ckpts/htc_x101_64x4d_fpn_dconv_c3-c5_coco-20e_16x1_20e_nuim_20201008_211222-0b16ac4b.pth
```
    