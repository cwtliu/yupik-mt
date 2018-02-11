# *-* encoding:utf-8 *-*
import re
from constants import *
from postbase import Postbase, postbases

# TODO conversions
def convert(word):
    word = word.replace('vv','1')
    word = word.replace('ll','2')
    word = word.replace('ss','3')
    word = word.replace('gg','4')
    word = word.replace('rr','5')
    word = word.replace('ng','6')
    word = word.replace('μ','7')
    word = word.replace('+','8')
    word = word.replace('TMg','9')
    word = word.replace('¥r','j')
    word = word.replace('¥rr','z')
    word = word.replace('¥g','x')
    word = word.replace('¥k','h')
    word = word.replace('¥q','d')
    return word

def deconvert(word):
    word = word.replace('1','vv')
    word = word.replace('2','ll')
    word = word.replace('3','ss')
    word = word.replace('4','gg')
    word = word.replace('5','rr')
    word = word.replace('6','ng')
    word = word.replace('7','m2')
    word = word.replace('8','n2')
    word = word.replace('9','ng2')
    word = word.replace('j','¥r')
    word = word.replace('z','¥rr')
    word = word.replace('x','¥g')
    word = word.replace('h','¥k')
    word = word.replace('d','¥q')
    return word


class DirtyParser(object):

    def __init__(self, dictionary_folder='../data/dictionary_txt/', dictionary_files=None, debug=True):
        self.debug = debug
        self.dictionary_folder = dictionary_folder
        self.dictionary_files = dictionary_files
        if self.dictionary_files is None:
            self.dictionary_files = ['NP']

        self.dictionary = [] # List of words in dictionary (nouns and verbs)
        self.open_dictionary()

        self.postbases = [Postbase(p, debug=self.debug) for p in postbases]

    def open_dictionary(self):
        nouns = []
        verbs = []
        for filename in self.dictionary_files:
            f_nouns = open(self.dictionary_folder + filename + ".nouns.txt", "r")
            f_verbs = open(self.dictionary_folder + filename + ".verbs.txt", "r")
            nouns.append(f_nouns.readlines())
            verbs.append(f_verbs.readlines())

        words = [w.rstrip('\n') for w in verbs[0]]
        words.extend([w.rstrip('\n') for w in nouns[0]])
        self.dictionary = words

    def match(self, word):
        # Check against dictionary
        matches = {}
        for w in self.dictionary:
            d = 0
            for i in range(len(w)):
                if w[i] != word[i]:
                    break
                else:
                    d += 1
            matches[w[:d+2]] = d
        best_match = max(matches.values())
        return [m for m in matches if matches[m] == best_match]

    def parse(self, word):
        if self.debug: print "Looking at ", word
        matches = self.match(word)

        good = []
        for m in matches:
            if self.debug: print "\n+ Root ", m
            # Get the remaining of root and word
            remaining_word = ""
            remaining_root = ""
            for i in range(len(m)):
                if w[i] != m[i]:
                    remaining_word = w[i:]
                    remaining_root = m[i:]
                    break

            for postbase in self.postbases:
                if self.debug: print "Postbase ", postbase
                leftover_root, good_match = postbase.parse(m, remaining_word, remaining_root)
                if good_match:
                    good.append((m, postbase, leftover_root))
        return good

if __name__ == '__main__':
    test_words = ["pissullrunrituq", "nerenrituq"]
    p = DirtyParser(debug=False)
    for w in test_words:
        print p.parse(w)
