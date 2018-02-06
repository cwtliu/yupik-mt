# Author: kechavez
from __future__ import print_function
from enchant import Dict
from enchant.tokenize import get_tokenizer 
import sys


"""
This script makes small corrections to a text file and outputs suggestions for
misspellings.
Usage: python nonwords.py <file.txt>
options: --list_recs, to list recommended fixes.
"""

if not (1 < len(sys.argv) < 4):
  print("Usage: python nonwords.py [--list_recs] <file.txt>")
  sys.exit()

list_recs = False
if len(sys.argv) == 3 and (sys.argv[1] == "--list_recs"):
  list_recs = True
  
fname = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1]

# List of common incorrect spellings and associated corrections to perform
# auto-correct with.
auto_corrections = [("’", "'"), ("ﬁ", "fi"), ("ﬂ", "fl")]

en_dict = Dict("en_US")
en_tokenizer = get_tokenizer("en_US")
line_num = 1

ilines = open(fname, 'r').readlines()

invalid_words = []
olines = []

for iline in ilines:
  # Perform auto-correction in place.
  oline = iline
  for correction in auto_corrections:
    oline = oline.replace(*correction)
  olines.append(oline)

  invalid_words.append((line_num, [iword[0] for iword in en_tokenizer(oline) \
                    if not en_dict.check(iword[0])]))

  line_num += 1

open(fname + '.corrected', 'w').writelines(olines)
print('****************NOTE****************')
print("See autocorrections in file " + fname + ".corrected")
print('************************************')

for ln, iws in invalid_words:
  # Stream invalid words to stdout.
  if len(iws) != 0:
    print("Invalids words found in line ", ln, ":", iws)

    if (list_recs):
      recs = [en_dict.suggest(iw)[0] if len(en_dict.suggest(iw)) > 0 else "_" \
                for iw in iws]
      print("\trecommendations: ", recs)


