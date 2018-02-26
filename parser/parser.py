#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Temigo

import re
from constants import *
from postbase import Postbase
import time

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

    def __init__(self, dictionary_path='../data/',
                postbases_folder='../data/postbases_txt/',
                postbases_files=None,
                debug=0):
        self.debug = debug
        self.dictionary_path = dictionary_path
        self.postbases_folder = postbases_folder
        self.postbases_files = postbases_files
        if self.postbases_files is None:
            self.postbases_files = ['LMNPQR']

        self.postbases = [] # List of postbases in dictionary
        self.dictionary = [] # List of words in dictionary (nouns and verbs)
        self.open_dictionary()
        self.open_postbases()

        #self.postbases = [Postbase(p, debug=self.debug) for p in postbases]

    def open_dictionary(self):
        nouns = []
        verbs = []
        with open(self.dictionary_path + "all_nouns_manually_edited.txt", "r") as f_nouns:
            nouns.extend(f_nouns.readlines())
        with open(self.dictionary_path + "all_verbs_manually_edited.txt", "r") as f_verbs:
            verbs.extend(f_verbs.readlines())

        words = [w.rstrip('\n').rstrip('-') for w in verbs]
        words.extend([w.rstrip('\n') for w in nouns])
        self.dictionary = words
        if self.debug>=1: print("\nSuccessfully loaded dictionary with %d nouns and %d verbs (total %d words).\n" % (len(nouns), len(verbs), len(words)))

    def open_postbases(self):
        postbases = []
        for filename in self.postbases_files:
            f_postbases = open(self.postbases_folder + filename + ".postbases.txt", "r")
            postbases.extend(f_postbases.readlines())

        postbases = [p.replace('–', '-').replace('*', '') for p in postbases]
        self.postbases = [Postbase(re.sub(re.compile("-$"), "\\\\", p.rstrip('\n')), debug=self.debug) for p in postbases]
        if self.debug>=1: print("\nSuccessfully loaded %d postbases." % len(postbases))

    def compare(self, w1, w2):
        """
        w1 is the reference word
        Returns length of identical sequence (starting from beginning of word)
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
        if self.debug>=2: print "\n+ Root ", match
        for postbase in self.postbases:
            if self.debug>=2: print "Postbase ", postbase
            # Assuming one level only
            new_word = postbase.concat(match)
            good_match = abs(self.compare(new_word, word)-len(new_word)) <= 2
            if self.debug>=2: print good_match
            if good_match:
                good.append((postbase, new_word))
        return good

    def analyze(self, word):
        if self.debug>=1: print "Looking at ", word
        start_time = time.time()
        matches = self.match(word)
        dict_time = time.time()
        matches = [([m], m) for m in matches]
        # Matches is a list of tuples (tokens, match)
        # such that concatenation of tokens = match
        final_matches = []
        while len(matches):
            tokens, match = matches.pop()
            if self.debug>=2: print("++++ Match %s ++++" % match, tokens)
            if abs(self.compare(match, word)-len(match)) <= 2 and abs(len(word) - self.compare(match, word)) <= 2:
                final_matches.append((tokens, match))
            else:
                # Abandon if the last token is final and we didn't pass above condition
                if isinstance(tokens[-1], Postbase) and tokens[-1].final:
                    pass
                else:
                    good = self.parse(word, match)
                    matches = matches + [(tokens + [g[0]], g[1]) for g in good]
        match_time = time.time()
        if self.debug>=1: print("\nDictionary lookup: %f\nMatching recursion: %f\n" % (dict_time - start_time, match_time - dict_time))
        return final_matches

if __name__ == '__main__':
    test_words = ["pissullrunrituq", "nerenrituq"]
    p = DirtyParser(debug=1, postbases_files=['VY'])
    #for w in test_words:
    #    print p.parse(w)
    print(p.analyze("pissuryug"))
    #print(p.analyze("pissuryunriteqatartuq"))
