/*********************** Comparison Slider *****************************/
/* Modified from
 https://medium.com/@predragdavidovic10/native-dual-range-slider-html-css-javascript-91e778134816
 https://www.codehim.com/html5-css3/html-css-image-comparison-slider/
 by Yingshu Chen
* */

/* the paper database */
const cardData = [

    {
        "title": "FlashTex: Fast Relightable Mesh Texturing with LightControlNet",
        "conference": "ECCV 2024(Oral)",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2402.13251",
            "code": "https://github.com/Roblox/FlashTex",
            "project": "https://flashtex.github.io/"
        }
    },
    {
        "title": "TexDreamer: Towards Zero-Shot High-Fidelity 3D Human Texture Generation",
        "conference": "ECCV 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2403.12906",
            "code": "https://github.com/ggxxii/texdreamer",
            "project": "https://ggxxii.github.io/texdreamer/"
        }
    },
    {
        "title": "Scene-Conditional 3D Object Stylization and Composition",
        "conference": "ECCV 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2312.12419",
            "project": "https://shallowtoil.github.io/scene-cond-3d/"
        }
    },
    {
        "title": "VCD-Texture: Variance Alignment based 3D-2D Co-Denoising for Text-Guided Texturing",
        "conference": "ECCV 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2407.04461"
        }
    },
    {
        "title": "Towards High-Quality 3D Motion Transfer with Realistic Apparel Animation",
        "conference": "ECCV 2024",
        "tags": [
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2407.11266",
            "code": "https://github.com/rongakowang/MMDMC"
        }
    },
    {
        "title": "StyleCity: Large-Scale 3D Urban Scenes Stylization",
        "conference": "ECCV 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2404.10681",
            "code": "https://github.com/chenyingshu/stylecity3d",
            "project": "https://chenyingshu.github.io/stylecity3d/"
        }
    },
    {
        "title": "Creating LEGO Figurines From Single Images",
        "conference": "SIGGRAPH 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://dl.acm.org/doi/10.1145/3658167"
        }
    },
    {
        "title": "Controllable Neural Style Transfer for Dynamic Meshes",
        "conference": "SIGGRAPH 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://dl.acm.org/doi/10.1145/3641519.3657474"
        }
    },
    {
        "title": "HeadArtist: Text-conditioned 3D Head Generation with Self Score Distillation",
        "conference": "SIGGRAPH 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2312.07539",
            "code": "https://github.com/KumapowerLIU/HeadArtist",
            "project": "https://kumapowerliu.github.io/HeadArtist/"
        }
    },
    {
        "title": "MaPa: Text-driven Photorealistic Material Painting for 3D Shapes",
        "conference": "SIGGRAPH 2024 Conf Paper",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2404.17569",
            "project": "https://zhanghe3z.github.io/MaPa/"
        }
    },
    {
        "title": "Diffusion Texture Painting",
        "conference": "SIGGRAPH 2024 Conf Paper",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://dl.acm.org/doi/10.1145/3641519.3657458",
            "code": "https://github.com/nv-tlabs/DiffusionTexturePainting",
            "project": "https://research.nvidia.com/labs/toronto-ai/DiffusionTexturePainting/"
        }
    },
    {
        "title": "TexPainter: Generative Mesh Texturing With Multi-view Consistency",
        "conference": "SIGGRAPH 2024 Conf Paper",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2406.18539",
            "code": "https://github.com/Quantuman134/TexPainter",
            "project": "https://quantuman134.github.io/"
        }
    },
    {
        "title": "DreamMat: High-quality PBR Material Generation With Geometry- and Light-aware Diffusion Models",
        "conference": "SIGGRAPH/TOG 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2405.17176",
            "code": "https://github.com/zzzyuqing/DreamMat",
            "project": "https://zzzyuqing.github.io/dreammat.github.io/"
        }
    },
    {
        "title": "EASI-Tex: Edge-Aware Mesh Texturing from Single Image",
        "conference": "SIGGRAPH/TOG 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2405.17393",
            "code": "https://github.com/sairajk/easi-tex",
            "project": "https://sairajk.github.io/easi-tex/"
        }
    },
    {
        "title": "Coin3D: Controllable and Interactive 3D Assets Generation With Proxy-guided Conditioning",
        "conference": "SIGGRAPH 2024 Conf Paper",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2405.08054",
            "code": "https://github.com/zju3dv/Coin3D",
            "project": "https://zju3dv.github.io/coin3d/"
        }
    },
    {
        "title": "ThemeStation: Generating Theme-Aware 3D Assets from Few Exemplars",
        "conference": "SIGGRAPH 2024 Conf Paper",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2403.15383",
            "code": "https://github.com/3DTopia/ThemeStation",
            "project": "https://3dthemestation.github.io/"
        }
    },
    {
        "title": "DressCode: Autoregressively Sewing and Generating Garments from Text Guidance",
        "conference": "SIGGRAPH/TOG 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2401.16465",
            "code": "https://github.com/IHe-KaiI/DressCode",
            "project": "https://ihe-kaii.github.io/DressCode/"
        }
    },
    {
        "title": "Mesh Neural Cellular Automata",
        "conference": "SIGGRAPH/TOG 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2311.02820",
            "code": "https://github.com/IVRL/MeshNCA",
            "project": "https://meshnca.github.io/"
        }
    },
    {
        "title": "Paint3D: Paint Anything 3D with Lighting-Less Texture Diffusion Models",
        "conference": "CVPR 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2312.13913",
            "code": "https://github.com/OpenTexture/Paint3D",
            "project": "https://paint3d.github.io/"
        }
    },
    {
        "title": "TextureDreamer: Image-guided Texture Synthesis through Geometry-aware Diffusion",
        "conference": "CVPR 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2401.09416",
            "project": "https://texturedreamer.github.io/"
        }
    },
    {
        "title": "TeMO: Towards Text-Driven 3D Stylization for Multi-Object Meshes",
        "conference": "CVPR 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2312.04248",
            "code": "https://github.com/zhangxuying1004/TeMO"
        }
    },
    {
        "title": "3D Paintbrush: Local Stylization of 3D Shapes with Cascaded Score Distillation",
        "conference": "CVPR 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2311.09571",
            "code": "https://github.com/threedle/3d-paintbrush",
            "project": "https://threedle.github.io/3d-paintbrush/"
        }
    },
    {
        "title": "As-Plausible-As-Possible: Plausibility-Aware Mesh Deformation Using 2D Diffusion Priors",
        "conference": "CVPR 2024",
        "tags": [
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://as-plausible-as-possible.github.io/static/APAP.pdf",
            "code": "https://github.com/KAIST-Visual-AI-Group/APAP",
            "project": "https://as-plausible-as-possible.github.io/"
        }
    },
    {
        "title": "SceneTex: High-Quality Texture Synthesis for Indoor Scenes via Diffusion Priors",
        "conference": "CVPR 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2311.17261",
            "code": "https://github.com/daveredrum/SceneTex",
            "project": "https://daveredrum.github.io/SceneTex/"
        }
    },
    {
        "title": "Paint-it: Text-to-Texture Synthesis via Deep Convolutional Texture Map Optimization and Physically-Based Rendering",
        "conference": "CVPR 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://kim-youwang.github.io/media/paint-it/paint-it.pdf",
            "code": "https://github.com/postech-ami/paint-it",
            "project": "https://kim-youwang.github.io/paint-it"
        }
    },
    {
        "title": "Dreaming Your Room Space with Text-Driven Panoramic Texture Propagation",
        "conference": "IEEE VR 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://ybbbbt.com/publication/dreamspace/media/DreamSpace.pdf",
            "code": "https://github.com/ybbbbt/dreamspace",
            "project": "https://ybbbbt.com/publication/dreamspace/"
        }
    },
    {
        "title": "TECA: Text-Guided Generation and Editing of Compositional 3D Avatars",
        "conference": "3DV 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2309.07125",
            "code": "https://github.com/HaoZhang990127/TECA",
            "project": "https://yfeng95.github.io/teca/"
        }
    },
    {
        "title": "StyleAvatar: Stylizing Animatable Head Avatars",
        "conference": "WACV 2024",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://openaccess.thecvf.com/content/WACV2024/papers/Perez_StyleAvatar_Stylizing_Animatable_Head_Avatars_WACV_2024_paper.pdf"
        }
    },
    {
        "title": "Text2Scene: Text-Driven Indoor Scene Stylization With Part-Aware Details",
        "conference": "CVPR 2023",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://openaccess.thecvf.com/content/CVPR2023/html/Hwang_Text2Scene_Text-Driven_Indoor_Scene_Stylization_With_Part-Aware_Details_CVPR_2023_paper.html",
            "project": "https://www.youtube.com/watch?v=CGIXY2kwIYM"
        }
    },
    {
        "title": "TextDeformer: Geometry Manipulation using Text Guidance",
        "conference": "SIGGRAPH 2023 Conf Paper",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2304.13348",
            "code": "https://github.com/threedle/TextDeformer",
            "project": "https://threedle.github.io/TextDeformer/"
        }
    },
    {
        "title": "TEXTure: Text-Guided Texturing of 3D Shapes",
        "conference": "SIGGRAPH 2023 Conf Paper",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2302.01721",
            "code": "https://github.com/TEXTurePaper/TEXTurePaper",
            "project": "https://texturepaper.github.io/TEXTurePaper/"
        }
    },
    {
        "title": "Creative Birds: Self-Supervised Single-View 3D Style Transfer",
        "conference": "ICCV 2023",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2307.14127",
            "code": "https://github.com/wrk226/creative_birds"
        }
    },
    {
        "title": "Text2Tex: Text-driven Texture Synthesis via Diffusion Models",
        "conference": "ICCV 2023",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://daveredrum.github.io/Text2Tex/static/Text2Tex.pdf",
            "code": "https://github.com/daveredrum/Text2Tex",
            "project": "https://daveredrum.github.io/Text2Tex/"
        }
    },
    {
        "title": "TexFusion: Synthesizing 3D Textures with Text-Guided Image Diffusion Models",
        "conference": "ICCV 2023",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://openaccess.thecvf.com//content/ICCV2023/papers/Cao_TexFusion_Synthesizing_3D_Textures_with_Text-Guided_Image_Diffusion_Models_ICCV_2023_paper.pdf",
            "project": "https://research.nvidia.com/labs/toronto-ai/publication/2023_iccv_texfusion/"
        }
    },
    {
        "title": "X-Mesh:Towards Fast and Accurate Text-driven 3D Stylization via Dynamic Textual Guidance",
        "conference": "ICCV 2023",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2303.15764",
            "code": "https://github.com/xmu-xiaoma666/X-Mesh",
            "project": "https://xmu-xiaoma666.github.io/Projects/X-Mesh/"
        }
    },
    {
        "title": "Texture Generation on 3D Meshes with Point-UV Diffusion",
        "conference": "ICCV 2023",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://cvmi-lab.github.io/Point-UV-Diffusion/paper/point_uv_diffusion.pdf",
            "code": "https://github.com/CVMI-Lab/Point-UV-Diffusion",
            "project": "https://cvmi-lab.github.io/Point-UV-Diffusion/"
        }
    },
    {
        "title": "3DStyle-Diffusion: Pursuing Fine-grained Text-driven 3D Stylization with 2D Diffusion Models",
        "conference": "ACM MM 2023",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2311.05464",
            "code": "https://github.com/yanghb22-fdu/3dstyle-diffusion-official"
        }
    },
    {
        "title": "RoomDreamer: Text-Driven 3D Indoor Scene Synthesis with Coherent Geometry and Texture",
        "conference": "ACM MM 2023",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2305.11337",
            "project": "https://youtu.be/p4xgwj4QJcQ"
        }
    },
    {
        "title": "Decorate3D: Text-Driven High-Quality Texture Generation for Mesh Decoration in the Wild",
        "conference": "NeurIPS 2023",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://decorate3d.github.io/Decorate3D/static/Decorate3D.pdf",
            "code": "https://github.com/Decorate3D/Decorate3D",
            "project": "https://decorate3d.github.io/Decorate3D/"
        }
    },
    {
        "title": "HyperDreamer: Hyper-Realistic 3D Content Generation and Editing from a Single Image",
        "conference": "SIGGRAPH Asia 2023 Conf Paper",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2312.04543",
            "code": "https://github.com/wutong16/HyperDreamer",
            "project": "https://ys-imtech.github.io/HyperDreamer/"
        }
    },
    {
        "title": "AlteredAvatar: Stylizing Dynamic 3D Avatars with Fast Style Adaptation",
        "conference": "Arxiv 2023",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2305.19245",
            "project": "https://alteredavatar.github.io/"
        }
    },
    {
        "title": "HeadSculpt: Crafting 3D Head Avatars with Text",
        "conference": "Neurips 2023",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2306.03038",
            "code": "https://github.com/BrandonHanx/HeadSculpt",
            "project": "https://brandonhan.uk/HeadSculpt/"
        }
    },
    {
        "title": "StyleMesh: Style Transfer for Indoor 3D Scene Reconstructions",
        "conference": "CVPR 2022",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2112.01530",
            "code": "https://github.com/lukasHoel/stylemesh",
            "project": "https://lukashoel.github.io/stylemesh/"
        }
    },
    {
        "title": "Latent-NeRF for Shape-Guided Generation of 3D Shapes and Textures",
        "conference": "CVPR 2022",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2211.07600",
            "code": "https://github.com/eladrich/latent-nerf",
            "project": "https://youtu.be/WwOXzWvGNdc"
        }
    },
    {
        "title": "Text2Mesh: Text-Driven Neural Stylization for Meshes",
        "conference": "CVPR 2022",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2112.03221",
            "code": "https://github.com/threedle/text2mesh",
            "project": "https://threedle.github.io/text2mesh/"
        }
    },
    {
        "title": "TANGO: Text-driven Photorealistic and Robust 3D Stylization via Lighting Decomposition",
        "conference": "NeurIPS 2022",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "http://arxiv.org/abs/2210.11277",
            "code": "https://github.com/Gorilla-Lab-SCUT/tango",
            "project": "https://cyw-3d.github.io/tango/"
        }
    },
    {
        "title": "CLIP-Mesh: Generating textured meshes from text using pretrained image-text models",
        "conference": "SIGGRAPH Asia 2022",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Text-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2203.13333",
            "code": "https://github.com/NasirKhalid24/CLIP-Mesh",
            "project": "https://www.nasir.lol/clipmesh"
        }
    },
    {
        "title": "3DStyleNet: Creating 3D Shapes with Geometric and Texture Style",
        "conference": "ICCV 2021",
        "tags": [
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://research.nvidia.com/labs/toronto-ai/3DStyleNet/assets/3dstyle-paper.pdf",
            "project": "https://research.nvidia.com/labs/toronto-ai/3DStyleNet/"
        }
    },
    {
        "title": "Deep Geometric Texture Synthesis",
        "conference": "SIGGRAPH 2020",
        "tags": [
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/2007.00074",
            "code": "https://github.com/amirhertz/geometric-textures",
            "project": "https://ranahanocka.github.io/geometric-textures/"
        }
    },
    {
        "title": "Paparazzi: Surface Editing by way of Multi-View Image Processing",
        "conference": "SIGGRAPH Asia 2018",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://www.dgp.toronto.edu/projects/paparazzi/paparazzi-surface-editing-by-way-of-multi-view-image-processing-siggraph-asia-2018-liu-et-al.pdf",
            "code": "https://github.com/HTDerekLiu/Paparazzi",
            "project": "https://www.dgp.toronto.edu/projects/paparazzi/"
        }
    },
    {
        "title": "Neural 3D Mesh Renderer",
        "conference": "CVPR 2018",
        "tags": [
            {
                "class": "btn-outline-success",
                "text": "Image-guided"
            },
            {
                "class": "btn-outline-primary",
                "text": "Mesh"
            }
        ],
        "links": {
            "paper": "https://arxiv.org/abs/1711.07566",
            "code": "https://github.com/hiroharu-kato/style_transfer_3d",
            "project": "https://hiroharu-kato.com/assets/downloads/cvpr_2018_poster.pdf"
        }
    }
    // Add more papers here...
];

