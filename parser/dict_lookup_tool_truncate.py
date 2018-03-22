from __future__ import print_function
import parser as yp
import sys
import pickle
import re
import string
from nltk.tokenize import word_tokenize

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

MORPHEME_DELIMITER = ' ' # ' ** ' 
WORD_DELIMITER = ' '# ' @@@ '
SPLIT_WORD_DELIMITER = ' @@@ '
PLACEHOLDER = '^' # '%%' # if dictionary translation not found, tac this onto begin of word.
# punc_re = re.compile('[%s]' % re.escape(string.punctuation))

root_dict, pb_dict = None, None
# noun_root_dict, verb_root_dict = None, None
# noun_pb_dict, verb_pb_dict  = None, None
end_dict = None

def add_delim(word, delim_type):
  if delim_type == 'word':
    return '<w> ' + word + ' </w>'
  elif delim_type == 'en':
    return '<e> ' + word + ' </e>'
  elif delim_type == 'ypk':
    return '<y> ' + word + ' </y>'
  elif delim_type == 'sentence':
    return '<s> ' + word + ' </s>'
  else:
    return word

def pair_word_def(word, d):
  return add_delim(word, 'ypk') + ' ' + add_delim(d, 'en')
         # add_delim(d, 'en') if d is not None else add(PLACEHOLDER, 'en')

def tokenize(s):
  return ' '.join(word_tokenize(s))

'''
pairing types: 'word', 'sentence'
'''
def dict_lookup(sentence, add_delims=False, pairing_type=None):
  dirty_english_sentence = []
  morphs = []

  for encoded_morphemes in sentence.split(SPLIT_WORD_DELIMITER):
    morphemes = [yp.deconvert(em).replace('–', '-') for em in encoded_morphemes.split()]
    if len(morphemes) > 0:
      morphemes = [m for m in morphemes if m not in string.punctuation]
    morphs.append(WORD_DELIMITER.join(morphemes))
 

  for encoded_morphemes in sentence.split(SPLIT_WORD_DELIMITER):
    root = []
    pbs = []
    end = []

    morphemes = [yp.deconvert(em).replace('–', '-') for em in encoded_morphemes.split()]
    
    # Set aside beginning and ending punctuation.
    # Middle punctuation is found in postbase list.
    # Remove punctuation. 
    if len(morphemes) > 0:
      morphemes = [m for m in morphemes if m not in string.punctuation]

    # Get root.
    definition_found = True
    if len(morphemes) > 0:
      if morphemes[0] in root_dict:
        root.append(root_dict[morphemes[0]])
      elif morphemes[0].strip('-') in root_dict:
        # TODO: Undo hardcoding of stripping '-' from roots found in the parsed file.
        root.append(root_dict[morphemes[0].strip('-')])
      elif morphemes[0] == 'maurluq*':
        # TODO: hardcoded definitions, again.
        root.append('grandmother')
      elif not pairing_type:
        root.append(PLACEHOLDER + morphemes[0])
      elif pairing_type != 'sentence':
        root.append(PLACEHOLDER)

    # word-definition pairing.
    if pairing_type == 'word' and len(morphemes) > 0:
      root[0] = pair_word_def(morphemes[0], tokenize(root[0]))
    if pairing_type == 'sentence' and len(morphemes) > 0 and len(root) > 0:
      root[0] = WORD_DELIMITER.join([r for r in word_tokenize(root[0]) if r not in string.punctuation])

    # Get postbases and ending.
    definition_found = True
    if len(morphemes) > 1:
      for morpheme in morphemes[1:]:
        # TODO: Hardcoded backwardslash replacement.
        morph = morpheme.replace('\\','-').strip().rstrip()
        skip = morph == SPLIT_WORD_DELIMITER.rstrip().strip()
        if not skip:
          if morph in string.punctuation:
            root.append(morph)
            # pbs.append(morph)
          elif morph in pb_dict:
            # pbs.append(pb_dict[morph])
            root.append(pb_dict[morph])
          elif '=' + morph in pb_dict:
            # TODO: Undo hardcode of adding '=' at beginning.
            root.append(pb_dict['=' +  morph])
            # pbs.append(pb_dict['=' +  morph])
          elif '=' + morph[1:] in pb_dict:
            # TODO: Undo hardcode of replacing '=' with ''
            # pbs.append(pb_dict['=' + morph[1:]])
            root.append(pb_dict['=' + morph[1:]])
          elif morph in end_dict:
            # end.append(end_dict[morph])
            root.append(end_dict[morph])
          elif morph == '@~-ke-':
            # TODO: Undo hardcoding definitino for this special case.
            root.append('the one or ones that the possessor is V-ing')
          elif morph == 'maurluq*':
            # TODO: hardcoded definitions, again.
            root.append('grandmother')
          elif morph == 'nek':
            # TODO: hardcoded definitions, again.
            root.append('many N')
          elif morph == 'nun':
            # TODO: hardcoded definitions, again.
            root.append('toward N')
          elif morph == 'mek':
            # TODO: hardcoded definitions, again.
            root.append('one N')
          elif morph == 'riit':
            # TODO: hardcoded definitions, again.
            root.append('the many N')
          elif '-llu' in morph and len(morph) <= len('xxx-llu'):
            # TODO: hardcoded definitions, again.
            root.append(pb_dict['=llu'])
          elif morph == 'mun':
            # TODO: hardcoded definitions, again.
            root.append('toward N')
          elif not pairing_type:
            root.append(PLACEHOLDER + morph)
          elif pairing_type == 'word':
            root.append(PLACEHOLDER)

          # word-definition pairing.
          if pairing_type == 'word':
            root[-1] = pair_word_def(morph, tokenize(root[-1]))
          elif pairing_type == 'sentence' and len(root) > 0:
            root[-1] = WORD_DELIMITER.join([r for r in word_tokenize(root[-1]) if r not in string.punctuation])

    # dirty_english_sentence.append(MORPHEME_DELIMITER.join(beg_punc + end + pbs + root + end_punc))
    dirty_english_sentence.append(MORPHEME_DELIMITER.join(root))

  if pairing_type != 'sentence':
    return WORD_DELIMITER.join(dirty_english_sentence)

  return WORD_DELIMITER.join(morphs) + '<ye> ' + WORD_DELIMITER.join(dirty_english_sentence)

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
    print('Specify file for dictionary lookup processing.')
    sys.exit()

  yupik_txt = sys.argv[1]
  dirty_english_txt = \
    yupik_txt[:yupik_txt.find('.')].replace('yupik','english') \
    + '_dirty_translation' + yupik_txt[yupik_txt.find('.'):]
  yupik_lines = None

  # Retrieve yupik book lines.
  with open(yupik_txt, 'r') as yf:
    yupik_lines = yf.readlines()

  retrieve_dicts()

  # Process yupik lines.
  dirty_english_lines = []
  for line in yupik_lines[:-1]:
    print('ENCODED YUPIK MORPHEMES:', line)
    dirty_english = dict_lookup(line, add_delims=False, pairing_type='sentence')
    print('TRANSLATION: ', dirty_english, '\n\n')
    # dirty_english_lines.append(WORD_DELIMITER.join(dirty_english))
    dirty_english_lines.append(dirty_english+'\n')
  dirty_english_lines.append(dict_lookup(yupik_lines[-1], add_delims=False, pairing_type='sentence'))

  print('output in ', dirty_english_txt)
  open(dirty_english_txt, 'w').writelines(dirty_english_lines)
