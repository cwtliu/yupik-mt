from __future__ import print_function
import sys

'''
This script moves splits postbases into noun or verb categories provided name and definitions files.
author: kechavez
'''

if len(sys.argv) != 3:
  print('Specify both postbase names and dictionary files')
  sys.exit()

f_pbs = sys.argv[1]
f_pbs_defs = sys.argv[2]
pbs = open(sys.argv[1]).readlines()
pb_defs = open(sys.argv[2]).readlines()

noun_pbs, verb_pbs  = [], []
noun_pbs_defs, verb_pbs_defs  = [], []

for i in range(len(pb_defs)):
  dsplit = pb_defs[i].split(';')
  nd = ';'.join([d for d in dsplit if d.find('N') != -1]).lstrip()
  vd = ';'.join([d for d in dsplit if d.find('V') != -1]).lstrip()
  if len(nd) > 0:
    noun_pbs.append(pbs[i])
    noun_pbs_defs.append(nd)

  if len(vd) > 0:
    verb_pbs.append(pbs[i])
    verb_pbs_defs.append(vd)

open(f_pbs[:f_pbs.find('.')] + '_noun.txt', 'w').writelines(noun_pbs)
open(f_pbs[:f_pbs.find('.')] + '_verb.txt', 'w').writelines(verb_pbs)
open(f_pbs[:f_pbs.find('.')] + '_noun_definitions.txt', 'w').writelines(noun_pbs_defs)
open(f_pbs[:f_pbs.find('.')] + '_verbs_definitions.txt', 'w').writelines(verb_pbs_defs)