$(document).ready(function () {
    // new Dics({
    //     container: document.querySelector("#disc-slider"),
    //     textPosition: "top"
    // });

    // Navbar
    let scrollerBlock = $("#navbarSection");
    let fromAbstract = document.querySelector('#tldr');

    $(window).scroll(function () {
        if ($(this).scrollTop() > fromAbstract.offsetTop) {
            scrollerBlock.fadeIn(400);
        } else {
            scrollerBlock.fadeOut(400);
        }
    });

    $(document).click(function (event) {
        var clickover = $(event.target);
        var $navbar = $(".navbar-collapse");
        var _opened = $navbar.hasClass("show");
        if (_opened === true && !clickover.hasClass("navbar-toggle")) {
            $navbar.collapse('hide');
        }
    });

    // Sliders
    const fromSlider = document.querySelector('#fromSlider');
    const toSlider = document.querySelector('#toSlider');
    // fillSlider(fromSlider, toSlider, '#C6C6C6', '#25daa5', toSlider);
    setToggleAccessible(toSlider);

    fromSlider.oninput = () => controlFromSlider(fromSlider, toSlider);
    toSlider.oninput = () => controlToSlider(fromSlider, toSlider);

    // Images (support three image now only)
    const imageCompIds = ['goldenComp', 'nightComp', 'milkywayComp'];
    imagesComp = [];
    for (let i = 0; i < imageCompIds.length; i++) {
        imagesComp.push(document.getElementById(imageCompIds[i]));
    }

});

