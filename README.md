# <p align='center'>`Advances in 3D Neural Stylization`</p>

A review of 3D neural stylization papers, mainly neural stylization on 3D data with image or text reference.

Other variants are also welcomed, e.g., with other/no reference, 3D-aware neural stylization, non-neural 3D stylization.

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

## Surveys
**Advances in 3D Neural Stylization: A Survey** <br>
_Yingshu Chen, Guocheng Shao, Ka Chun Shum, Binh-Son Hua, Sai-Kit Yeung._ 2023.<br>
<!--<a href="https://advances3dstyle.hkustvgd.com/"><img src="https://img.shields.io/badge/WEBSITE-stay%20tuned-blue?style=for-the-badge"></a>-->
<a href="#"><img src="https://img.shields.io/badge/WEBSITE-stay%20tuned-efefef?style=for-the-badge"></a>
<a href="https://arxiv.org/abs/2311.18328"><img src="https://img.shields.io/badge/arxiv-2311.18328-red?style=for-the-badge"></a>
<a href="https://github.com/chenyingshu/advances_3d_neural_stylization"><img src="https://img.shields.io/badge/CODE-Access%20Github-0366d6?style=for-the-badge"></a>
<!--<a href="https://chenyingshu.github.ioadvances_3d_neural_stylization/assets/survey.pdf"><img src="https://img.shields.io/badge/paper-download%20paper-green?style=for-the-badge"></a>-->
<br>

If you find this work useful, please cite our paper:
```bibtex
@article{chen2023advances3dstyle,
  title={Advances in 3D Neural Stylization: A Survey},
  author={Chen, Yingshu and Shao, Guocheng and Shum, Ka Chun and Hua, Binh-Son and Yeung, Sai-Kit},
  journal={arXiv preprint arXiv:2311.18328},
  year={2023}
}
```
<details>
  <summary>
    
### Other related surveys, courses
  </summary>
  
