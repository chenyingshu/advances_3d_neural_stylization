BATCH=1
for j in chair_snerf
do

	for i in 3 14 17 19 71 122
	do
		python eval_style_loss.py \
		-i sample_data/image_dir/${j}_$i \
		-style sample_data/style_dir/${i}.jpg \
		-o logs/${j}_${i}_B${BATCH}.txt \
		--batch_size ${BATCH} \
		--image_size 256 \
		--gpu_ids 0
	done

done
