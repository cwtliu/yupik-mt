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
    word = word.replace('ń','8')
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
        self.endings = [] # List of endings
        self.open_dictionary()
        self.open_postbases()
        self.open_endings()

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
        self.dictionary = [convert(word) for word in words]
        if self.debug>=1: print("Successfully loaded dictionary with %d nouns and %d verbs (total %d words)." % (len(nouns), len(verbs), len(words)))

    def open_postbases(self):
        postbases = []
        # FIXME noun and verb postbases
        #for filename in self.postbases_files:
        #    f_postbases = open(self.postbases_folder + filename + ".postbases.txt", "r")
        #    postbases.extend(f_postbases.readlines())
        with open(self.dictionary_path + "postbases_txt/all_postbases_noun.txt", "r") as f_noun:
            postbases.extend(f_noun.readlines())
        with open(self.dictionary_path + "postbases_txt/all_postbases_verb_man_edit.txt", "r") as f_verb:
            postbases.extend(f_verb.readlines())
        # FIXME long dash vs short dash difference
        postbases = [p.replace('–', '-').replace('*', '').replace('’', '\'') for p in postbases]
        self.postbases = [Postbase(re.sub(re.compile("-$"), "\\\\", convert(p.rstrip('\n'))), debug=self.debug) for p in postbases]
        self.postbases = [p for p in self.postbases if p.matched()]
        if self.debug>=1: print("Successfully loaded %d postbases." % len(postbases))

    def open_endings(self):
        endings = []
        with open(self.dictionary_path + "endings.txt", "r") as f_endings:
            endings.extend(f_endings.readlines())
        self.endings = [Postbase(convert(e.rstrip('\n').replace("\"", "")), isEnding=True, debug=self.debug) for e in endings]
        self.endings = [e for e in self.endings if e.matched()]
        if self.debug>=1: print("Successfully loaded %d endings." % len(self.endings))

    def compare(self, w1, w2):
        """
        w1 is the reference word (dictionary)
        Returns length of identical sequence (starting from beginning of word)
        """
        d = 0
        for i in range(min(len(w1), len(w2))):
            if w1[i] != w2[i]:
                break
            else:
                d += 1
        return d, len(w1)-d

    def match(self, word):
        """
        Check against dictionary: find potential root matches list
        """
        matches_d = {}
        matches_diff = {}
        for w in self.dictionary:
            if w[0] == word[0]:
                d, diff = self.compare(w, word)
                if w[-2:] == 'te':
                    diff = max(0, diff - 1)
                matches_d[w] = d
                matches_diff[w] = diff
        # Take the roots with a small enough difference
        return [m for m in matches_diff if matches_d[m] >= 1 and matches_diff[m] <= 1]

    def parse(self, word, match):
        """
        Comparing word with potential root match: test all postabses/endings
        """
        good = []
        if self.debug>=1: print "\n+ Root ", match
        for postbase in self.postbases+self.endings:
        #for postbase in [Postbase("+'(g/t)u:6a", debug=2)]:
            if self.debug>=2: print "Postbase ", postbase, postbase.tokens
            # Assuming one level only
            new_word = postbase.concat(match)
            diff = self.compare(new_word, word)[1]
            if postbase.formula[-3:] == 'te\\':
                diff = max(0, diff-1)
            good_match = diff <= 1
            if good_match:
                if self.debug>=1: print postbase, new_word
                good.append((postbase, new_word))
        if len(good) == 0:
            max_length = 0
        else:
            max_length = max([len(g[1]) for g in good])
        return [g for g in good if len(g) == max_length]

    def analyze(self, word):
        """
        Consider 1 word and
        - find potential matches in dictionary (self.match) and put them in a queue
        - pop a potential match from the queue
            - check whether the length is good enough and keep it if it is
            - check if the last postbase was final or not. Drop the match if it was.
            - Find new postbases/endings (self.parse) and add them to the queue.
        """
        if self.debug>=1: print "Looking at ", word
        start_time = time.time()
        matches = self.match(word)
        print(matches)
        dict_time = time.time()
        matches = [([m], m) for m in matches]
        # Matches is a list of tuples (tokens, match)
        # such that concatenation of tokens = match
        final_matches = []
        while len(matches):
            tokens, match = matches.pop()
            if self.debug>=1:
                print("++++ Match %s ++++" % match, tokens)
            if self.compare(match, word)[1] <= 1 and abs(len(word) - self.compare(match, word)[0]) <= 1:
                final_matches.append((tokens, match))
            else:
                # Abandon if the last token is final and we didn't pass above condition
                if isinstance(tokens[-1], Postbase) and tokens[-1].final:
                    pass
                else: # Last token is not final and above condition is not matched
                    good = self.parse(word, match)
                    # FIXME also try endings
                    #if len(good) > 0:
                    matches = matches + [(tokens + [g[0]], g[1]) for g in good]
                    #else: # No further postbase match => try endings

        match_time = time.time()
        if self.debug>=1: print("\nDictionary lookup: %f\nMatching recursion: %f\n" % (dict_time - start_time, match_time - dict_time))
        return final_matches

    def best_score(self, matches, word):
        """"
        Final decision: decide which list of root/postbases/endings we should
        keep based on differences with word
        """
        #print([(m, self.compare(word, m[1])) for m in matches])
        #d = [m for m in matches if abs(len(m[1]) - len(word)) == 0]
        d = [m for m in matches if self.compare(word, m[1])[0] == len(word)]

        if len(d) == 0:
            raise Exception("No good match found for %s with matches %s" % (word, matches))
        #elif len(d) > 1:
        #    Exception("Several matches were found for %s: %s" %(word, d))
        root_length = [len(m[0][0]) for m in d]
        max_length = max(root_length)
        return [m for m in d if len(m[0][0]) == max_length]

    def tokenize(self, sentence):
        if self.debug>=1: print("\nTokenizing: %s\n" % sentence)
        sentence = sentence.split(" ")
        sentence_matches = []
        for word in sentence:
            word = convert(word)
            matches = self.analyze(word)
            sentence_matches.append(self.best_score(matches, word))
        return sentence_matches

if __name__ == '__main__':
    test_words = ["pissullrunrituq", "nerenrituq"]
    p = DirtyParser(debug=1, postbases_files=['VY'])
    #for w in test_words:
    #    print p.parse(w)
    #print(p.analyze("pissuryug"))
    #print(p.analyze("pissuryunriteqatartuq"))
    # cenirte- / @~+yugnaite- / +’(g/t)u:6a
    #print(p.tokenize("alingullruuq"))
    # alinge- / -llru- / +'(g/t)uq
    #print(p.tokenize("an'uq"))
    # ane- / +'(g/t)uq
    #print(p.tokenize("anyunrituq"))
    # ane- / @~+yug- / -nrite- / +'(g/t)uq
    #print(p.tokenize("aqui2ruuk"))
    # ane- / +'(g/t)uuk
    #print(p.tokenize("elitnaurvik"))
    # elitnaurvik maybe?
    # or maybe elite- naurvik
    print(p.tokenize("waniwa unuaqu ayagciqlua"))
    # ce8ir / @~+yug- /  @~+ngaite- / +’(g/t)u:6a

    # yugni- / –ke- / @~–kengaq
    #print(p.tokenize("yugnikekengaq"))
    #print(p.tokenize("kipus6aituq"))
    #print(p.parse("ce8ircug6aitua", "ce8ircug6aite"))
    # kipute- / @~+ngaite- / +'(g/t)uq
