from __future__ import print_function
from enchant import Dict
from enchant.tokenize import get_tokenizer 
import sys


"""
This script will read a text file and output where non-english words occur.
Usage: python nonwords.py <file.txt>
"""

if (len(sys.argv) != 2):
  print("Usage: python nonwords.py <file.txt>")
  sys.exit()

fname = sys.argv[1]

word_lines = [] # List of (word, line) tuples.
en_dict = Dict("en_US")
en_tokenizer = get_tokenizer("en_US")
line_num = 0

with open(fname, 'r') as f:
  for line in f:
    # Note: might conisder making this a list of corrections.
    pline = line.replace("’", "'") # Remove special character.
    pline = pline.replace("ﬁ", "f") # Remove special character.

    invalid_words = [iword[0] for iword in en_tokenizer(pline) \
                      if not en_dict.check(iword[0])] 

    # Stream output to stdout.
    if len(invalid_words) != 0:
      word_lines.append((invalid_words, line_num))
      print("Invalids words found in line ", line_num, ":", invalid_words)

    line_num += 1

