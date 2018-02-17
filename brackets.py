# *-* encoding: utf-8 *-*
# Remove brackets from data.
# Usage: python brackets.py filename
# Author: Temigo
import re, sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    lines = f.readlines()

with open(filename + "_no_brackets", "w") as f:
    r = re.compile("[\{\}\[\]]+")
    for line in lines:
        m = r.split(line)
        if len(m)>=3:
            new_line = ""
            if len(m) > 3:
                print line
                print m
            for i in range(len(m)):
                if i%2==0:
                    new_line += m[i]
                elif len(m)%2 == 0 and i == len(m)-1:
                    new_line += m[i]
            f.write(new_line.replace('[', '').replace(']', ''))
        else:
            f.write(line.replace('[', '').replace(']', ''))
