import mmcv
from mmcv import Config
from mmdet3d.models import build_model
from mmcv.runner import (get_dist_info, init_dist, load_checkpoint,
                         wrap_fp16_model)
from mmdet.apis import inference_detector, init_detector, show_result_pyplot
import glob
import os
from PIL import Image
import numpy as np
from tqdm import tqdm
import argparse
import cv2

def box2mask(result, score_thresh):
    mask = np.zeros((900, 1600)).astype(np.int8)
    for i in range(10):
        if len(result[0][i]) > 0:
            for j in range(len(result[0][i])):
                if result[0][i][j][-1] > score_thresh:
                    x1 = [int(result[0][i][j][0]), int(result[0][i][j][1])]
                    x2 = [int(result[0][i][j][2]), int(result[0][i][j][1])]
                    x3 = [int(result[0][i][j][2]), int(result[0][i][j][3])]
                    x4 = [int(result[0][i][j][0]), int(result[0][i][j][3])]
                    coord = np.array([[x1, x2, x3, x4]])
                    mask = cv2.fillPoly(mask, coord, 1)
    return mask

def process_camera_images(camera_type, model, img_files, output_cam_dir, score_thresh):
    for idx in tqdm(range(len(img_files)), desc=f'Processing {camera_type}'):
        img = img_files[idx]
        result = inference_detector(model, img)
        mask = box2mask(result, score_thresh)

        png = Image.fromarray((mask * 255).astype('uint8'))
        name = os.path.splitext(os.path.basename(img))[0] + '.png'
        save_path = os.path.join(output_cam_dir, name)
        png.save(save_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--devices', type=str, default='cuda:0')
    parser.add_argument('--threshold', type=float, default=0.1)
    parser.add_argument('--config', type=str, required=True, help='Path to config file')
    parser.add_argument('--checkpoint', type=str, required=True, help='Path to checkpoint file')
    args = parser.parse_args()

    score_thresh = args.threshold

    root = './data/nuscenes/samples'
    output_dir = './data/nuscenes/nuscenes_box_{:.2f}'.format(score_thresh)
    os.makedirs(output_dir, exist_ok=True)

    # Define camera types
    camera_types = ['CAM_FRONT', 'CAM_FRONT_RIGHT', 'CAM_FRONT_LEFT', 'CAM_BACK', 'CAM_BACK_RIGHT', 'CAM_BACK_LEFT']

    # Model configuration
    model = init_detector(args.config, args.checkpoint, device=args.devices)

    # Process images for each camera type
    for camera_type in camera_types:
        img_files = glob.glob(os.path.join(root, camera_type, '*.jpg'))
        output_cam_dir = os.path.join(output_dir, camera_type)
        os.makedirs(output_cam_dir, exist_ok=True)
        process_camera_images(camera_type, model, img_files, output_cam_dir, score_thresh)

if __name__ == "__main__":
    main()