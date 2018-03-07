from __future__ import print_function
import parser as yp
import sys
import pickle

'''
This script takes a yupik text, and does a rough translation using 
dictionary look ups. This loosely takes into account the ordering
author: kechavez '''

# ALL_ROOT_PKL_FILE = 'data/all_verbs_dict.pkl'
ALL_ROOT_PKL_FILE = '../data/all_bases.pkl'
ALL_PB_PKL_FILE = '../data/postbases_txt/all_postbases_dict.pkl'
# NOUN_ROOT_PKL_FILE = None
# VERB_ROOT_PKL_FILE = None
# NOUN_PB_PKL_FILE = None
# VERB_PB_PKL_FILE = None
END_PKL_FILE = '../data/endings/all_endings.pkl'

PLACEHOLDER = '%%' # if dictionary translation not found, tac this onto begin of word.

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

# retrieve dictionaries.
root_dict, pb_dict = None, None
# noun_root_dict, verb_root_dict = None, None
# noun_pb_dict, verb_pb_dict  = None, None
end_dict = None
with open(ALL_ROOT_PKL_FILE, 'rb') as rf, open(ALL_PB_PKL_FILE, 'rb') as pf, \
     open(END_PKL_FILE, 'rb') as ef:
     # open(NOUN_ROOT_PKL_FILE, 'rb') as nrf, open(VERB_ROOT_PKL_FILE, 'rb') as vrf, \
     # open(NOUN_PB_PKL_FILE, 'rb') as npf, open(VERB_PB_PKL_FILE, 'rb') as vpf, \
  root_dict, pb_dict = pickle.load(rf), pickle.load(pf)
  # noun_root_dict, verb_root_dict = pickle.load(nrf), pickle.load(vrf)
  # noun_pb_dict, verb_pb_dict = pickle.load(nrf), pickle.load(vrf)
  end_dict = pickle.load(ef)

# Process yupik lines.
yupik_word_lines = [l.split() for l in yupik_lines]
dirty_english_lines = []
yupik_parser = yp.DirtyParser(debug=False)
for line_idx in range(len(yupik_word_lines)):
  dirty_english = []
  # for word_idx in range(len(yupik_word_lines[line_idx])):
    # match = yupik_parser.parse(yupik_word_lines[line_idx][word_idx])
#TODO: UNDO DEBUG
  match = [yp.decrypt(w) +'\n' for w in yupik_word_lines[line_idx]]
  print('YUPIK WORD: ', match)
  
  root = root_dict[match[0]] if match[0] in root_dict else PLACEHOLDER + match[0]
  pbs = []
  end = []
  # The remaining morphemes must be postbases or an ending.
  for i in range(1, len(match)):
    if match[i] in pb_dict:
      pbs.append(pb_dict[match[i]])
    elif match[i] in end_dict:
      end.append(end_dict[match[i]])
    else:
      pbs.append(PLACEHOLDER)

  # end = end_dict[match[-1]] if match[-1] in end_dict else PLACEHOLDER + match[-1]
  # pbs = [pb_dict[pb] if pb in pb_dict else PLACEHOLDER + pb for pb in match[1:-1][::-1]]
  dirty_english.append(' '.join(end + pbs + [root]))
  print('TRANSLATION: ', dirty_english)

  dirty_english_lines.append(dirty_english)

print('output in ', dirty_english_txt)
# open(dirty_english_txt, 'w').writelines(dirty_english_lines)
# print(dirty_english_lines)

