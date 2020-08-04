export CUDA_VISIBLE_DEVICES=0
python multi-run.py \
	--list /shared/xudongliu/code/semi-flow/hd3/lists/seg_track_val_new_5.txt \
	--root /data5/bdd100k/images/track/val \
	--out predictions/bdd-Sintel-val-5 \
	--model sintel
