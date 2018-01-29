# *-* encoding: utf-8 *-*
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
os.system("pdf2txt.py -t xml -c utf-8 %s.pdf > %s.xml" % (filename, filename))
f = open('%s.xml' % filename, 'r')

soup = BeautifulSoup(f, 'lxml')

nouns = []
verbs = []
nouns_definitions = []
verbs_definitions = []

s = ""
d = ""
definitions = {}
words = []
current = False
for textline in soup.find_all("textline"):
    for text in textline.find_all("text"):
        if "font" in text.attrs and re.search("Bold|1-0|5-0", text['font']) or (',' in text.string and current):
            # Remove headlines
            if "size" in text.attrs and float(text.attrs["size"]) < 17:
                if len(d.strip()): # entry that didn't finish with '#'
                    if len(d.strip()) > 1:
                        definitions[s] = d
                        words.append(s)
                        s = ""
                        d = ""
                    elif current:
                        s += d
                        d = ""
                current = True
                s+= text.string
        elif re.search("#", text.string):
            # Register d and reset it
            current = False
            definitions[s] = d
            words.append(s)
            s = ""
            d = ""
        else:
            if len(s) and current:
                d += text.string

for s in words:
    if len(s) > 1 and s.find(u'—') == -1:
        d = definitions[s].lstrip().rstrip()
        d = re.sub('\n|\r', '', d)
        for w in s.split(","):
            # Replace special characters
            w = w.replace(u'\u00F7', u'\u0144') # division to n acute
            w = w.replace(u'\u00B5', u'\u1E3F') # micro to m acute
            w = w.replace('TMg', u'\u0144g')# ng acute
            # Ligatures : leave them with ¥ symbol
            #w = w.replace(u'\u00A5g', u'\u011D') # ¥g to ug ligature (g circonflex)
            #w = w.replace(u'\u00A5q', u'\u')# ur ligature
            # urr ligature
            # Remove digits
            w = ''.join([i for i in w if not i.isdigit()])
            # Remove whitespaces
            w = w.replace(' ', '')
            if len(w) > 1:
                if w.find('-') == -1:
                    if w not in nouns:
                        nouns.append(w)
                        nouns_definitions.append(d)
                else:
                    if w not in verbs:
                        verbs.append(w)
                        verbs_definitions.append(d)
f.close()

writeListToFile(nouns, '%s.nouns.txt' % filename)
writeListToFile(nouns_definitions, '%s.nouns.definitions.txt' % filename)
writeListToFile(verbs, '%s.verbs.txt' % filename)
writeListToFile(verbs_definitions, '%s.verbs.definitions.txt' % filename)
