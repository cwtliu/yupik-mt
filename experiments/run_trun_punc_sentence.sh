python -m nmt.nmt \
  --src=ypk --tgt=en \
  --vocab_prefix=/home/yuarcuun/trun_punc_sentence/vocab \
  --train_prefix=/home/yuarcuun/trun_punc_sentence/train \
  --dev_prefix=/home/yuarcuun/trun_punc_sentence/dev \
  --test_prefix=/home/yuarcuun/trun_punc_sentence/test \
  --out_dir=/home/yuarcuun/trun_punc_sentence_output_infer8 \
  --num_train_steps=80000 \
  --steps_per_stats=100 \
  --num_layers=2 \
  --num_units=128 \
  --dropout=0.2 \
  --metrics=bleu \
  --attention=scaled_luong \
  --attention_architecture=standard \
  --encoder_type=bi \
  --unit_type=lstm \
  --infer_batch_size=8 \
  --batch_size=128 \
  --learning_rate=0.5 \
  --decay_scheme=luong234
