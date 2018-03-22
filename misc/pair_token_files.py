import sys

fname1 = sys.argv[1]
fname2 = sys.argv[2]
outname = sys.argv[3]

flines1, flines2 = [], []

with open(fname1,'r') as  f1, open(fname2,'r') as  f2:
 flines1,flines2 = f1.readlines(), f2.readlines()

outlines = [flines1[i].strip() + ' <ye>' + flines2[i][flines2[i].find('>')+1:] for i in range(len(flines1))]

open(outname, 'w').writelines(outlines)
