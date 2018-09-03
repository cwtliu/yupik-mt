python -m nmt.nmt \
  --src=ypk --tgt=en \
  --vocab_prefix=/home/yuarcuun/ypk-rulebased30k_eng-nltk/vocab \
  --train_prefix=/home/yuarcuun/ypk-rulebased30k_eng-nltk/train_parsed \
  --dev_prefix=/home/yuarcuun/ypk-rulebased30k_eng-nltk/dev_parsed \
  --test_prefix=/home/yuarcuun/ypk-rulebased30k_eng-nltk/test_parsed \
  --out_dir=/home/yuarcuun/ypk-rulebased30k_eng-nltk_output \
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
  --learning_rate=0.5 \
  --decay_scheme=luong234