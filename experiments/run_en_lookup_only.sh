python -m nmt.nmt \
  --src=ypk --tgt=en \
  --vocab_prefix=/home/ubuntu/baseline_dataset_noemptylines_tokens/vocab \
  --train_prefix=/home/ubuntu/baseline_dataset_noemptylines_tokens/train \
  --dev_prefix=/home/ubuntu/baseline_dataset_noemptylines_tokens/dev \
  --test_prefix=/home/ubuntu/baseline_dataset_noemptylines_tokens/test \
  --out_dir=/home/ubuntu/model_many_hp1 \
  --num_train_steps=50000 \
  --steps_per_stats=100 \
  --num_layers=2 \
  --num_units=128 \
  --dropout=0.2 \
  --metrics=bleu \
  --attention=scaled_luong \
  --attention_architecture=standard \
  --encoder_type=bi \
  --unit_type=lstm \
  --learning_rate=1.0 \
  --decay_scheme=luong234