function updateImages() {
    leftValue = fromSlider.value;
    rightValue = toSlider.value;
    // console.log("from:",leftValue);
    // console.log("to:",rightValue);
    imagesComp[0].style.clipPath = "polygon(0% 0%, " + leftValue + "% 0%, " + leftValue + "% 100%, 0% 100%)";
    imagesComp[1].style.clipPath = "polygon(0% 0%, " + rightValue + "% 0%, " + rightValue + "% 100%, 0% 100%)";
}

function controlFromSlider(fromSlider, toSlider) {
    const [from, to] = getParsed(fromSlider, toSlider);
    // fillSlider(fromSlider, toSlider, '#C6C6C6', '#25daa5', toSlider);
    if (from > to) {
        fromSlider.value = to;
    }
    updateImages();
}

function controlToSlider(fromSlider, toSlider) {
    const [from, to] = getParsed(fromSlider, toSlider);
    // fillSlider(fromSlider, toSlider, '#C6C6C6', '#25daa5', toSlider);
    setToggleAccessible(toSlider);
    if (from <= to) {
        toSlider.value = to;
    } else {
        toSlider.value = from;
    }
    updateImages();
}

function getParsed(currentFrom, currentTo) {
    const from = parseInt(currentFrom.value, 10);
    const to = parseInt(currentTo.value, 10);
    return [from, to];
}

