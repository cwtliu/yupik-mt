python -m nmt.nmt \
  --src=ypk --tgt=en \
  --vocab_prefix=/home/ubuntu/dataset_trun_stop_punc_sentence/vocab \
  --train_prefix=/home/ubuntu/dataset_trun_stop_punc_sentence/train_parsed \
  --dev_prefix=/home/ubuntu/dataset_trun_stop_punc_sentence/dev_parsed \
  --test_prefix=/home/ubuntu/dataset_trun_stop_punc_sentence/test_parsed \
  --out_dir=/home/ubuntu/parsed_dict_trun_model \
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
  --learning_rate=.5 \
  --decay_scheme=luong234 \
  --batch_size=128 \
  --infer_batch_size=8