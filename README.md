# <p align='center'>`Advances in 3D Neural Stylization`</p>

## Contributing

If you think I have missed out on something (or) have any suggestions (papers, implementations and other resources), feel free to [pull a request](https://github.com/chenyingshu/advances_3d_neural_stylization/pulls)

Feedback and contributions are welcome!

markdown format:
``` markdown
**Here is the Paper Name.**<br>
*[Author 1](homepage), Author 2, and Author 3.*<br>
Conference or Journal Year. <br>
[[Paper](link)] [[Project](link)] [[Github](link)] [[Video](link)] [[Data](link)]
```

## Table of Contents
- [Mesh Stylization](#mesh-stylization)
- [Volumetric Stylization](#volumetric-stylization)
- [Novel View Stylization](#novel-view-stylization)
- [2D Baselines](#)
- [Evaluation Datasets](#)
## Overview ##
|  Abbr.  |  Title   | Book  | Paper  | Project  | Github  |
|  ----  |  ----    | ----  |----   |----  |----  |
|  |**Mesh Stylization**  | || |  |
|  Neural Renderer | Neural 3D Mesh Renderer |CVPR 2018|[[Paper](https://arxiv.org/abs/1711.07566)]|[[Project](https://hiroharu-kato.com/assets/downloads/cvpr_2018_poster.pdf)] | [[Github](https://github.com/hiroharu-kato/style_transfer_3d)] |
| 3DStyleNet | 3DStyleNet: Creating 3D Shapes with Geometric and Texture Style | ICCV 2021| [[Paper](https://research.nvidia.com/labs/toronto-ai/3DStyleNet/assets/3dstyle-paper.pdf)] | [[Project](https://research.nvidia.com/labs/toronto-ai/3DStyleNet/)] |  |
|  StyleMesh  | StyleMesh: Style Transfer for Indoor 3D Scene Reconstructions   | CVPR 2022 |  [[Paper](https://arxiv.org/abs/2112.01530)]  |  [[Project](https://lukashoel.github.io/stylemesh/)]  | [[Github](https://github.com/lukasHoel/stylemesh)]   | 
| Creative Birds | Creative Birds: Self-Supervised Single-View 3D Style Transfer | ICCV 2023 | [[Paper](https://arxiv.org/abs/2307.14127)] | | [[Github](https://github.com/wrk226/creative_birds)] |
| Text2Mesh |Text2Mesh: Text-Driven Neural Stylization for Meshes  |CVPR 2022|[[Paper](https://arxiv.org/abs/2112.03221)]| [[Project](https://threedle.github.io/text2mesh/)] | [[Github](https://github.com/threedle/text2mesh)]  |
| X-Mesh | X-Mesh:Towards Fast and Accurate Text-driven 3D Stylization via Dynamic Textual Guidance | ICCV 2023 | [[Paper](https://arxiv.org/abs/2303.15764)] | [[Project](https://xmu-xiaoma666.github.io/Projects/X-Mesh/)] | [[Github](https://github.com/xmu-xiaoma666/X-Mesh)] |
|  |**Volumetric Stylization**  | || |  |
| VolumeNST | Efficient Neural Style Transfer For Volumetric Simulations | ACM SIGGRAPH Asia, 2022|  [[Paper](https://studios.disneyresearch.com/app/uploads/2022/10/Efficient-Neural-Style-Transfer-For-Volumetric-Simulations.pdf)]| [[Project](https://studios.disneyresearch.com/2022/11/30/efficient-neural-style-transfer-for-volumetric-simulations/)] |  |
|  | **Novel View Stylization** | || |  |
|  LSNV  | Learning to stylize novel views |  ICCV 2021  | [[Paper](https://arxiv.org/abs/2105.13509)]   | [[Project](https://hhsinping.github.io/3d_scene_stylization/)]   |  [[Github](https://github.com/hhsinping/stylescene)] |
| HyperStyle | Stylizing 3D Scene via Implicit Representation and HyperNetwork |WACV 2022 | [[Paper](https://arxiv.org/abs/2105.13016)] |  [[Project](https://ztex08010518.github.io/3dstyletransfer/)] | [[Github](https://github.com/ztex08010518/Stylizing-3D-Scene)] |
| StylizedNeRF | StylizedNeRF: Consistent 3D Scene Stylization as Stylized NeRF via 2D-3D Mutual Learning | CVPR 2022|[[Paper](https://arxiv.org/abs/2205.12183)]| [[Project](http://geometrylearning.com/StylizedNeRF/)]| [[Github](https://github.com/IGLICT/StylizedNeRF)] |
|3D Photo Stylization | 3D Photo Stylization: Learning to Generate Stylized Novel Views from a Single Image | CVPR 2022|[[Paper](https://arxiv.org/abs/2112.00169)]|[[Project](https://pages.cs.wisc.edu/~fmu/style3d/)]  | [[Github](https://github.com/fmu2/3d_photo_stylization)]  |
| ARF |ARF: Artistic Radiance Fields  | ECCV 2022|[[Paper](https://arxiv.org/abs/2206.06360)]|[[Project](https://www.cs.cornell.edu/projects/arf/)] | [[Github](https://github.com/Kai-46/ARF-svox2)] |
| UINS | Unified Implicit Neural Stylization |ECCV 2022 |[[Paper](https://arxiv.org/abs/2204.01943)]|[[Project](https://zhiwenfan.github.io/INS/)]  | [[Github](https://github.com/VITA-Group/INS)] |
| INS | Instant Neural Radiance Fields Stylization | ArXiv 2023 |[[Paper](https://arxiv.org/abs/2303.16884)]| | [[Github](https://github.com/lsx0101/Instant-NeRF-Stylization)] |
|ArtNV |Artistic Style Novel View Synthesis Based on A Single Image  |CVPRW 2022, SIGGRAPH Posters 2022 |[[Paper](https://openaccess.thecvf.com/content/CVPR2022W/CVFAD/papers/Tseng_Artistic_Style_Novel_View_Synthesis_Based_on_a_Single_Image_CVPRW_2022_paper.pdf)]|[[Project](https://kuan-wei-tseng.github.io/ArtNV)]  |[[Github](https://github.com/Kuan-Wei-Tseng/ArtNV)]  |
| SNeRF |SNeRF: Stylized Neural Implicit Representations for 3D Scenes  | SIGGRAPH 2022|[[Paper](https://arxiv.org/abs/2207.02363)]| [[Project](https://research.facebook.com/publications/snerf-stylized-neural-implicit-representations-for-3d-scenes/)] |  |
| LipRF | Transforming Radiance Field with Lipschitz Network for Photorealistic 3D Scene Stylization |CVPR 2023 |[[Paper](https://arxiv.org/abs/2303.13232)] | |  |
|StyleRF  | StyleRF: Zero-shot 3D Style Transfer of Neural Radiance Fields | CVPR 2023|[[Paper](https://arxiv.org/abs/2303.10598)]|[[Project](https://kunhao-liu.github.io/StyleRF/)] | [[Github](https://github.com/Kunhao-Liu/StyleRF)] |
| Ref-NPR | Ref-NPR: Reference-Based Non-Photorealistic Radiance Fields for Controllable Scene Stylization | CVPR 2023|[[Paper](https://arxiv.org/abs/2212.02766)]|[[Project](https://ref-npr.github.io/)] |  [[Github](https://github.com/dvlab-research/Ref-NPR/)] |
| UPST-NeRF | UPST-NeRF: Universal Photorealistic Style Transfer of Neural Radiance Fields for 3D Scene | Arxiv 2022 | [[Paper](https://arxiv.org/pdf/2208.07059.pdf)] | [[Project](https://semchan.github.io/UPST_NeRF/)] | [[Github](https://github.com/semchan/UPST-NeRF)] |
| SINE |Semantic-driven Image-based NeRF Editing with Prior-guided Editing Field  | CVPR 2023|[[Paper](https://arxiv.org/abs/2303.13277)]|[[Project](https://zju3dv.github.io/sine/)] |  [[Github](https://github.com/zju3dv/SINE)]  |
| LocalStyleNeRF | Locally Stylized Neural Radiance Fields | ICCV 2023 | | [[Project](https://nerfstyle.hkustvgd.com/)] |  |
| NeRF-art | NeRF-Art: Text-Driven Neural Radiance Fields Stylization | TVCG 2023|[[Paper](https://arxiv.org/abs/2212.08070)]| [[Project](https://cassiepython.github.io/nerfart/)]|  [[Github](https://github.com/cassiePython/NeRF-Art)]|
|InstructN2N  | Instruct-NeRF2NeRF | ICCV 2023|[[Paper](https://arxiv.org/abs/2303.12789)] |[[Project](https://instruct-nerf2nerf.github.io/)]  | [[Github](https://github.com/ayaanzhaque/instruct-nerf2nerf)] |
| | | | | |  |


## Mesh Stylization
**Neural 3D Mesh Renderer**<br>
*Hiroharu Kato, Yoshitaka Ushiku, Tatsuya Harada*<br>
CVPR 2018. [[Paper](https://arxiv.org/abs/1711.07566)][[Project](https://hiroharu-kato.com/assets/downloads/cvpr_2018_poster.pdf)] [[Github](https://github.com/hiroharu-kato/style_transfer_3d)]  <br>
_Features_:
- approximate gradient for rasterization
- single-image 3d mesh reconstruction with 2d supervision
- gradient-based 3d mesh editing including 2d->3d style transfer(image->mesh)

**StyleMesh: Style Transfer for Indoor 3D Scene Reconstructions**<br>
*Lukas Höllein, Justin Johnson, Matthias Nießner*<br>
CVPR 2022. [[Paper](https://arxiv.org/abs/2112.01530)] [[Project](https://lukashoel.github.io/stylemesh/)] [[Github](https://github.com/lukasHoel/stylemesh)]  <br>
_Features_:
- 3D consistent texture optimization
- depth-aware and angle-aware optimization for equally-sized and unstreched stylization patterns

**Text2Mesh: Text-Driven Neural Stylization for Meshes**<br>
*Oscar Michel, Roi Bar-On, Richard Liu, Sagie Benaim, Rana Hanocka*<br>
CVPR 2022.[[Paper](https://arxiv.org/abs/2112.03221)] [[Project](https://threedle.github.io/text2mesh/)] [[Github](https://github.com/threedle/text2mesh)]  <br>
_Features_:
- based on CLIP[[Github](https://github.com/openai/CLIP)]
- handle low quality meshes

add more recent works

## Volumetric Stylization
**Efficient Neural Style Transfer For Volumetric Simulations**<br>
*Joshua Aurand, Raphaël Oritz, Sylvia Nauer, Vinicius Azevedo*<br>
ACM SIGGRAPH Asia, 2022. [[Paper](https://studios.disneyresearch.com/app/uploads/2022/10/Efficient-Neural-Style-Transfer-For-Volumetric-Simulations.pdf)][[Video](https://youtu.be/8tD5Yt3smDw)]<br>
_Features_:
- mainly for smoke
- view-independent stylization

## Novel View Stylization
### General Neural Rendering
**Learning to stylize novel views**<br>
*Hsin-Ping Huang, Hung-Yu Tseng, Saurabh Saini, Maneesh Singh, Ming-Hsuan Yang.* <br>
ICCV 2021. [[Paper](https://arxiv.org/abs/2105.13509)] [[Project](https://hhsinping.github.io/3d_scene_stylization/)] [[Github](https://github.com/hhsinping/stylescene)]  <br>
_Features_:
- Point-cloud based feature
- Style feature transformation

**Artistic Style Novel View Synthesis Based on A Single Image**<br>
*Kuan-Wei Tseng, Yao-Chih Lee, Chu-Song Chen*<br>
CVPR 2022.[[Paper](https://openaccess.thecvf.com/content/CVPR2022W/CVFAD/papers/Tseng_Artistic_Style_Novel_View_Synthesis_Based_on_a_Single_Image_CVPRW_2022_paper.pdf)] [[Project](https://kuan-wei-tseng.github.io/ArtNV)] [[Github](https://github.com/Kuan-Wei-Tseng/ArtNV)] <br>
_Features_:
- based on Synsin(differentiable point cloud renderer)[[Paper](https://arxiv.org/abs/1912.08804)]
- occlusion aware dense matching
- mainly for VR

<!-- CLIP3DStyler Arxiv 2023, point cloud based neural rendering-->

### Implicit Field Based Rendering
**Stylizing 3D Scene via Implicit Representation and HyperNetwork**<br>
*Pei-Ze Chiang, Meng-Shiun Tsai, Hung-Yu Tseng, Wei-sheng Lai, Wei-Chen Chiu.* <br>
WACV 2022. [[Paper](https://arxiv.org/abs/2105.13016)] [[Project](https://ztex08010518.github.io/3dstyletransfer/)] [[Github](https://github.com/ztex08010518/Stylizing-3D-Scene)]  <br>
_Features_:
- hypernetwork to control NeRF weights
- two-step training and patch-subsampling

**StylizedNeRF: Consistent 3D Scene Stylization as Stylized NeRF via 2D-3D Mutual Learning**<br>
*Yi-Hua Huang, Yue He, Yu-Jie Yuan, Yu-Kun Lai, Lin Gao*<br>
CVPR 2022. [[Paper](https://arxiv.org/abs/2205.12183)] [[Project](http://geometrylearning.com/StylizedNeRF/)] [[Github](https://github.com/IGLICT/StylizedNeRF)]  <br>
_Features_:
- pre-trained NeRF with color prediction module replaced with a style network
- mutual learning for two parts mentioned above

**3D Photo Stylization: Learning to Generate Stylized Novel Views from a Single Image**<br>
*Fangzhou Mu, Jian Wang, Yicheng Wu, Yin Li*<br>
CVPR 2022. [[Paper](https://arxiv.org/abs/2112.00169)] [[Project](https://pages.cs.wisc.edu/~fmu/style3d/)] [[Github](https://github.com/fmu2/3d_photo_stylization)]  <br>
_Features_:
- pre-trained NeRF with color prediction module replaced with a style network
- mutual learning for two parts mentioned above

**ARF: Artistic Radiance Fields**<br>
*Kai Zhang, Nick Kolkin, Sai Bi, Fujun Luan, Zexiang Xu, Eli Shechtman, Noah Snavely*<br>
ECCV 2022. [[Paper](https://arxiv.org/abs/2206.06360)] [[Project](https://www.cs.cornell.edu/projects/arf/)] [[Github](https://github.com/Kai-46/ARF-svox2)]  <br>
_Features_:
- pre-trained NeRF with color prediction module replaced with a style network
- mutual learning for two parts mentioned above

**Unified Implicit Neural Stylization**<br>
*Zhiwen Fan, Yifan Jiang, Peihao Wang, Xinyu Gong, Dejia Xu, Zhangyang Wang*<br>
ECCV 2022. [[Paper](https://arxiv.org/abs/2204.01943)] [[Project](https://zhiwenfan.github.io/INS/)] [[Github](https://github.com/VITA-Group/INS)]  <br>
_Features_:
- continuous in the style space(allow interpolation between styles)

**Instant Neural Radiance Fields Stylization**<br>
*Shaoxu Li, Ye Pan*<br>
[[Paper](https://arxiv.org/abs/2303.16884)] [[Github](https://github.com/lsx0101/Instant-NeRF-Stylization)] <br>
_Features_:
- training for novel view stylization image synthesis only costs 10 minutes.
- extend the style target of NeRF stylization from images to 3D scene image sets

**SNeRF: Stylized Neural Implicit Representations for 3D Scenes**<br>
*Thu Nguyen-Phuoc, Feng Liu, Lei Xiao*<br>
SIGGRAPH 2022.[[Paper](https://arxiv.org/abs/2207.02363)]<br>
_Features_:
- applies to indoor scenes, outdoor scenes and 4D dynamic avatars
- reduce GPU memory requirement

**Transforming Radiance Field with Lipschitz Network for Photorealistic 3D Scene Stylization**<br>
*Zicheng Zhang, Yinglu Liu, Congying Han, Yingwei Pan, Tiande Guo, Ting Yao*<br>
CVPR 2023. [[Paper](https://arxiv.org/abs/2303.13232)] <br>
_Features_:
- photo-realistic
- based on Lipschitz transformation and condition

**StyleRF: Zero-shot 3D Style Transfer of Neural Radiance Fields**<br>
*Kunhao Liu, Fangneng Zhan, Yiwen Chen, Jiahui Zhang, Yingchen Yu, Abdulmotaleb El Saddik, Shijian Lu, Eric Xing*<br>
CVPR 2023. [[Paper](https://arxiv.org/abs/2303.10598)] [[Project](https://kunhao-liu.github.io/StyleRF/)] [[Github](https://github.com/Kunhao-Liu/StyleRF)] <br>
_Features_:
- zero-shot 3d stylization
- sampling-invariant content transformation
- deferring style transformation to 2D feature maps

**Ref-NPR: Reference-Based Non-Photorealistic Radiance Fields for Controllable Scene Stylization**<br>
*Yuechen Zhang, Zexin He, Jinbo Xing, Xufeng Yao, Jiaya Jia*<br>
CVPR 2023. [[Paper](https://arxiv.org/abs/2212.02766)] [[Project](https://ref-npr.github.io/)] [[Github](https://github.com/dvlab-research/Ref-NPR/)] <br>
_Features_:
- reference based ray registration process and a template-based feature matching scheme to achieve geometrically and perceptually consistent stylization

**NeRF-Art: Text-Driven Neural Radiance Fields Stylization**<br>
*Can Wang, Ruixiang Jiang, Menglei Chai, Mingming He, Dongdong Chen, Jing Liao*<br>
TVCG 2023. [[Paper](https://arxiv.org/abs/2212.08070)] [[Project](https://cassiepython.github.io/nerfart/)] [[Github](https://github.com/cassiePython/NeRF-Art)] <br>
_Features_:
- combine CLIP[[Github](https://github.com/openai/CLIP)] with NeRF
- cover global structures and local details 
- adopt a weight regularization to effectively reduce cloudy artifacts and geometry noises

**Instruct-NeRF2NeRF**<br>
*Ayaan Haque, Matthew Tancik, Alexei A. Efros, Aleksander Holynski, Angjoo Kanazawa*<br>
ICCV 2023. [[Paper](https://arxiv.org/abs/2303.12789)] [[Project](https://instruct-nerf2nerf.github.io/)] [[Github](https://github.com/ayaanzhaque/instruct-nerf2nerf)] <br>
_Features_:
- extract shape and appearance priors from a 2D diffusion model
- edit input images and change 3d implicit field representation

**Semantic-driven Image-based NeRF Editing with Prior-guided Editing Field**<br>
*Chong Bao, Yinda Zhang, Bangbang Yang, Tianxing Fan, Zesong Yang, Hujun Bao, Guofeng Zhang, Zhaopeng Cui*<br>
CVPR 2023. [[Paper](https://arxiv.org/abs/2303.13277)] [[Project](https://zju3dv.github.io/sine/)] [[Github](https://github.com/zju3dv/SINE)] <br>
_Features_:
- edit a photo-realistic NeRF with a single-view image or with text prompts
- cyclic constraints with a proxy mesh for geometric editing
- the color compositing mechanism to enhance texture editing
- feature-cluster-based regularization to control the affected editing area and maintain irrelevant parts unchanged

<!--[[Paper]()] [[Project]()] [[Github]()] <br>-->