function fillSlider(from, to, sliderColor, rangeColor, controlSlider) {
    const rangeDistance = to.max - to.min;
    const fromPosition = from.value - to.min;
    const toPosition = to.value - to.min;
    controlSlider.style.background = `linear-gradient(
      to right,
      ${sliderColor} 0%,
      ${sliderColor} ${(fromPosition) / (rangeDistance) * 100}%,
      ${rangeColor} ${((fromPosition) / (rangeDistance)) * 100}%,
      ${rangeColor} ${(toPosition) / (rangeDistance) * 100}%, 
      ${sliderColor} ${(toPosition) / (rangeDistance) * 100}%, 
      ${sliderColor} 100%)`;
}

function setToggleAccessible(currentTarget) {
    const toSlider = document.querySelector('#toSlider');
    if (Number(currentTarget.value) <= 0) {
        toSlider.style.zIndex = 2;
    } else {
        toSlider.style.zIndex = 0;
    }
}

function copyCitation() {
    /* Copy text into clipboard */
    text_data = document.getElementById('citationText').textContent;
    navigator.clipboard.writeText(text_data);
    var tooltip = document.getElementById("copyTooltip");
    tooltip.innerHTML = "Copied!";
}

function resetTooltip() {
    var tooltip = document.getElementById("copyTooltip");
    tooltip.innerHTML = "Copy";
}

