# Parser for Yup'ik -> English PDF dictionary
#
# Usage : python parse_dict.py filename.pdf
# Requires PDFMiner python module and its pdf2txt.py tool.
#
# Used with Yup'ik Eskimo Dictionary, 2nd edition. Jacobson, Steven A. 2012
# Original dictionary can be found at
# http://www.uaf.edu/anla/collections/search/resultDetail.xml

from bs4 import BeautifulSoup
import re
import sys, os
from utils import writeListToFile

# Open PDF file
if len(sys.argv) < 2:
    print "Usage : python parse_postbases.py filename.pdf"
filename = os.path.splitext(sys.argv[1])[0]
os.system("pdf2txt.py -t xml %s.pdf > %s.xml" % (filename, filename))
f = open('%s.xml' % filename, 'r')

soup = BeautifulSoup(f, 'lxml')

nouns = []
verbs = []

for textline in soup.find_all("textline"):
    s = ""
    for text in textline.find_all(font=re.compile("Bold")):
        s += text.string
    if len(s) > 0 and s.find(u'—') == -1:
        for w in s.split(","):
            # Remove digits
            w = ''.join([i for i in w if not i.isdigit()])
            # Remove whitespaces
            w = w.strip()
            if w.find('-') == -1:
                if w not in nouns: nouns.append(w)
            else:
                if w not in verbs: verbs.append(w)
f.close()

writeListToFile(nouns, '%s.nouns.txt' % filename)
writeListToFile(verbs, '%s.verbs.txt' % filename)