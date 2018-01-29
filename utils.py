# Tools and utils
import os

def writeListToFile(list, filename):
    f = open(filename, 'w')
    for x in list:
        f.write(x.encode('utf-8') + os.linesep)
    f.close()
