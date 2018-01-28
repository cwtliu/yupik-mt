# Parser for Yup'ik -> English PDF dictionary
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
from utils import writeListToFile

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
        if 'bbox' in text.attrs:
            xmin, ymin, xmax, ymax = text['bbox'].split(',')
            xmins.append(float(xmin))
            ymaxs.append(float(ymax))

x0 = min(xmins)
y0 = max(ymaxs)
postbases = []

for textline in soup.find_all("textline"):
    take = False
    s = ""
    for text in textline.find_all("text"):
        if 'bbox' in text.attrs:
            xmin, ymin, xmax, ymax = text['bbox'].split(',')
            if float(xmin) < x0 + 1 and float(ymax) < y0 - 30:
                take = True
                break
    if take:
        for text in textline.find_all("text"):
            if re.search("Bold", text['font']) and not re.search("{", text.string):
                s += text.string
            else:
                break
        # Remove digits
        s = ''.join([i for i in s if not i.isdigit()])        
        if len(s):
            postbases.append(s)

f.close()
writeListToFile(postbases, '%s.postbases.txt' % filename)