**Neural Style Transfer: A Review** [[Paper](https://arxiv.org/abs/1705.04058)] [[Project](https://github.com/ycjing/Neural-Style-Transfer-Papers)] <br>
*Yongcheng Jing, Yezhou Yang, Zunlei Feng, Jingwen Ye, Yizhou Yu, Mingli Song.* TVCG, 2019.

**Multimodal Image Synthesis and Editing: The Generative AI Era** [[Paper](https://arxiv.org/abs/2112.13592)]  [[Project](https://fnzhan.com/Generative-AI/)]  <br>
*Fangneng Zhan, Yingchen Yu, Rongliang Wu, Jiahui Zhang, Shijian Lu, Lingjie Liu, Adam Kortylewski, Christian Theobalt, Eric Xing.* TPAMI, 2023.

**Diffusion Models in Vision: A Survey** [[Paper](https://arxiv.org/abs/2209.04747)] [[Project](https://github.com/CroitoruAlin/Diffusion-Models-in-Vision-A-Survey)] <br>
*Florinel-Alin Croitoru, Vlad Hondru, Radu Tudor Ionescu, Mubarak Shah.* TPAMI, 2023.

**Diffusion Models: A Comprehensive Survey of Methods and Applications** [[Paper](https://arxiv.org/abs/2209.00796)][[Project](https://github.com/YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy)] <br>
*Ling Yang, Zhilong Zhang, Yang Song, Shenda Hong, Runsheng Xu, Yue Zhao, Wentao Zhang, Bin Cui, Ming-Hsuan Yang.* ACM Computing Surveys 2023.

**State of the Art on Neural Rendering** [[Paper](https://arxiv.org/abs/2004.03805)] <br>
*Ayush Tewari, Ohad Fried, Justus Thies, Vincent Sitzmann, Stephen Lombardi, Kalyan Sunkavalli, Ricardo Martin-Brualla, Tomas Simon, Jason Saragih, Matthias Nießner, Rohit Pandey, Sean Fanello, Gordon Wetzstein, Jun-Yan Zhu, Christian Theobalt, Maneesh Agrawala, Eli Shechtman, Dan B Goldman, Michael Zollhöfer.* State of the Art Report at EUROGRAPHICS 2020. <br>
**Neural Rendering** [[Project](https://www.neuralrender.com/CVPR/)] CVPR 2020 Tutorial. <br>
**Advances in Neural Rendering** [[Paper](https://dl.acm.org/doi/10.1145/3450508.3464573)] [[Project](https://www.neuralrender.com/)] SIGGRAPH 2021 Courses.


**Advances in Neural Rendering** [[Paper](https://arxiv.org/abs/2111.05849)] <br>
*Ayush Tewari, Justus Thies, Ben Mildenhall, Pratul Srinivasan, Edgar Tretschk, Yifan Wang, Christoph Lassner, Vincent Sitzmann, Ricardo Martin-Brualla, Stephen Lombardi, Tomas Simon, Christian Theobalt, Matthias Niessner, Jonathan T. Barron, Gordon Wetzstein, Michael Zollhoefer, Vladislav Golyanik.* State of the Art Report at EUROGRAPHICS 2022.

**Neural Fields in Visual Computing and Beyond** [[Paper](https://arxiv.org/abs/2111.11426)]  [[Project](https://neuralfields.cs.brown.edu/)]  <br>
*Yiheng Xie, Towaki Takikawa, Shunsuke Saito, Or Litany, Shiqin Yan, Numair Khan, Federico Tombari, James Tompkin, Vincent Sitzmann, Srinath Sridhar.* State of the Art Report at EUROGRAPHICS 2022. <br>
**Neural Fields for Visual Computing** [[Paper](https://dl.acm.org/doi/abs/10.1145/3587423.3595477)] [[Project](https://neuralfields.cs.brown.edu/siggraph23.html)] <br>
*Towaki Takikawa, Shunsuke Saito, James Tompkin, Vincent Sitzmann, Srinath Sridhar, Or Litany, Alex Yu.* SIGGRAPH 2023 Courses.<br>

**Generative AI meets 3D: A Survey on Text-to-3D in AIGC Era** [[Paper](https://arxiv.org/abs/2305.06131)]<br>
*Chenghao Li, Chaoning Zhang, Atish Waghwase, Lik-Hang Lee, Francois Rameau, Yang Yang, Sung-Ho Bae, Choong Seon Hong*<br>
</details>

## Table of Contents
- [Mesh Stylization](#mesh-stylization)
- [Volumetric Stylization](#volumetric-stylization)
- [Point Cloud Stylization](#point-cloud-stylization)
- [Novel View Stylization](#novel-view-stylization)
- [Evaluation]()


<details open>
  <summary>
    
## Overview of 3D Neural Stylization ##
  </summary>
<div align=left> 
  Image guidance: <img align=top src="assets/icon_image.png" width="32" height="32"> 
  Text guidance: <img align=top src="assets/icon_text.png" width="32" height="32"> 
  3D guidance: <img align=top src="assets/icon_obj.png" width="32" height="32"> 
</div>

|  Abbr.  |  Title   | Venue  | Paper  | Project  | Github  |
|  ----  |  ----    | ----  |----   |----  |----  |
|  |**Mesh Stylization**  | || |  |
|  Neural Renderer <br><img src="assets/icon_image.png" width="20" height="20">  | Neural 3D Mesh Renderer |CVPR 2018|[[Paper](https://arxiv.org/abs/1711.07566)]|[[Project](https://hiroharu-kato.com/assets/downloads/cvpr_2018_poster.pdf)] | [[Github](https://github.com/hiroharu-kato/style_transfer_3d)] |
| Paparazzi <br><img src="assets/icon_image.png" width="20" height="20">| Paparazzi: Surface Editing by way of Multi-View Image Processing | SIGGRAPH Asia 2018 | [[Paper](https://www.dgp.toronto.edu/projects/paparazzi/paparazzi-surface-editing-by-way-of-multi-view-image-processing-siggraph-asia-2018-liu-et-al.pdf)] | [[Project](https://www.dgp.toronto.edu/projects/paparazzi/)] | [[Github](https://github.com/HTDerekLiu/Paparazzi)] |
| DGTS <br><img src="assets/icon_obj.png" width="20" height="20">| Deep Geometric Texture Synthesis| SIGGRAPH 2020 | [[Paper](https://arxiv.org/abs/2007.00074)] | [[Project](https://ranahanocka.github.io/geometric-textures/)]| [[Github](https://github.com/amirhertz/geometric-textures)]|
| 3DStyleNet <br><img src="assets/icon_obj.png" width="20" height="20">| 3DStyleNet: Creating 3D Shapes with Geometric and Texture Style | ICCV 2021| [[Paper](https://research.nvidia.com/labs/toronto-ai/3DStyleNet/assets/3dstyle-paper.pdf)] | [[Project](https://research.nvidia.com/labs/toronto-ai/3DStyleNet/)] |  |
|  StyleMesh <br><img src="assets/icon_image.png" width="20" height="20">| StyleMesh: Style Transfer for Indoor 3D Scene Reconstructions   | CVPR 2022 |  [[Paper](https://arxiv.org/abs/2112.01530)]  |  [[Project](https://lukashoel.github.io/stylemesh/)]  | [[Github](https://github.com/lukasHoel/stylemesh)]   | 
| Creative Birds <br><img src="assets/icon_text.png" width="20" height="20">| Creative Birds: Self-Supervised Single-View 3D Style Transfer | ICCV 2023 | [[Paper](https://arxiv.org/abs/2307.14127)] | | [[Github](https://github.com/wrk226/creative_birds)] |
|Latent-NeRF  <br><img src="assets/icon_text.png" width="20" height="20"> |Latent-NeRF for Shape-Guided Generation of 3D Shapes and Textures | CVPR 2022 | [[Paper](https://arxiv.org/abs/2211.07600)] |[[Video](https://youtu.be/WwOXzWvGNdc)] | [[Github](https://github.com/eladrich/latent-nerf)]|
| Text2Mesh <br><img src="assets/icon_text.png" width="20" height="20"><img src="assets/icon_image.png" width="20" height="20">|Text2Mesh: Text-Driven Neural Stylization for Meshes  |CVPR 2022|[[Paper](https://arxiv.org/abs/2112.03221)]| [[Project](https://threedle.github.io/text2mesh/)] | [[Github](https://github.com/threedle/text2mesh)]  |
| TANGO <br><img src="assets/icon_text.png" width="20" height="20">|TANGO: Text-driven Photorealistic and Robust 3D Stylization via Lighting Decomposition  |NeurIPS 2022|[[Paper](http://arxiv.org/abs/2210.11277)]| [[Project](https://cyw-3d.github.io/tango/)] | [[Github](https://github.com/Gorilla-Lab-SCUT/tango)]  |
| CLIP-Mesh <br><img src="assets/icon_text.png" width="20" height="20">|CLIP-Mesh: Generating textured meshes from text using pretrained image-text models  |SIGGRAPH Asia 2022 |[[Paper](https://arxiv.org/abs/2203.13333)]| [[Project](https://www.nasir.lol/clipmesh)] | [[Github](https://github.com/NasirKhalid24/CLIP-Mesh)]  |
| Text2Scene <br><img src="assets/icon_image.png" width="20" height="20"><img src="assets/icon_text.png" width="20" height="20">| Text2Scene: Text-Driven Indoor Scene Stylization With Part-Aware Details  |CVPR 2023|[[Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Hwang_Text2Scene_Text-Driven_Indoor_Scene_Stylization_With_Part-Aware_Details_CVPR_2023_paper.html)]| [[Video](https://www.youtube.com/watch?v=CGIXY2kwIYM)] |  |
| TextDeformer <br><img src="assets/icon_text.png" width="20" height="20">| TextDeformer: Geometry Manipulation using Text Guidance | SIGGRAPH 2023 Conf Paper| [[Paper](https://arxiv.org/abs/2304.13348)] | [[Project](https://threedle.github.io/TextDeformer/)] | [[Github](https://github.com/threedle/TextDeformer)] |
| TEXTure <br><img src="assets/icon_text.png" width="20" height="20"><img src="assets/icon_image.png" width="20" height="20">| TEXTure: Text-Guided Texturing of 3D Shapes | SIGGRAPH 2023 Conf Paper | [[Paper](https://arxiv.org/abs/2302.01721)] | [[Project](https://texturepaper.github.io/TEXTurePaper/)] | [[Github](https://github.com/TEXTurePaper/TEXTurePaper)] |
| Text2Tex <br><img src="assets/icon_text.png" width="20" height="20">| Text2Tex: Text-driven Texture Synthesis via Diffusion Models | ICCV 2023 | [[Paper](https://daveredrum.github.io/Text2Tex/static/Text2Tex.pdf)] | [[Project](https://daveredrum.github.io/Text2Tex/)] | [[Github](https://github.com/daveredrum/Text2Tex)] |
|TexFusion <br><img src="assets/icon_text.png" width="20" height="20">| TexFusion: Synthesizing 3D Textures with Text-Guided Image Diffusion Models| ICCV 2023 |[[Paper](https://openaccess.thecvf.com//content/ICCV2023/papers/Cao_TexFusion_Synthesizing_3D_Textures_with_Text-Guided_Image_Diffusion_Models_ICCV_2023_paper.pdf)] | [[Project](https://research.nvidia.com/labs/toronto-ai/publication/2023_iccv_texfusion/)]|  | 
| X-Mesh <br><img src="assets/icon_text.png" width="20" height="20">| X-Mesh:Towards Fast and Accurate Text-driven 3D Stylization via Dynamic Textual Guidance | ICCV 2023 | [[Paper](https://arxiv.org/abs/2303.15764)] | [[Project](https://xmu-xiaoma666.github.io/Projects/X-Mesh/)] | [[Github](https://github.com/xmu-xiaoma666/X-Mesh)] |
|Point-UV Diffusion  <br><img src="assets/icon_text.png" width="20" height="20"><img src="assets/icon_image.png" width="20" height="20"> |Texture Generation on 3D Meshes with Point-UV Diffusion | ICCV 2023| [[Paper](https://cvmi-lab.github.io/Point-UV-Diffusion/paper/point_uv_diffusion.pdf)] |[[Project](https://cvmi-lab.github.io/Point-UV-Diffusion/)] | [[Github](https://github.com/CVMI-Lab/Point-UV-Diffusion)]|
|3DStyle-Diffusion<br><img src="assets/icon_text.png" width="20" height="20"> | 3DStyle-Diffusion: Pursuing Fine-grained Text-driven 3D Stylization with 2D Diffusion Models | ACM MM 2023| [[Paper](https://arxiv.org/abs/2311.05464)] | | [[Github(TBA)](https://github.com/yanghb22-fdu/3dstyle-diffusion-official)] |
|RoomDreamer<br><img src="assets/icon_text.png" width="20" height="20"> | RoomDreamer: Text-Driven 3D Indoor Scene Synthesis with Coherent Geometry and Texture |ACM MM 2023| [[Paper](https://arxiv.org/abs/2305.11337)]| [[Video](https://youtu.be/p4xgwj4QJcQ)] | |
| DreamSpace <br><img src="assets/icon_text.png" width="20" height="20"> | Dreaming Your Room Space with Text-Driven Panoramic Texture Propagation| Arxiv 2023| [[Paper](https://ybbbbt.com/publication/dreamspace/media/DreamSpace.pdf)] | [[Project](https://ybbbbt.com/publication/dreamspace/)] | [[Github](https://github.com/ybbbbt/dreamspace)] |
| Decorate3D <br><img src="assets/icon_text.png" width="20" height="20"> | Decorate3D: Text-Driven High-Quality Texture Generation for Mesh Decoration in the Wild| NeurIPS 2023| [[Paper](https://decorate3d.github.io/Decorate3D/static/Decorate3D.pdf)] | [[Project](https://decorate3d.github.io/Decorate3D/)] | [[Github(TBA)](https://github.com/Decorate3D/Decorate3D)] |
|TECA <br><img src="assets/icon_text.png" width="20" height="20">|TECA: Text-Guided Generation and Editing of Compositional 3D Avatars |3DV 2024 |[[Paper](https://arxiv.org/abs/2309.07125)]|[[Project](https://yfeng95.github.io/teca/)]|[[Github](https://github.com/HaoZhang990127/TECA)] |
|HyperDreamer <br><img src="assets/icon_text.png" width="20" height="20">|HyperDreamer: Hyper-Realistic 3D Content Generation and Editing from a Single Image |SIGGRAPH Asia 2023 Conf Paper |[[Paper](https://arxiv.org/abs/2312.04543)] |[[Project](https://ys-imtech.github.io/HyperDreamer/)]| [[Github(TBA)](https://github.com/wutong16/HyperDreamer)]|
|SceneTex<br><img src="assets/icon_text.png" width="20" height="20"> | SceneTex: High-Quality Texture Synthesis for Indoor Scenes via Diffusion Priors |Arxiv 2023| [[Paper](https://arxiv.org/abs/2311.17261)]| [[Project](https://daveredrum.github.io/SceneTex/)]| [[Github](https://github.com/daveredrum/SceneTex)]|
|Paint-it <br><img src="assets/icon_text.png" width="20" height="20">  | Paint-it: Text-to-Texture Synthesis via Deep Convolutional Texture Map Optimization and Physically-Based Rendering| Arxiv 2023| [[Paper](https://kim-youwang.github.io/media/paint-it/paint-it.pdf)]|[[Project](https://kim-youwang.github.io/paint-it)] | [[Github(TBA)](https://github.com/postech-ami/paint-it)] |
|AlteredAvatar <br><img src="assets/icon_text.png" width="20" height="20">|AlteredAvatar: Stylizing Dynamic 3D Avatars with Fast Style Adaptation|Arxiv 2023| [[Paper](https://arxiv.org/abs/2305.19245)]| [[Project](https://alteredavatar.github.io/)]||
|StyleAvatar <br><img src="assets/icon_text.png" width="20" height="20"><img src="assets/icon_image.png" width="20" height="20">|StyleAvatar: Stylizing Animatable Head Avatars| WACV 2024|[[Paper](https://openaccess.thecvf.com/content/WACV2024/papers/Perez_StyleAvatar_Stylizing_Animatable_Head_Avatars_WACV_2024_paper.pdf)]|||
|Paint3D <br><img src="assets/icon_text.png" width="20" height="20"><img src="assets/icon_image.png" width="20" height="20">|Paint3D: Paint Anything 3D with Lighting-Less Texture Diffusion Models|Arxiv 2023| [[Paper](https://arxiv.org/abs/2312.13913)]|[[Project](https://paint3d.github.io/)] |[[Github(TBA)](https://github.com/OpenTexture/Paint3D)]|
|TextureDreamer <br><img src="assets/icon_image.png" width="20" height="20">|TextureDreamer: Image-guided Texture Synthesis through Geometry-aware Diffusion | Arxiv 2024| [[Paper](https://arxiv.org/abs/2401.09416)] | [[Project](https://texturedreamer.github.io/)]| |
|  |**Volumetric Stylization**  | || |  |
| TNST <br><img src="assets/icon_image.png" width="20" height="20">|Transport-Based Neural Style Transfer for Smoke Simulations|  SIGGRAPH Asia 2019| [[Paper](http://arxiv.org/abs/1905.07442)] | [[Video](https://www.youtube.com/watch?v=67qVRhoOQPE)]|[[Github](https://github.com/byungsook/neural-flow-style/tree/tnst)]  |
| LNST <br><img src="assets/icon_image.png" width="20" height="20">| Lagrangian Neural Style Transfer for Fluids | SIGGRAPH 2020 | [[Paper](http://arxiv.org/abs/2005.00803)] | [[Video](https://www.youtube.com/watch?v=WPmUsIVf3-4)]|[[Github](https://github.com/byungsook/neural-flow-style/tree/lnst)]  |
| SKPN <br><img src="assets/icon_image.png" width="20" height="20">| Volumetric appearance stylization with stylizing kernel prediction network|SIGGRAPH 2021  | [[Paper](https://sites.cs.ucsb.edu/~lingqi/publications/paper_volst.pdf)] | [[Video](https://dl.acm.org/doi/abs/10.1145/3450626.3459799)]|  |
| ENST <br><img src="assets/icon_image.png" width="20" height="20">| Efficient Neural Style Transfer For Volumetric Simulations | SIGGRAPH Asia 2022|  [[Paper](https://studios.disneyresearch.com/app/uploads/2022/10/Efficient-Neural-Style-Transfer-For-Volumetric-Simulations.pdf)]| [[Project](https://studios.disneyresearch.com/2022/11/30/efficient-neural-style-transfer-for-volumetric-simulations/)] |  |
| ShaDDR <br> <img src="assets/icon_obj.png" width="20" height="20">  | ShaDDR: Interactive Example-Based Geometry and Texture Generation via 3D Shape Detailization and Differentiable Rendering   | SIGGRAPH Asia 2023 Conf Paper |[[Paper](https://arxiv.org/abs/2306.04889)]  | [[Project](https://qiminchen.github.io/shaddr/)] |[[Github](https://github.com/qiminchen/ShaDDR)] |
|  | **Point Cloud Stylization** | || |  |
| PSNet <br><img src="assets/icon_obj.png" width="20" height="20"><img src="assets/icon_image.png" width="20" height="20">| PSNet: A Style Transfer Network for Point Cloud Stylization on Geometry and Color |WACV 2020 | [[Paper](https://openaccess.thecvf.com/content_WACV_2020/html/Cao_PSNet_A_Style_Transfer_Network_for_Point_Cloud_Stylization_on_WACV_2020_paper.html)]| [[Video](https://www.youtube.com/watch?v=EbUOg1gVcFw&t=1818s)] | [[Github](https://github.com/xucao-42/psnet)] |
| PointInverter | PointInverter: Point Cloud Reconstruction and Editing via a Generative Model with Shape Priors | WACV 2023 | [[Paper](https://arxiv.org/abs/2211.08702)]| [[Project](https://ja-yeon-kim.github.io/PointInverter/)] | |
||**Implicit Shape Stylization**||||
|Neural Wavelet |Neural Wavelet-domain Diffusion for 3D Shape Generation, Inversion, and Manipulation | SIGGRAPH Asia 2022 Conf Paper| [[Paper](https://arxiv.org/abs/2302.00190)]||[[Github](https://github.com/edward1997104/Wavelet-Generation)]|
|SPAGHETTI |SPAGHETTI: Editing Implicit Shapes Through Part Aware Generation| SIGGRAPH 2022, TOG| [[Paper](https://igl.ethz.ch/projects/SPAGHETTI/SPAGHETTI-paper.pdf)]|[[Project](https://igl.ethz.ch/projects/SPAGHETTI/)]| [[Github](https://github.com/amirhertz/spaghetti)]|
|SALAD |SALAD: Part-Level Latent Diffusion for 3D Shape Generation and Manipulation| ICCV 2023| [[Paper](https://salad3d.github.io/assets/salad.pdf)]| [[Project](https://salad3d.github.io/)]| [[Github](https://github.com/KAIST-Geometric-AI-Group/SALAD)]|
|  | **Novel View Stylization** | || |  |
|  LSNV <br><img src="assets/icon_image.png" width="20" height="20"> | Learning to stylize novel views |  ICCV 2021  | [[Paper](https://arxiv.org/abs/2105.13509)]   | [[Project](https://hhsinping.github.io/3d_scene_stylization/)]   |  [[Github](https://github.com/hhsinping/stylescene)] |
| HyperStyle <br><img src="assets/icon_image.png" width="20" height="20"> | Stylizing 3D Scene via Implicit Representation and HyperNetwork |WACV 2022 | [[Paper](https://arxiv.org/abs/2105.13016)] |  [[Project](https://ztex08010518.github.io/3dstyletransfer/)] | [[Github](https://github.com/ztex08010518/Stylizing-3D-Scene)] |
| StylizedNeRF <br><img src="assets/icon_image.png" width="20" height="20"> | StylizedNeRF: Consistent 3D Scene Stylization as Stylized NeRF via 2D-3D Mutual Learning | CVPR 2022|[[Paper](https://arxiv.org/abs/2205.12183)]| [[Project](http://geometrylearning.com/StylizedNeRF/)]| [[Github](https://github.com/IGLICT/StylizedNeRF)] |
|3D Photo Stylization <br><img src="assets/icon_image.png" width="20" height="20">| 3D Photo Stylization: Learning to Generate Stylized Novel Views from a Single Image | CVPR 2022|[[Paper](https://arxiv.org/abs/2112.00169)]|[[Project](https://pages.cs.wisc.edu/~fmu/style3d/)]  | [[Github](https://github.com/fmu2/3d_photo_stylization)]  |
| ARF <br><img src="assets/icon_image.png" width="20" height="20">|ARF: Artistic Radiance Fields  | ECCV 2022|[[Paper](https://arxiv.org/abs/2206.06360)]|[[Project](https://www.cs.cornell.edu/projects/arf/)] | [[Github](https://github.com/Kai-46/ARF-svox2)] |
| UINS <br><img src="assets/icon_image.png" width="20" height="20"> | Unified Implicit Neural Stylization |ECCV 2022 |[[Paper](https://arxiv.org/abs/2204.01943)]|[[Project](https://zhiwenfan.github.io/INS/)]  | [[Github](https://github.com/VITA-Group/INS)] |
| INS <br><img src="assets/icon_image.png" width="20" height="20"> | Instant Neural Radiance Fields Stylization | ArXiv 2023 |[[Paper](https://arxiv.org/abs/2303.16884)]| | [[Github](https://github.com/lsx0101/Instant-NeRF-Stylization)] |
| ArtNV <br><img src="assets/icon_image.png" width="20" height="20">|Artistic Style Novel View Synthesis Based on A Single Image  |CVPRW 2022, SIGGRAPH Posters 2022 |[[Paper](https://openaccess.thecvf.com/content/CVPR2022W/CVFAD/papers/Tseng_Artistic_Style_Novel_View_Synthesis_Based_on_a_Single_Image_CVPRW_2022_paper.pdf)]|[[Project](https://kuan-wei-tseng.github.io/ArtNV)]  |[[Github](https://github.com/Kuan-Wei-Tseng/ArtNV)]  |
| SNeRF <br><img src="assets/icon_image.png" width="20" height="20"> |SNeRF: Stylized Neural Implicit Representations for 3D Scenes  | SIGGRAPH 2022|[[Paper](https://arxiv.org/abs/2207.02363)]| [[Project](https://research.facebook.com/publications/snerf-stylized-neural-implicit-representations-for-3d-scenes/)] |  |
| LipRF <br><img src="assets/icon_image.png" width="20" height="20">| Transforming Radiance Field with Lipschitz Network for Photorealistic 3D Scene Stylization |CVPR 2023 |[[Paper](https://arxiv.org/abs/2303.13232)] | |  |
|StyleRF  <br><img src="assets/icon_image.png" width="20" height="20">| StyleRF: Zero-shot 3D Style Transfer of Neural Radiance Fields | CVPR 2023|[[Paper](https://arxiv.org/abs/2303.10598)]|[[Project](https://kunhao-liu.github.io/StyleRF/)] | [[Github](https://github.com/Kunhao-Liu/StyleRF)] |
| Ref-NPR <br><img src="assets/icon_image.png" width="20" height="20"><img src="assets/icon_text.png" width="20" height="20">| Ref-NPR: Reference-Based Non-Photorealistic Radiance Fields for Controllable Scene Stylization | CVPR 2023|[[Paper](https://arxiv.org/abs/2212.02766)]|[[Project](https://ref-npr.github.io/)] |  [[Github](https://github.com/dvlab-research/Ref-NPR/)] |
| UPST-NeRF <br><img src="assets/icon_image.png" width="20" height="20">| UPST-NeRF: Universal Photorealistic Style Transfer of Neural Radiance Fields for 3D Scene | Arxiv 2022 | [[Paper](https://arxiv.org/pdf/2208.07059.pdf)] | [[Project](https://semchan.github.io/UPST_NeRF/)] | [[Github](https://github.com/semchan/UPST-NeRF)] |
| LocalStyleNeRF <br><img src="assets/icon_image.png" width="20" height="20">| Locally Stylized Neural Radiance Fields | ICCV 2023 |[[Paper](https://arxiv.org/abs/2309.10684)] | [[Project](https://nerfstyle.hkustvgd.com/)] | [[Github](https://github.com/hkust-vgd/nerfstyle)] |
| SINE <br><img src="assets/icon_image.png" width="20" height="20"><img src="assets/icon_text.png" width="20" height="20">|Semantic-driven Image-based NeRF Editing with Prior-guided Editing Field  | CVPR 2023|[[Paper](https://arxiv.org/abs/2303.13277)]|[[Project](https://zju3dv.github.io/sine/)] |  [[Github](https://github.com/zju3dv/SINE)]|
| NeRF-art <br><img src="assets/icon_text.png" width="20" height="20">| NeRF-Art: Text-Driven Neural Radiance Fields Stylization | TVCG 2023|[[Paper](https://arxiv.org/abs/2212.08070)]| [[Project](https://cassiepython.github.io/nerfart/)]|  [[Github](https://github.com/cassiePython/NeRF-Art)]|
| TSNeRF <br><img src="assets/icon_text.png" width="20" height="20">| TSNeRF: Text-driven stylized neural radiance fields via semantic contrastive learning | Computers & Graphics 2023,  CCF CAD/Graphics 2023 | [[Paper](https://www.sciencedirect.com/science/article/pii/S0097849323001796)] | |  |
|InstructN2N <br><img src="assets/icon_text.png" width="20" height="20"> | Instruct-NeRF2NeRF | ICCV 2023|[[Paper](https://arxiv.org/abs/2303.12789)] |[[Project](https://instruct-nerf2nerf.github.io/)]  | [[Github](https://github.com/ayaanzhaque/instruct-nerf2nerf)] |
| Blending-NeRF <br><img src="assets/icon_text.png" width="20" height="20">| Blending-NeRF: Text-Driven Localized Editing in Neural Radiance Fields | ICCV 2023 | [[Paper](https://arxiv.org/pdf/2308.11974)] | [[Project](https://seokhunchoi.github.io/Blending-NeRF/)] |  |
|Vox-E <br><img src="assets/icon_text.png" width="20" height="20">|Vox-E: Text-guided Voxel Editing of 3D Objects |ICCV 2023 |[[Paper](https://arxiv.org/abs/2303.12048/)]|[[Project](https://tau-vailab.github.io/Vox-E/)]|[[Github](https://github.com/TAU-VAILab/Vox-E)]|
|ClimateNeRF |ClimateNeRF: Extreme Weather Synthesis in Neural Radiance Field| ICCV 2023| [[Paper](https://arxiv.org/abs/2211.13226)]| [[Project](https://climatenerf.github.io/)]| [[Github](https://github.com/y-u-a-n-l-i/Climate_NeRF)]|
|ViCA-NeRF | ViCA-NeRF: View-Consistency-Aware 3D Editing of Neural Radiance Fields|NeurIPS 2023 | | |  |
|CoARF | CoARF: Controllable 3D Artistic Style Transfer for Radiance Fields| 3DV 2024| | |  |
|MuVieCAST <br><img src="assets/icon_image.png" width="20" height="20">| MuVieCAST: Multi-View Consistent Artistic Style Transfer|3DV 2024 |[[Paper](https://arxiv.org/abs/2312.05046)]|[[Project](https://muviecast.github.io/)]|[[Github](https://github.com/Mirmix/muviecast)]|
|DreamEditor <br><img src="assets/icon_text.png" width="20" height="20"> | DreamEditor: Text-Driven 3D Scene Editing with Neural Fields| SIGGRAPH Asia 2023 Conf Paper| [[Paper](https://arxiv.org/abs/2306.13455)]| [[Project](https://www.sysu-hcp.net/projects/cv/111.html)] | [[Github](https://github.com/zjy526223908/DreamEditor)]|
|GaussianEditor <br><img src="assets/icon_text.png" width="20" height="20"> | GaussianEditor: Editing 3D Gaussians Delicately with Text Instructions| Arxiv 2023| [[Paper](https://arxiv.org/abs/2311.16037)]| [[Project](https://gaussianeditor.github.io/)] |  |
|3DFaceHybrid <br><img src="assets/icon_image.png" width="20" height="20"> | 3D Face Style Transfer with a Hybrid Solution of NeRF and Mesh Rasterization | WACV 2024 | [[Paper](https://openaccess.thecvf.com/content/WACV2024/html/Feng_3D_Face_Style_Transfer_With_a_Hybrid_Solution_of_NeRF_WACV_2024_paper.html)] | |  |
|NeRFEditor <br><img src="assets/icon_text.png" width="20" height="20"><img src="assets/icon_image.png" width="20" height="20"> | NeRFEditor: Differentiable Style Decomposition for 3D Scene Editing| WACV 2024 | [[Paper](https://arxiv.org/abs/2212.03848)] | [[Project](https://chuny1.github.io/NeRFEditor/nerfeditor.html)] |  |
|Free-Editor <br><img src="assets/icon_text.png" width="20" height="20"><img src="assets/icon_image.png" width="20" height="20"> | Free-Editor: Zero-shot Text-driven 3D Scene Editing | Arxiv 2023 | [[Paper](https://arxiv.org/abs/2312.13663)] | [[Project](https://free-editor.github.io/)] | |
|ED-NeRF <br><img src="assets/icon_text.png" width="20" height="20">|ED-NeRF: Efficient Text-Guided Editing of 3D Scene With Latent Space NeRF |ICLR2024 |[[Paper](https://openreview.net/forum?id=9DvDRTTdlu)] | |  |
<!--| | | | | |  | -->
<!--| |**Text-driven Stylization** | | | |  |-->

</details>

<details>
  <summary>
    
## Other Related 3D Generation
  </summary>
  
<div align=left> 
  Image guidance: <img align=top src="assets/icon_image.png" width="32" height="32"> 
  Text guidance: <img align=top src="assets/icon_text.png" width="32" height="32"> 
  3D guidance: <img align=top src="assets/icon_obj.png" width="32" height="32"> 
</div>

|  Abbr.  |  Title   | Venue  | Paper  | Project  | Github  |
|  ----  |  ----    | ----  |----   |----  |----  |
|CLIP-Mesh <br><img src="assets/icon_text.png" width="20" height="20">|CLIP-Mesh: Generating textured meshes from text using pretrained image-text models| SIGGRAPH Asia 2022 Conf Paper| [[Paper](https://arxiv.org/abs/2203.13333)]| [[Project](https://www.nasir.lol/clipmesh)]| [[Github](https://github.com/NasirKhalid24/CLIP-Mesh)]|
| DreamFusion <br><img src="assets/icon_text.png" width="20" height="20">| DreamFusion: Text-to-3D using 2D Diffusion | ICLR 2023 |[[Paper](https://arxiv.org/abs/2209.14988)] | [[Project](https://dreamfusion3d.github.io/)] | [[Github](https://github.com/ashawkey/stable-dreamfusion)]<br>(unofficial) |
|SJC <br><img src="assets/icon_text.png" width="20" height="20">| Score Jacobian Chaining: Lifting Pretrained 2D Diffusion Models for 3D Generation | CVPR 2023| [[Paper](https://arxiv.org/abs/2212.00774)]| [[Project](https://pals.ttic.edu/p/score-jacobian-chaining)]| [[Github](https://github.com/pals-ttic/sjc/)]|
|Magic3D <br><img src="assets/icon_text.png" width="20" height="20">|Magic3D: High-Resolution Text-to-3D Content Creation |CVPR 2023 |[[Paper](https://arxiv.org/abs/2211.10440)]|[[Project](https://research.nvidia.com/labs/dir/magic3d/)]||
|Fantasia3D <br><img src="assets/icon_text.png" width="20" height="20">|Fantasia3D: Disentangling Geometry and Appearance for High-quality Text-to-3D Content Creation |ICCV 2023 |[[Paper](https://arxiv.org/abs/2303.13873)]|[[Project](https://fantasia3d.github.io/)]|[[Github](https://github.com/Gorilla-Lab-SCUT/Fantasia3D)]|
|Zero-1-to-3 <br><img src="assets/icon_image.png" width="20" height="20"> |Zero-1-to-3: Zero-shot One Image to 3D Object| ICCV 2023| [[Paper](https://arxiv.org/abs/2303.11328)]|[[Project](https://zero123.cs.columbia.edu/)]| [[Github](https://github.com/cvlab-columbia/zero123)]|
|ProlificDreamer <br><img src="assets/icon_text.png" width="20" height="20">|ProlificDreamer: High-Fidelity and Diverse Text-to-3D Generation with Variational Score Distillation |NeurIPS 2023 |[[Paper](https://arxiv.org/abs/2305.16213)]|[[Project](https://ml.cs.tsinghua.edu.cn/prolificdreamer/)]|[[Github](https://github.com/thu-ml/prolificdreamer)]| 
|3D VADER <br><img src="assets/icon_text.png" width="20" height="20">|Autodecoding Latent 3D Diffusion Models |NeurIPS 2023 |[[Paper](https://arxiv.org/abs/2307.05445)]|[[Project](https://snap-research.github.io/3DVADER/)]|[[Github](https://github.com/snap-research/3DVADER)]|
|HiFA <br><img src="assets/icon_text.png" width="20" height="20">| HiFA: High-fidelity Text-to-3D with Advanced Diffusion Guidance | ICLR 2024 | [[Paper](https://arxiv.org/abs/2305.18766)]| [[Project](https://josephzhu.com/HiFA-site/)]| [[Github](https://github.com/JunzheJosephZhu/HiFA)]|
| DreamCraft3D <br><img src="assets/icon_text.png" width="20" height="20"> | DreamCraft3D: Hierarchical 3D Generation with Bootstrapped Diffusion Prior| ICLR 2024| [[Paper](https://arxiv.org/abs/2310.16818)] |[[Project](https://mrtornado24.github.io/DreamCraft3D/)] |  [[Github](https://github.com/deepseek-ai/DreamCraft3D)]| 
|DreamGaussian <br><img src="assets/icon_text.png" width="20" height="20"> | DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation | ICLR 2024| [[Paper](https://arxiv.org/abs/2309.16653)]| [[Project](https://dreamgaussian.github.io/)]| [[Github](https://github.com/dreamgaussian/dreamgaussian)]|

</details>

<details open>
  <summary>
    
## Other 3D Stylization
  </summary>
  
<div align=left> 
  Image guidance: <img align=top src="assets/icon_image.png" width="32" height="32"> 
  Text guidance: <img align=top src="assets/icon_text.png" width="32" height="32"> 
  3D guidance: <img align=top src="assets/icon_obj.png" width="32" height="32"> 
</div>

|  Abbr.  |  Title   | Venue  | Paper  | Project  | Github  |
|  ----  |  ----    | ----  |----   |----  |----  |
| StyleLit <br> <img align=top src="assets/icon_image.png" width="20" height="20"> |StyLit: Illumination-Guided Example-Based Stylization of 3D Renderings | SIGGRAPH 2016 | [[Paper](https://dcgi.fel.cvut.cz/home/sykorad/Fiser16-SIG.pdf)]| [[Project](https://dcgi.fel.cvut.cz/home/sykorad/stylit)] | [[Demo](http://stylit.org/)] |
| StyleBlit <br> <img align=top src="assets/icon_image.png" width="20" height="20"> |StyleBlit: Fast Example‐Based Stylization with Local Guidance | Computer Graphics Forum, EG 2019 | [[Paper](https://dcgi.fel.cvut.cz/home/sykorad/Sykora19-EG.pdf)]| [[Project](https://dcgi.fel.cvut.cz/home/sykorad/styleblit.html)] | [[Github](https://github.com/jamriska/styleblit)] <br> [[Unity Plugin](https://dcgi.fel.cvut.cz/home/sykorad/StyleBlit/unity_plugin.zip)]|
| StyleProp <br> <img align=top src="assets/icon_image.png" width="20" height="20">  | StyleProp: Real‐time Example‐based Stylization of 3D Models  | Computer Graphics Forum, PG 2020  | [[Paper](https://dcgi.fel.cvut.cz/home/sykorad/Hauptfleisch20-PG.pdf)]  | [[Project](https://dcgi.fel.cvut.cz/home/sykorad/styleprop.html)]  |  |
| Cubic Stylization <br> <img src="assets/icon_obj.png" width="20" height="20">  | Cubic Stylization   | SIGGRAPH Asia 2019  |[[Paper](https://arxiv.org/abs/1910.02926)]  | [[Project](https://www.dgp.toronto.edu/projects/cubic-stylization/)] |[[Github1](https://github.com/HTDerekLiu/CubicStylization_MATLAB)] <br>[[Github2](https://github.com/HTDerekLiu/CubicStylization_Cpp)]  |
|  Normal-Driven <br><img src="assets/icon_obj.png" width="20" height="20"> |  Normal‐Driven Spherical Shape Analogies |  Computer Graphics Forum, SGP 2021  | [[Paper](https://arxiv.org/abs/2104.11993)]  | [[Video](https://youtu.be/p4hLJ0xVGcM)] |[[Github1](https://github.com/HTDerekLiu/normal_driven_MATLAB)] <br>[[Github2](https://github.com/HTDerekLiu/normal_driven_cpp)] |
|Stroke Transfer <br> <img align=top src="assets/icon_image.png" width="20" height="20">  <img src="assets/icon_obj.png" width="20" height="20">|Stroke Transfer: Example-based Synthesis of Animatable Stroke Styles|SIGGRAPH 2022 Conf Paper| [[Paper](http://www.cg.it.aoyama.ac.jp/yonghao/sig22/StrokeTransfer.pdf)] |[[Project](http://www.cg.it.aoyama.ac.jp/yonghao/sig22/abstsig22.html)]| [[Github](https://github.com/AGU-Graphics/StrokeTransfer)]|
|  Stealth Shaper  | Stealth Shaper: Reflectivity Optimization as Surface Stylization    | SIGGRAPH 2023 Conf Paper| [[Paper](https://dl.acm.org/doi/10.1145/3588432.3591542)]  | [[Project](https://kenji-tojo.github.io/publications/stealthshaper/)]  | [[Github](https://github.com/kenji-tojo/stealth-shaper)]  |


</details>

## Mesh Stylization
**Neural 3D Mesh Renderer**<br>
*Hiroharu Kato, Yoshitaka Ushiku, Tatsuya Harada*<br>
CVPR 2018. [[Paper](https://arxiv.org/abs/1711.07566)][[Project](https://hiroharu-kato.com/assets/downloads/cvpr_2018_poster.pdf)] [[Github](https://github.com/hiroharu-kato/style_transfer_3d)]  <br>
_Features_:
- approximate gradient for rasterization
- single-image 3d mesh reconstruction with 2d supervision
- gradient-based 3d mesh editing including 2d->3d style transfer(image->mesh)


**Paparazzi: Surface Editing by way of Multi-View Image Processing**<br>
*Hsueh-Ti Derek Liu, Michael Tao, Alec Jacobson*<br>
SIGGRAPH Asia 2018.  [[Paper](https://www.dgp.toronto.edu/projects/paparazzi/paparazzi-surface-editing-by-way-of-multi-view-image-processing-siggraph-asia-2018-liu-et-al.pdf)]  [[Project](https://www.dgp.toronto.edu/projects/paparazzi/)]  [[Github](https://github.com/HTDerekLiu/Paparazzi)]  <br>
_Features_:
- image-guided mesh surface stylization
- vertex position optimization
- sample training cameras on the offset surface

**3DStyleNet: Creating 3D Shapes with Geometric and Texture Style**<br>
*Kangxue Yin, Jun Gao, Maria Shugrina, Sameh Khamis, Sanja Fidler*<br>
ICCV 2021. [[Paper](https://research.nvidia.com/labs/toronto-ai/3DStyleNet/assets/3dstyle-paper.pdf)]  [[Project](https://research.nvidia.com/labs/toronto-ai/3DStyleNet/)]  <br>
_Features_:
- 3D shape and texture style tranfer
- 3D textured model as guidance
- Large 3D data driven

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

**TANGO: Text-driven Photorealistic and Robust 3D Stylization via Lighting Decomposition** <br>
*Yongwei Chen, Rui Chen, Jiabao Lei, Yabin Zhang, Kui Jia*<br>
Neurips 2022. [[Paper](http://arxiv.org/abs/2210.11277)] [[Project](https://cyw-3d.github.io/tango/)] [[Github](https://github.com/Gorilla-Lab-SCUT/tango)] <br>

**Creative Birds: Self-Supervised Single-View 3D Style Transfer**<br>
*Renke Wang, Guimin Que, Shuo Chen, Xiang Li, Jun Li, Jian Yang* <br>
ICCV 2023. [[Paper](https://arxiv.org/abs/2307.14127)] [[Github](https://github.com/wrk226/creative_birds)]<br>

**Text2Scene: Text-Driven Indoor Scene Stylization With Part-Aware Details**<br>
*Inwoo Hwang, Hyeonwoo Kim, Young Min Kim*<br>
CVPR 2023. [[Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Hwang_Text2Scene_Text-Driven_Indoor_Scene_Stylization_With_Part-Aware_Details_CVPR_2023_paper.html)] [[Video](https://www.youtube.com/watch?v=CGIXY2kwIYM)] [[Github](https://github.com/uvavision/Text2Scene)] <br>

**TextDeformer: Geometry Manipulation using Text Guidance**<br>
*William Gao, Noam Aigerman, Thibault Groueix, Vladimir G. Kim, Rana Hanocka*<br>
SIGGRAPH Conference Proceedings 2023. [[Paper](https://arxiv.org/abs/2304.13348)]  [[Project](https://threedle.github.io/TextDeformer/)] [[Github](https://github.com/threedle/TextDeformer)] <br>

**TEXTure: Text-Guided Texturing of 3D Shapes**<br>
*Elad Richardson, Gal Metzer, Yuval Alaluf, Raja Giryes, Daniel Cohen-Or*<br>
SIGGRAPH Conference Proceedings 2023. [[Paper](https://arxiv.org/abs/2302.01721)]  [[Project](https://texturepaper.github.io/TEXTurePaper/)]  [[Github](https://github.com/TEXTurePaper/TEXTurePaper)] <br>

**Text2Tex: Text-driven Texture Synthesis via Diffusion Models**<br>
*Dave Zhenyu Chen, Yawar Siddiqui, Hsin-Ying Lee, Sergey Tulyakov, Matthias Nießner*<br>
ICCV 2023. [[Paper](https://daveredrum.github.io/Text2Tex/static/Text2Tex.pdf)]  [[Project](https://daveredrum.github.io/Text2Tex/)]  [[Github](https://github.com/daveredrum/Text2Tex)] <br>

**X-Mesh:Towards Fast and Accurate Text-driven 3D Stylization via Dynamic Textual Guidance**<br>
*Yiwei Ma, Xiaioqing Zhang, Xiaoshuai Sun, Jiayi Ji, Haowei Wang, Guannan Jiang, Weilin Zhuang, Rongrong Ji*<br>
ICCV 2023. [[Paper](https://arxiv.org/abs/2303.15764)]  [[Project](https://xmu-xiaoma666.github.io/Projects/X-Mesh/)]  [[Github](https://github.com/xmu-xiaoma666/X-Mesh)] <br>

## Volumetric Stylization
**Transport-Based Neural Style Transfer for Smoke Simulations**  <br>
*Byungsoo Kim, Vinicius C. Azevedo, Markus Gross, Barbara Solenthaler*<br>
SIGGRAPH Asia 2019.| [[Paper](http://arxiv.org/abs/1905.07442)]  [[Video](https://www.youtube.com/watch?v=67qVRhoOQPE)] [[Github](https://github.com/byungsook/neural-flow-style/tree/tnst)]  <br>
_Features_:
- dynamic smoke
- optimization-based stylization
 
**Lagrangian Neural Style Transfer for Fluids** <br>
*Byungsoo Kim, Vinicius C. Azevedo, Markus Gross, Barbara Solenthaler*<br>
SIGGRAPH 2020. [[Paper](http://arxiv.org/abs/2005.00803)]  [[Video](https://www.youtube.com/watch?v=WPmUsIVf3-4)] [[Github](https://github.com/byungsook/neural-flow-style/tree/lnst)]  <br>
_Features_:
- fluid
- optimization-based stylization
  
**Volumetric appearance stylization with stylizing kernel prediction network** <br>
*Jie Guo, Mengtian Li, Zijing Zong, Yuntao Liu, Jingwu He, Yanwen Guo, Ling-Qi Yan*<br>
SIGGRAPH 2021. [[Paper](https://sites.cs.ucsb.edu/~lingqi/publications/paper_volst.pdf))]  [[Video](https://dl.acm.org/doi/abs/10.1145/3450626.3459799)]|  <br>
_Features_:
- dynamic or static model
- arbitrary style transfer

**Efficient Neural Style Transfer For Volumetric Simulations**<br>
*Joshua Aurand, Raphaël Oritz, Sylvia Nauer, Vinicius Azevedo*<br>
ACM SIGGRAPH Asia, 2022. [[Paper](https://studios.disneyresearch.com/app/uploads/2022/10/Efficient-Neural-Style-Transfer-For-Volumetric-Simulations.pdf)][[Video](https://youtu.be/8tD5Yt3smDw)]<br>
_Features_:
- mainly for smoke
- view-independent stylization
- feed-forward network for acceleration


## Point Cloud Stylization
**PSNet: A Style Transfer Network for Point Cloud Stylization on Geometry and Color**<br>
*Xu Cao, Weimin Wang, Katashi Nagao, Ryosuke Nakamura*<br>
Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), 2020<br>
[[Paper](https://openaccess.thecvf.com/content_WACV_2020/html/Cao_PSNet_A_Style_Transfer_Network_for_Point_Cloud_Stylization_on_WACV_2020_paper.html)] [[Github](https://github.com/xucao-42/psnet)] [[Video](https://www.youtube.com/watch?v=EbUOg1gVcFw&t=1818s)]
_Features_:
- explicit point cloud stylization
- geometric and color stylization

## Novel View Stylization
### General Neural Rendering
**Learning to stylize novel views**<br>
*Hsin-Ping Huang, Hung-Yu Tseng, Saurabh Saini, Maneesh Singh, Ming-Hsuan Yang.* <br>
ICCV 2021. [[Paper](https://arxiv.org/abs/2105.13509)] [[Project](https://hhsinping.github.io/3d_scene_stylization/)] [[Github](https://github.com/hhsinping/stylescene)]  <br>
_Features_:
- Point-cloud based feature
- Style feature transformation
- Require MVS reconstruction, depth rendering


**3D Photo Stylization: Learning to Generate Stylized Novel Views from a Single Image**<br>
*Fangzhou Mu, Jian Wang, Yicheng Wu, Yin Li*<br>
CVPR 2022. [[Paper](https://arxiv.org/abs/2112.00169)] [[Project](https://pages.cs.wisc.edu/~fmu/style3d/)] [[Github](https://github.com/fmu2/3d_photo_stylization)]  <br>
_Features_:
- pre-trained NeRF with color prediction module replaced with a style network
- mutual learning for two parts mentioned above

**Artistic Style Novel View Synthesis Based on A Single Image**<br>
*Kuan-Wei Tseng, Yao-Chih Lee, Chu-Song Chen*<br>
CVPR Workshop 2022 / SIGGRAPH Poster 2022.[[Paper](https://openaccess.thecvf.com/content/CVPR2022W/CVFAD/papers/Tseng_Artistic_Style_Novel_View_Synthesis_Based_on_a_Single_Image_CVPRW_2022_paper.pdf)] [[Project](https://kuan-wei-tseng.github.io/ArtNV)] [[Github](https://github.com/Kuan-Wei-Tseng/ArtNV)] <br>
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

**Locally Stylized Neural Radiance Fields**<br>
*Hong-Wing Pang, Binh-Son Hua, Sai-Kit Yeung*<br>
ICCV 2023. [[Paper](https://arxiv.org/abs/2309.10684)]  [[Project](https://nerfstyle.hkustvgd.com/)] [[Github](https://github.com/hkust-vgd/nerfstyle)] <br>
_Features_:
- explicitly semantic match stylization
- based on instant-NGP
- room stylization

**Semantic-driven Image-based NeRF Editing with Prior-guided Editing Field**<br>
*Chong Bao, Yinda Zhang, Bangbang Yang, Tianxing Fan, Zesong Yang, Hujun Bao, Guofeng Zhang, Zhaopeng Cui*<br>
CVPR 2023. [[Paper](https://arxiv.org/abs/2303.13277)] [[Project](https://zju3dv.github.io/sine/)] [[Github](https://github.com/zju3dv/SINE)] <br>
_Features_:
- edit a photo-realistic NeRF with a single-view image or with text prompts
- cyclic constraints with a proxy mesh for geometric editing
- the color compositing mechanism to enhance texture editing
- feature-cluster-based regularization to control the affected editing area and maintain irrelevant parts unchanged
- 
**NeRF-Art: Text-Driven Neural Radiance Fields Stylization**<br>
*Can Wang, Ruixiang Jiang, Menglei Chai, Mingming He, Dongdong Chen, Jing Liao*<br>
TVCG 2023. [[Paper](https://arxiv.org/abs/2212.08070)] [[Project](https://cassiepython.github.io/nerfart/)] [[Github](https://github.com/cassiePython/NeRF-Art)] <br>
_Features_:
- combine CLIP[[Github](https://github.com/openai/CLIP)] with NeRF
- cover global structures and local details 
- adopt a weight regularization to effectively reduce cloudy artifacts and geometry noises

**Instruct-NeRF2NeRF: Editing 3D Scenes with Instructions**<br>
*Ayaan Haque, Matthew Tancik, Alexei A. Efros, Aleksander Holynski, Angjoo Kanazawa*<br>
ICCV 2023. [[Paper](https://arxiv.org/abs/2303.12789)] [[Project](https://instruct-nerf2nerf.github.io/)] [[Github](https://github.com/ayaanzhaque/instruct-nerf2nerf)] <br>
_Features_:
- extract shape and appearance priors from a 2D diffusion model
- edit input images and change 3d implicit field representation

**Blending-NeRF: Text-Driven Localized Editing in Neural Radiance Fields**<br>
ICCV 2023. [[Paper](https://arxiv.org/pdf/2308.11974)]  [[Project](https://seokhunchoi.github.io/Blending-NeRF/)] <br>
_Features_:
- text-guided local editing

<!--[[Paper]()] [[Project]()] [[Github]()] <br>-->
