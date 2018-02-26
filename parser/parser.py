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

        words = [w.rstrip('\n').rstrip('-') for w in verbs[0]]
        words.extend([w.rstrip('\n') for w in nouns[0]])
        self.dictionary = words

    def compare(self, w1, w2):
        """
        w1 is the reference word
        """
        #if len(w2) < len(w1):
        #    temp = w1
        #    w1 = w2
        #    w2 = temp
        d = 0
        for i in range(min(len(w1), len(w2))):
            if w1[i] != w2[i]:
                break
            else:
                d += 1
        return d

    def match(self, word):
        # Check against dictionary
        matches = {}
        for w in self.dictionary:
            d = self.compare(w, word)
            matches[w[:d+2]] = d
        best_match = max(matches.values())
        return [m for m in matches if matches[m] == best_match]

    def parse(self, word, match):
        good = []
        if self.debug: print "\n+ Root ", match
        # Get the remaining of root and word
        #remaining_word = ""
        #remaining_root = ""
        #for i in range(len(m)):
        #    if word[i] != m[i]:
        #        remaining_word = word[i:]
        #        remaining_root = m[i:]
        #        break

        for postbase in self.postbases:
            if self.debug: print "Postbase ", postbase
            # Assuming one level only
            new_word = postbase.concat(match)
            #print(self.compare(new_word, word)-len(new_word))
            good_match = abs(self.compare(new_word, word)-len(new_word)) <= 2
            if self.debug: print good_match
            #leftover_root, good_match = postbase.parse(m, remaining_word, remaining_root)
            if good_match:
                good.append((postbase, new_word))
        return good

    def analyze(self, word):
        if self.debug: print "Looking at ", word
        matches = self.match(word)
        matches = [([m], m) for m in matches]
        # Matches is a list of tuples (tokens, match)
        # such that concatenation of tokens = match
        final_matches = []
        while len(matches):
            tokens, match = matches.pop()
            if self.debug: print("++++ Match %s ++++" % match, tokens)
            if abs(self.compare(match, word)-len(match)) <= 2 and abs(len(word) - self.compare(match, word)) <= 2:
                final_matches.append((tokens, match))
            else:
                good = self.parse(word, match)
                matches = matches + [(tokens + [g[0]], g[1]) for g in good]

        return final_matches

if __name__ == '__main__':
    test_words = ["pissullrunrituq", "nerenrituq"]
    p = DirtyParser(debug=False)
    #for w in test_words:
    #    print p.parse(w)
    print(p.analyze("pissuryug"))
    print(p.analyze("pissuryunriteqatartuq"))
