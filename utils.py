# *-* encoding: utf-8 *-*
# Tools and utils
# Author: Temigo

import os

def writeListToFile(list, filename):
    f = open(filename, 'w')
    for x in list:
        f.write(x.encode('utf-8') + os.linesep)
    f.close()

def replaceSpecialCharacters(w):
    w = w.replace(u'\u00F7', u'\u0144') # division to n acute
    w = w.replace(u'\u00B5', u'\u1E3F') # micro to m acute
    w = w.replace('TMg', u'\u0144g')# ng acute
    # Ligatures : leave them with ¥ symbol
    #w = w.replace(u'\u00A5g', u'\u011D') # ¥g to ug ligature (g circonflex)
    #w = w.replace(u'\u00A5q', u'\u')# ur ligature
    # urr ligature
    return w
