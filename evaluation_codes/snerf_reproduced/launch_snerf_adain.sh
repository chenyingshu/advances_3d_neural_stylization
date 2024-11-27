# Assume you have reconstruct the scene 
ROUNDS=5
GPU=0
for (( ITER = 1; ITER <= $ROUNDS; ITER++ ))
do
let LASTI=ITER-1;
for i in {0...10}
do
	for j in Truck Playground 
	do
  		SCENE=${j}_iter${ITER}
		FOLDER=rgb
		DATATYPE=TanksAndTempleBG
		CONFIG=tnt_fixgeom
		# copy folder
		mkdir ../dataset/${DATATYPE}/AdaIN/
		mkdir ../dataset/${DATATYPE}/AdaIN/${SCENE}_$i
		scp -r ../dataset/${DATATYPE}/${j}/* ../dataset/${DATATYPE}/AdaIN/${SCENE}_${i}/

		# style transfer		
		cd ../../pytorch-AdaIN
		if  [[ ${ITER} -eq 1 ]]
		then
			CUDA_VISIBLE_DEVICES=${GPU} python test_snerf.py \
			--content_dir ../svox2/dataset/${DATATYPE}/${j}/${FOLDER} \
			--style ../svox2/dataset/styles/${i}.jpg \
			--decoder models/decoder.pth \
			--content_size 512 \
			--style_size 512 \
			--output ../svox2/dataset/${DATATYPE}/AdaIN/${SCENE}_${i}/${FOLDER} \
			--alpha 0.5
			
		else
			CUDA_VISIBLE_DEVICES=${GPU} python test_snerf.py \
			--content_dir ../svox2/opt/ckpt/AdaIN/${j}_iter${LASTI}_$i/train_renders \
			--style ../svox2/dataset/styles/${i}.jpg \
			--decoder models/decoder.pth \
			--content_size 512 \
			--style_size 512 \
			--output ../svox2/dataset/${DATATYPE}/AdaIN/${SCENE}_${i}/${FOLDER} \
			--alpha 0.5
		fi
		cd ../svox2/opt

		# reconstruction
		if  [[ ${ITER} -eq 1 ]]
		then
			CUDA_VISIBLE_DEVICES=${GPU} python opt.py \
			../dataset/${DATATYPE}/AdaIN/${SCENE}_$i \
			-c configs/${CONFIG}.json \
			--init_ckpt ckpt/TnT/${j}/ckpt.npz \
			-t ckpt/AdaIN/${SCENE}_$i
		else
			CKPT=ckpt/AdaIN/${j}_iter${LASTI}_$i/ckpt.npz
			CUDA_VISIBLE_DEVICES=${GPU} python opt.py \
			../dataset/${DATATYPE}/AdaIN/${SCENE}_$i \
			-c configs/${CONFIG}.json \
			--init_ckpt ${CKPT}  \
			-t ckpt/AdaIN/${SCENE}_$i
		fi

		CKPT=ckpt/AdaIN/${SCENE}_$i/ckpt.npz
		CUDA_VISIBLE_DEVICES=${GPU} python render_imgs.py \
		${CKPT} ../dataset/${DATATYPE}/$j \
		--train --no_lpips --no_vid

		CUDA_VISIBLE_DEVICES=${GPU} python render_imgs.py \
		${CKPT} ../dataset/${DATATYPE}/$j \
		--render_path --no_lpips 

	done


	for j in fern flower horns trex
	do
		SCENE=${j}_iter${ITER}
		FOLDER=images
		DATATYPE=nerf_llff_data
		CONFIG=llff_fixgeom
		# copy folder
		mkdir ../dataset/${DATATYPE}/AdaIN/
		mkdir ../dataset/${DATATYPE}/AdaIN/${SCENE}_$i
		scp -r ../dataset/${DATATYPE}/${j}/* ../dataset/${DATATYPE}/AdaIN/${SCENE}_${i}/

		# style transfer	
			# style transfer		
		cd ../../pytorch-AdaIN
		if  [[ ${ITER} -eq 1 ]]
		then
			CUDA_VISIBLE_DEVICES=${GPU} python test_snerf.py \
			--content_dir ../svox2/dataset/${DATATYPE}/${j}/${FOLDER} \
			--style ../svox2/dataset/styles/${i}.jpg \
			--decoder models/decoder.pth \
			--content_size 512 \
			--style_size 512 \
			--output ../svox2/dataset/${DATATYPE}/AdaIN/${SCENE}_${i}/${FOLDER} \
			--alpha 0.5 \
			--extra_output_dirs images_4,images_8
			
		else
			CUDA_VISIBLE_DEVICES=${GPU} python test_snerf.py \
			--content_dir ../svox2/opt/ckpt/AdaIN/${j}_iter${LASTI}_$i/train_renders \
			--style ../svox2/dataset/styles/${i}.jpg \
			--decoder models/decoder.pth \
			--content_size 512 \
			--style_size 512 \
			--output ../svox2/dataset/${DATATYPE}/AdaIN/${SCENE}_${i}/${FOLDER} \
			--alpha 0.5 \
			--extra_output_dirs images_4,images_8
		fi
		cd ../svox2/opt

		# reconstruction
		if  [[ ${ITER} -eq 1 ]]
		then
			CUDA_VISIBLE_DEVICES=${GPU} python opt.py \
			../dataset/${DATATYPE}/AdaIN/${SCENE}_$i \
			-c configs/${CONFIG}.json \
			--init_ckpt ../checkpoint/llff_c2f_fasttv_10e/$j/ckpt.npz \
			-t ckpt/AdaIN/${SCENE}_$i
		else
			CKPT=ckpt/AdaIN/${j}_iter${LASTI}_$i/ckpt.npz
			CUDA_VISIBLE_DEVICES=${GPU} python opt.py \
			../dataset/${DATATYPE}/AdaIN/${SCENE}_$i \
			-c configs/${CONFIG}.json \
			--init_ckpt ${CKPT}  \
			-t ckpt/AdaIN/${SCENE}_$i
		fi

		CKPT=ckpt/AdaIN/${SCENE}_$i/ckpt.npz
		CUDA_VISIBLE_DEVICES=${GPU} python render_imgs.py \
		${CKPT} ../dataset/${DATATYPE}/$j \
		--train --no_lpips --no_vid

		CUDA_VISIBLE_DEVICES=${GPU} python render_imgs.py \
		${CKPT} ../dataset/${DATATYPE}/$j \
		--render_path --no_lpips 

	done
	
	
done
done

