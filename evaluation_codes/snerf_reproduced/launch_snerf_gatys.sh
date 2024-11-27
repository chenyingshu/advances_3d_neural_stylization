# Assume you have reconstruct the scene
ROUNDS=5
GPU=1
for (( ITER = 1; ITER <= $ROUNDS; ITER++ ))
do
let LASTI=ITER-1;
for i in {0...10}
do
	for j in chair mic
	do  
		SCENE=${j}_iter${ITER}
		FOLDER=train
		DATATYPE=nerf_synthetic
		CONFIG=syn_fixgeom
		# copy folder
		mkdir ../dataset/${DATATYPE}/Gatys/
		mkdir ../dataset/${DATATYPE}/Gatys/${SCENE}_$i
		scp -r ../dataset/${DATATYPE}/${j}/* ../dataset/${DATATYPE}/Gatys/${SCENE}_${i}/
	

		# style transfer		
		if  [[ ${ITER} -eq 1 ]]; then
			CUDA_VISIBLE_DEVICES=${GPU} python neural_style_transfer.py \
			--content_dir ../dataset/${DATATYPE}/${j}/${FOLDER} \
			--style ../dataset/styles/${i}.jpg \
			--output_dir ../dataset/${DATATYPE}/Gatys/${SCENE}_${i}/${FOLDER}
		else
			CUDA_VISIBLE_DEVICES=${GPU} python neural_style_transfer.py \
			--content_dir ckpt/Gatys/${j}_iter${LASTI}_$i/train_renders_blackbg \
			--style ../dataset/styles/${i}.jpg \
			--output_dir ../dataset/${DATATYPE}/Gatys/${SCENE}_${i}/${FOLDER}
		fi

		# reconstruction
		if  [[ ${ITER} -eq 1 ]]
		then
			CUDA_VISIBLE_DEVICES=${GPU} python opt.py \
			../dataset/${DATATYPE}/Gatys/${SCENE}_$i \
			-c configs/${CONFIG}.json \
			--init_ckpt ../checkpoint/syn_256_to_512_fasttv/$j/ckpt.npz \
			-t ckpt/Gatys/${SCENE}_$i
		else
			CKPT=ckpt/Gatys/${j}_iter${LASTI}_$i/ckpt.npz
			CUDA_VISIBLE_DEVICES=${GPU} python opt.py \
			../dataset/${DATATYPE}/Gatys/${SCENE}_$i \
			-c configs/${CONFIG}.json \
			--init_ckpt ${CKPT}  \
			-t ckpt/Gatys/${SCENE}_$i
		fi


		CKPT=ckpt/Gatys/${SCENE}_$i/ckpt.npz
		CUDA_VISIBLE_DEVICES=${GPU} python render_imgs.py \
		${CKPT} ../dataset/${DATATYPE}/$j \
		--train --no_lpips --no_vid --blackbg

		CUDA_VISIBLE_DEVICES=${GPU} python render_imgs.py \
		${CKPT} ../dataset/${DATATYPE}/$j \
		--render_path --no_lpips 
	done
	
done
done