document.addEventListener("DOMContentLoaded", function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

function createCard(card) {
    return `
    <div class="col mb-4">
      <div class="card h-100">
        <div class="card-body">
          <h6 class="card-title">${card.title}</h6>
          <p class="card-text">${card.conference}</p>
          ${card.tags.map(tag => `
            <button type="button" class="btn ${tag.class}" disabled>${tag.text}</button>
          `).join("")}
        </div>
        <div class="card-footer">
          ${Object.entries(card.links).map(([type, url]) => {
        let iconClass;
        switch (type) {
            case "paper":
                iconClass = "fas fa-file-alt";
                break;
            case "code":
                iconClass = "fab fa-github";
                break;
            case "project":
                iconClass = "fas fa-pager";
                break;
            default:
                iconClass = "";
        }
        return `
              <a href="${url}" class="figure-group-vertical" target="_blank" data-toggle="tooltip" title="View ${type.charAt(0).toUpperCase() + type.slice(1)}">
                <i class="${iconClass} figure-img logo-label"></i>
              </a>
            `;
    }).join("")}
        </div>
      </div>
    </div>
  `;
}

async function renderCards() {
    try {
        // Fetch the JSON file
        const response = await fetch('js/paper_data.json'); // Path to your JSON file
        if (!response.ok) {
            throw new Error('Failed to load card data');
        }

        // Parse the JSON data
        const cardData = await response.json();

        // Get the container element
        const container = document.querySelector(".row.row-cols-1.row-cols-md-3");
        if (!container) {
            console.error("Container element not found!");
            return;
        }

        // Clear the container
        container.innerHTML = "";

        // Get all active tags
        const activeTags = Array.from(document.querySelectorAll('.selector-container .btn[aria-pressed="true"]'))
            .map(button => button.textContent.trim()); // Get the text content of active buttons

        // If no tags are active, hide all items
        if (activeTags.length === 0) {
            return;
        }

        // Filter JSON items based on active tags
        const filteredCards = cardData.filter(card => {
            // Check if the card has tags that match all active tags
            return activeTags.every(activeTag =>
                card.tags.some(tag => tag.text === activeTag)
            );
        });

        // Render matching cards
        filteredCards.forEach(card => {
            const cardHtml = createCard(card);
            container.insertAdjacentHTML("beforeend", cardHtml);
        });

        // Initialize Bootstrap tooltips
        $(document).ready(function () {
            $('[data-toggle="tooltip"]').tooltip();
        });
    } catch (error) {
        console.error("Error loading or rendering cards:", error);
    }
}

// Function to add event listeners to buttons
function setupButtonListeners() {
    // Get all buttons under .selector-container
    const buttons = document.querySelectorAll('.selector-container .btn');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            // Get the parent group of the clicked button
            const parentGroup = button.closest('.button-group');

            // Check if the button belongs to the "3D Representation" or "Optimization Type" group
            const groupHeading = parentGroup.querySelector('h4').textContent.trim();
            const isSingleActiveGroup = groupHeading === '3D Representation' || groupHeading === 'Optimization Type';

            if (isSingleActiveGroup) {
                // Deactivate all other buttons in the same group
                parentGroup.querySelectorAll('.btn').forEach(otherButton => {
                    if (otherButton !== button) {
                        otherButton.setAttribute('aria-pressed', 'false');
                        otherButton.classList.remove('active'); // Remove the 'active' class for css
                    }
                });
            }

            // Toggle the clicked button's active state
            // const isPressed = button.getAttribute('aria-pressed') === 'true';
            // button.setAttribute('aria-pressed', !isPressed);

            // Toggle the 'active' class for the clicked button
            // button.classList.toggle('active', !isPressed);

            // Re-render cards based on the updated active tags
            renderCards();
        });
    });
}

document.addEventListener("DOMContentLoaded", function () {
    renderCards(cardData);
    // Initialize Bootstrap tooltips after the cards are rendered
    $(document).ready(function () {
        $('[data-toggle="tooltip"]').tooltip();
    });
    setupButtonListeners();
})


