Tested in pytorch 1.6.0 Cuda 10.2, GTX2080Ti (11GB), Ubuntu 20.04
1. Copy repository:
```
git clone https://github.com/princeton-vl/RAFT
scp compute_flow_occlusion.py RAFT/
scp evaluate_temporal_consistency.py RAFT/
```
2. Requirements:
- follow official installation in https://github.com/princeton-vl/RAFT
- pip install lpips

3. evaluate pipeline:
- estimate optical flow and compute occlusion map for ground-truth/original sequence. E.g,
```
CUDA_VISIBLE_DEVICES=0 python compute_flow_occlusion.py \
--model models/raft-sintel.pth \
--mixed_precision \
--data_dir ../results/nerf_synthetic/chair/test_path \
--out_dir ../results/nerf_synthetic/chair/optical_flow 
```
- compute warp error and LPIPS error:
```
CUDA_VISIBLE_DEVICES=0 python evaluate_temporal_consistency.py \
--data_dir ../results/nerf_synthetic/chair/stylized_path \
--flow_dir ../results/nerf_synthetic/chair/optical_flow 
```
