# *-* coding: utf-8 *-*
# Author: kechavez
from __future__ import print_function
import pickle
import sys

"""
This file will use word-dictionary pair files to output a serialized dictionary.
User must ensure files are aligned prior to calling this script.

Usage: python serialize_word_def.py <words.txt> <definitions.txt> <out_file>
"""

if (len(sys.argv) % 2 != 0 and len(sys.argv) < 4):
  print("Usage: python serialize_word_def.py [pairs of <words.txt> <definitions.txt>] <out_file>")
  sys.exit()

out_file = sys.argv[-1]
word_def_dict = {}

for i in range(1, len(sys.argv)-1, 2):
  fwords = sys.argv[i]
  fdefs = sys.argv[i+1]
  with open(fwords, 'r') as fw, open (fdefs, 'r') as fd:
    for word in fw:
      d = fd.readline()
      word_def_dict[word.strip() \
                      .replace('–', '-') \
                      .replace('*', '') \
                      .replace('’', '\'')] = d.rstrip()

outf = open(out_file, 'wb')
pickle.dump(word_def_dict, outf)
outf.close()
