python serialize_word_def.py \
	data/all_nouns_manually_edited.txt data/all_noun_definitions_manually_edited.txt \
	data/all_nouns_rootform_nodash.txt data/all_noun_definitions_manually_edited.txt \
	data/all_nouns_rootform.txt data/all_noun_definitions_manually_edited.txt \
	data/all_verbs_manually_edited_nodash.txt data/all_verbs_definitions_manually_edited.txt \
	data/all_verbs_manually_edited.txt data/all_verbs_definitions_manually_edited.txt data/bases.pkl
# python serialize_word_def.py data/all_bases.txt data/all_bases_definitions.txt data/bases.pkl
python serialize_word_def.py data/postbases_txt/all_postbases.txt data/postbases_txt/all_postbases_definitions.txt data/postbases_txt/postbases.pkl
python serialize_word_def.py data/endings.txt data/endings_definitions.txt data/endings/endings.pkl
