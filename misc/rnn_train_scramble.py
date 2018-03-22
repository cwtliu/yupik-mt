from __future__ import print_function
import numpy as np
import parser.parser as yp

'''
author: kechavez
'''

yupik_scramble_name = \
  yupik_txt[:yupik_txt.find('.')] + '_scramble.txt' 
yupik_nonscramble_name = \
  yupik_txt[:yupik_txt.find('.')] + '_nonscramble.txt' 

# Read yupik book and grab words to scramble.
yupik_lines = None
with open(yupik_txt, 'r') as yb:
  yupik_lines = yb.readlines()

yupik_parser = yp.DirtyParser(debug=False)
yupik_scramble_lines = []
yupik_nonscramble_lines = []
for line in yupik_lines:
  for word in line:
    m = yupik_parser.parse(word)
    root, end= m[0], m[-1]
    yupik_nonscramble_lines.append(' '.join(m))
    yupik_scramble_lines.append(' '.join(root + list(np.random.permutation(m[1:-1])) + end))

open(yupik_scramble_name, 'w').writelines(yupik_scramble_name)
open(yupik_nonscramble_name, 'w').writelines(yupik_nonscramble_name)
