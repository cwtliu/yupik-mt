#Author: cwtliu
#!/usr/bin/python
# -*- coding: utf-8

# parses the scraped data into verse per lines, used with parse_files_in_directory.sh to iterate over books
import io
import codecs
import unicodedata
import sys
import re
import argparse
reload(sys)
sys.setdefaultencoding('utf8')
parser = argparse.ArgumentParser(description='go')
parser.add_argument("--i", type=str, required=True)
parser.add_argument("--o", type=str, required=True)
arguments2 = parser.parse_args()
inputname = arguments2.i
outputname = arguments2.o
def convert(inputname,outputname):
    with codecs.open(inputname, encoding='utf-8') as fin:
        with open(outputname,'wt') as fout:
            for line in fin:
            	splitted = line.split()
            	for m in splitted:
            		if any(i.isdigit() for i in m):
            			if '(' in m or ')' in m:
            				fout.write(m)
            			else:
            				fout.write('\n')
            				fout.write(m)
                	else:
            			fout.write(' ')
            			fout.write(m)
convert(inputname,outputname)