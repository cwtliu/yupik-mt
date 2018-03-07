from __future__ import print_function
import parser as yp
import sys
import pickle
import re
import string

'''
This script takes a yupik text, and does a rough translation using 
dictionary look ups. This loosely takes into account the ordering
author: kechavez '''

# ALL_ROOT_PKL_FILE = 'data/all_verbs_dict.pkl'
ALL_ROOT_PKL_FILE = '../data/bases.pkl'
ALL_PB_PKL_FILE = '../data/postbases_txt/postbases.pkl'
# NOUN_ROOT_PKL_FILE = None
# VERB_ROOT_PKL_FILE = None
# NOUN_PB_PKL_FILE = None
# VERB_PB_PKL_FILE = None
END_PKL_FILE = '../data/endings/endings.pkl'

MORPHEME_DELIMITER = ' ** ' 
WORD_DELIMITER = ' || '
PLACEHOLDER = '%%' # if dictionary translation not found, tac this onto begin of word.
# punc_re = re.compile('[%s]' % re.escape(string.punctuation))

root_dict, pb_dict = None, None
# noun_root_dict, verb_root_dict = None, None
# noun_pb_dict, verb_pb_dict  = None, None
end_dict = None

def dict_lookup(sentence):
  dirty_english_sentence = []
  for encoded_morphemes in sentence.split(WORD_DELIMITER):
    beg_punc = []
    end_punc = []
    root = None
    pbs = []
    end = []

    morphemes = [yp.deconvert(em) for em in encoded_morphemes.split()]
    
    # Set aside beginning and ending punctuation.
    # Middle punctuation is found in postbase list.
    b = 0
    while morphemes[b] in string.punctuation:
      beg_punc.append(morphemes[b])
      b += 1
    morphemes = morphemes[b:]
    e = len(morphemes) - 1
    while morphemes[e] in string.punctuation:
      end_punc.append(morphemes[e])
      e -= 1
    morphemes = morphemes[:e+1]

    # Get root.
    root = root_dict[morphemes[0]] \
            if morphemes[0] in root_dict else PLACEHOLDER + morphemes[0]

    # Get postbases and ending.
    if len(morphemes) > 1:
      for morpheme in morphemes[1:]:
        if morpheme in string.punctuation:
          pbs.append(morpheme)
        elif morpheme in pb_dict:
          pbs.append(pb_dict[morpheme])
        elif morpheme in end_dict:
          end.append(end_dict[morpheme])
        else:
          pbs.append(PLACEHOLDER + morpheme)

    dirty_english_sentence.append(MORPHEME_DELIMITER.join(beg_punc + end + pbs + [root] + end_punc))

  return WORD_DELIMITER.join(dirty_english_sentence)

def retrieve_dicts():
  global root_dict, pb_dict, end_dict
  with open(ALL_ROOT_PKL_FILE, 'rb') as rf, open(ALL_PB_PKL_FILE, 'rb') as pf, \
       open(END_PKL_FILE, 'rb') as ef:
       # open(NOUN_ROOT_PKL_FILE, 'rb') as nrf, open(VERB_ROOT_PKL_FILE, 'rb') as vrf, \
       # open(NOUN_PB_PKL_FILE, 'rb') as npf, open(VERB_PB_PKL_FILE, 'rb') as vpf, \
    root_dict, pb_dict = pickle.load(rf), pickle.load(pf)
    # noun_root_dict, verb_root_dict = pickle.load(nrf), pickle.load(vrf)
    # noun_pb_dict, verb_pb_dict = pickle.load(nrf), pickle.load(vrf)
    end_dict = pickle.load(ef)

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Specify both postbase names and dictionary files')
    sys.exit()

  yupik_txt = sys.argv[1]
  dirty_english_txt = \
    yupik_txt[:yupik_txt.find('.')].replace('yupik','english') + '_dirty_translation.txt' 
  yupik_lines = None

  # Retrieve yupik book lines.
  with open(yupik_txt, 'r') as yf:
    yupik_lines = yf.readlines()

  retrieve_dicts()

  # Process yupik lines.
  dirty_english_lines = []
  for line in yupik_lines:
    print('ENCODED YUPIK MORPHEMES:', line)
    dirty_english = dict_lookup(line)
    print('TRANSLATION: ', dirty_english, '\n\n')
    # dirty_english_lines.append(WORD_DELIMITER.join(dirty_english))
    dirty_english_lines.append(dirty_english+'\n')

  print('output in ', dirty_english_txt)
  open(dirty_english_txt, 'w').writelines(dirty_english_lines)
