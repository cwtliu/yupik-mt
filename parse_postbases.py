# Parser for Yup'ik -> English PDF postbases dictionary
#
# Usage : python parse_postbases.py filename.pdf
# Requires PDFMiner python module and its pdf2txt.py tool.
#
# Used with Yup'ik Eskimo Dictionary, 2nd edition. Jacobson, Steven A. 2012
# Original dictionary can be found at
# http://www.uaf.edu/anla/collections/search/resultDetail.xml

from bs4 import BeautifulSoup
import re
import sys, os
from utils import writeListToFile, replaceSpecialCharacters

# Open PDF file
if len(sys.argv) < 2:
    print "Usage : python parse_postbases.py filename.pdf"
filename = os.path.splitext(sys.argv[1])[0]
os.system("pdf2txt.py -t xml %s.pdf > %s.xml" % (filename, filename))
f = open('%s.xml' % filename, 'r')

soup = BeautifulSoup(f, 'lxml')
xmins = []
ymaxs = []

for textline in soup.find_all("textline"):
    s = ""
    for text in textline.find_all("text"):
        if 'bbox' in text.attrs :
            xmin, ymin, xmax, ymax = text['bbox'].split(',')
            xmins.append(float(xmin))
            ymaxs.append(float(ymax))

# In case a headline has the minimal x, restrict the min operation to suitable y
y0 = max(ymaxs)
x0 = min([xmins[i] for i in range(len(xmins)) if ymaxs[i] < y0 - 30])
postbases = []
postbases_definitions = []

s = ""
d = ""
definitions = {}
words = []
current = False

for textline in soup.find_all("textline"):
    take = False
    for text in textline.find_all("text"):
        if 'bbox' in text.attrs and not re.search("{", text.string):
            xmin, ymin, xmax, ymax = text['bbox'].split(',')
            if float(xmin) < x0 + 1 and float(ymax) < y0 - 30:
                take = True
                break
    if take:
        i = 0
        for text in textline.find_all("text"):
            # In case a line with minimum x does not start with a postbase
            if i == 0 and not ("font" in text.attrs and re.search("Bold|1-0|5-0", text['font'])):
                break
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
                break # Stop looking for postbases after # symbol
            else:
                if len(s) and current:
                    d += text.string
            i += 1

for s in words:
    if len(s) > 1:
        d = definitions[s].lstrip().rstrip()
        d = re.sub('\n|\r', '', d)
        for w1 in s.split(","):
            for w in w1.split("/"):
                # Replace special characters
                w = replaceSpecialCharacters(w)
                # Remove digits
                w = ''.join([i for i in w if not i.isdigit()])
                # Remove whitespaces
                w = w.replace(' ', '')
                if len(w) > 1 and w not in postbases:
                    postbases.append(w)
                    postbases_definitions.append(d.lstrip('0123456789. '))

f.close()
writeListToFile(postbases, '%s.postbases.txt' % filename)
writeListToFile(postbases_definitions, '%s.postbases.definitions.txt' % filename)
