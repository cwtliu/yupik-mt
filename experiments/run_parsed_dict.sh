python -m nmt.nmt \
  --src=ypk --tgt=en \
  --vocab_prefix=/home/ubuntu/parsed_dataset/vocab \
  --train_prefix=/home/ubuntu/parsed_dataset/train_parsed \
  --dev_prefix=/home/ubuntu/parsed_dataset/dev_parsed \
  --test_prefix=/home/ubuntu/parsed_dataset/test_parsed \
  --out_dir=/home/ubuntu/parsed_dict_model \
  --num_train_steps=100000 \
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