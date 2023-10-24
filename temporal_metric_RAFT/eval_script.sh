#!/bin/bash

MODEL=models/raft-sintel.pth
SCENE_PATH=../results/nerf_synthetic/chair/
# estimate optical flow and compute occlusion map
# for ground-truth/original sequence
CUDA_VISIBLE_DEVICES=0 python compute_flow_occlusion.py \
--model ${MODEL} \
--mixed_precision \
--data_dir ${SCENE_PATH}/test_path \
--out_dir ${SCENE_PATH}/optical_flow 

# compute warp error and LPIPS error:

CUDA_VISIBLE_DEVICES=0 python evaluate_temporal_consistency.py \
--data_dir ${SCENE_PATH}/stylized_path \
--flow_dir ${SCENE_PATH}/optical_flow 
```
