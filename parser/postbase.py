#!/usr/bin/python
# -*- coding:utf-8 -*-
# Authors: cwtliu, Temigo

import re
from constants import *

class Postbase(object):
    def __init__(self, formula, isEnding=False, debug=0):
        self.formula = formula
        self.final = not "\\" in formula
        self.debug = debug
        self.token = []
        self.tokens = self.tokenize(self.formula) # meaningful tokens
        self.isEnding = isEnding
        if not self.matched() and self.debug>=2: print("Warning: %s has non-matching parenthesis." % formula)
        self.reappend = False

    def __repr__(self):
        return self.formula

    # Check that simple parenthesis are matched in string
    def matched(self):
        count = 0
        for i in self.formula:
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
            if count < 0:
                return False
        return count == 0

    def tokenize(self, formula):
        """
        Tokenize postbase formula.

        >>> p = Postbase("+'(g/t)u:6a")
        >>> p.tokens
        ['+', "'", '(g/t)', 'u', ':6', 'a']
        """
        return filter(None, re.split(re.compile("(\([\w|/]+\))|(:[\w|\d]|:\(6\)|:\(e\)|:\(u\))|([\w|+|@|'|-|%|~|.|?|—])"), formula))

    def concat(self, word):
        new_word = word
        for token in self.tokens:
            new_word = self.apply(token, new_word)
            if self.debug>=2: print(token, new_word)
        return new_word

    def begins_with(self, token):
        """
        Check whether postbase begins with token.

        >>> p = Postbase("+'(g/t)u:6a")
        >>> p.begins_with("(g/t)")
        True
        >>> p.begins_with("n")
        False
        """
        # FIXME what if there is (6) or :6 in the suffix? Does it count as beginning with 6 ?
        return next(token for token in self.tokens if re.search("[\w|\d]", token)) == token

    def apply(self, token, root):
        """
        token and word are (properly encoded) strings.
        Apply token to word. Modify word in place.
        Assuming root does not have any dash at the end.

        >>> p1 = Postbase("-nrite")
        >>> p1.apply("-", "pissur")
        'pissu'
        >>> p2 = Postbase("~+miu")
        >>> p2.apply("~", "nere")
        'ner'
        >>> p3 = Postbase("%lu")
        >>> p3.apply("%","imir")
        'imi'
        >>> p3.apply("%","pag")
        'pag'
        >>> p3.apply("%","iqaar")
        'iqaar'
        >>> p4 = Postbase("%(e)nka")
        >>> p4.apply("%","qimugte")
        'qimugte'
        >>> p5 = Postbase(":6a")
        >>> p5.apply(":6","pitu")
        'pitu'
        >>> p5.apply(":6","ner'u")
        "ner'u"
        >>> p6 = Postbase(":guq")
        >>> p6.apply(":g","pai")
        'paig'
        >>> p7 = Postbase(":ruluku")
        >>> p7.apply(":r","paa")
        'paar'
        >>> p7.apply(":r","pa")
        'pa'
        >>> p8 = Postbase("-qatar-")
        >>> p8.apply("q","ayag")
        'ayak'
        >>> p9 = Postbase("'(g/t)uq")
        >>> p9.apply("'","ner")
        'ner'
        >>> p9.apply("'","qaner")
        'qaner'
        >>> p10 = Postbase("@~+ni-")
        >>> p10.apply("@","kipute")
        'kiput'
        >>> p10.apply("@","apte")
        'ap'
        >>> p11 = Postbase("@~+6aite-")
        >>> p11.apply("@","kipute")
        'kipus'
        >>> p12 = Postbase("@~+6aite-")
        >>> p12.apply("@","maan(e)te")
        'maan(e)l'
        >>> p13 = Postbase("@~:(u)ciq")
        >>> p13.apply("@","kipute")
        'kipus'
        >>> p14 = Postbase("@~:(u)ciq")
        >>> p14.apply("@","kit'e")
        "kis'u"
        >>> p15 = Postbase("@~:(u)ciq")
        >>> p15.apply("@","ce8irte")
        'ce8iru'
        >>> p16 = Postbase("@~+yug-")
        >>> p16.apply("@","kipute")
        'kipus'
        >>> p17 = Postbase("@~+6aite-")
        >>> p17.apply("@","kipute")
        'kipuc'
        >>> p18 = Postbase("@~+6aite-")
        >>> p18.apply("@","kit'e")
        'kic'
        """
        if len(root) == 0:
            return root

        if root[-1] == "-":
            print("Root should not have a dash at the end.")
            return root
            #raise Exception("Root should not have a dash at the end.")

        #if self.reappend:
        #    self.tokens[self.tokens.index(token)] = ':' + token
        #    token = ':' + token
        #    self.reappend = False

        # Return the first alpha item in tokens list

        first_letter=''
        first_letter_index = -1
        for l in self.tokens:
            if l.isalnum():
                first_letter = l
                first_letter_index = self.tokens.index(l)
                break

        flag = False
        if token == '=':
            root = root+'='
        elif token == '~':
            if root[-1] == 'e':
                root = root[:-1]
        elif token == "+":
            pass

        elif token == "-":
            if root[-1] in ["g", "r"]:
                root = root[:-1]
        elif token == "%":
            if len(root) > 3:
                if root[-1] == 'r' and root[-2] in vowels and root[-3] in vowels and root[-4] in consonants:
                    flag = True
            if flag:
                pass
            elif root[-1] == 'g' or (len(root) >= 2 and root[-2:] == 'er') or '*' in root:
                pass
            elif root[-1] in ["g", "r"]:
                root = root[:-1]
            flag = False
        elif token in [":(6)", ":(e)", ":(u)", "(e)", "(te)"]:
            pass
        elif token == ":6":
            position = self.tokens.index(token)
            #print(self.tokens.index(token))
            #print(self.tokens)
            if position+2 == len(self.tokens):
                #print('yes')
                if len(root) >= 2 and self.tokens[position+1] in vowels and root[-1] in vowels and root[-2] not in vowels:
                    root = root #+''.join(self.tokens[:position])
                else:
                    root = root+'6'#+''.join(self.tokens[:position])+'6'
            elif position+2 < len(self.tokens):
                if len(root) >= 2 and self.tokens[position+1] in vowels and self.tokens[position+2] not in vowels and root[-1] in vowels and root[-2] not in vowels:
                    root = root #+''.join(self.tokens[:position])
                else:
                    root = root+'6'#+''.join(self.tokens[:position])+'6'
        elif token == ":g":
            position = self.tokens.index(token)
            if position+2 == len(self.tokens):
                if len(root) >= 2 and self.tokens[position+1] in vowels and root[-1] in vowels and root[-2] not in vowels:
                    root = root+''.join(self.tokens[:position])
                else:
                    root = root+''.join(self.tokens[:position])+'g'
            elif position+2 < len(self.tokens):
                if self.tokens[position+1] in vowels and self.tokens[position+2] not in vowels and root[-1] in vowels and root[-2] not in vowels:
                    root = root+''.join(self.tokens[:position])+''.join(self.tokens[position+1:])
                else:
                    root = root+''.join(self.tokens[:position])+'g'
        elif token == ":r":
            position = self.tokens.index(token)
            if position+2 == len(self.tokens):
                if len(root) >= 2 and self.tokens[position+1] in vowels and root[-1] in vowels and root[-2] not in vowels:
                    root = root+''.join(self.tokens[:position])
                else:
                    root = root+''.join(self.tokens[:position])+'r'
            elif position+2 < len(self.tokens):
                if len(root) >= 2 and self.tokens[position+1] in vowels and self.tokens[position+2] not in vowels and root[-1] in vowels and root[-2] not in vowels:
                    root = root+''.join(self.tokens[:position])
                else:
                    root = root+''.join(self.tokens[:position])+'r'
        elif self.tokens.index(token) == first_letter_index and token in ['g', 'k', '4', 'q', 'r', '5'] + vowels:
            if token == 'g':
                if root[-1] == 'q' or root[-1] == 'r' or root[-1] == '5':
                    root = root[:-1]+'r'
                else:
                    root = root + 'g'
            elif token == 'k':
                if root[-1] == 'q' or root[-1] == 'r' or root[-1] == '5':
                    root = root[:-1]+'q'
                else:
                    root = root + 'k'
            elif token == '4':
                if root[-1] == 'q' or root[-1] == 'r' or root[-1] == '5':
                    root = root[:-1]+'5'
                else:
                    root = root + '4'
            elif token == 'q':
                if root[-1] == 'g' or root[-1] == 'k' or root[-1] == '4':
                    root = root[:-1]+'k'
                else:
                    root = root + 'q'
            elif token == 'r':
                if root[-1] == 'g' or root[-1] == 'k' or root[-1] == '4':
                    root = root[:-1]+'g'
                else:
                    root = root + 'r'
            elif token == '5':
                if root[-1] == 'g' or root[-1] == 'k' or root[-1] == '4':
                    root = root[:-1]+'4'
                else:
                    root = root + '5'
            elif token in vowels:
                if len(root) >= 2 and (root[-2:] == 'er' or root[-2:] == 'eg'):
                    root = root[:-2]+root[-1]
                else:
                    if root[-1] == 'e':
                        root = root[:-1] + token
                    else:
                        root = root + token
        elif token == "'":
            if len(root) == 3:
                if root[-1] == 'e' and root[-2] in consonants and root[-3] in vowels:
                    root = root[:-1] + "'"
            elif len(root) == 4:
                if root[-1] == 'e' and root[-2] in consonants and root[-3] in vowels and root[-4] in consonants:
                    root = root[:-1] + "'"
        elif token == ".":
            pass
        elif token == "@":
            # THIS IS ALL @ N RULE
            if len(root) >= 2 and root[-2:] == "te": # assuming an e deletion has already occurred...
                root = root[:-1]
            #print(first_letter)
            #print(self.tokens)
            if first_letter == "n":
                if len(root) >= 2 and root[-1] == "t" and (root[-2] in voiced_fricatives \
                                    or root[-2] in voiceless_fricatives \
                                    or root[-2] in voiced_nasals \
                                    or root[-2] in voiceless_nasals \
                                    or root[-2] in stops):
                    root = root[:-1]
                else:
                    pass
            # FIXME what if there is (6) or :6 in the suffix? Does it count as beginning with 6
            elif self.tokens.index(token) == first_letter_index and token in ['l','g','k','6'] and self.isEnding:
                if token == 'l':
                    if root[-1] == 't':
                        root = root[:-1] + '2'
                    else:
                        root = root + 'l'
                else:
                    if root[-1] == 't' and '(e)' in self.tokens:
                        root = root[:-2] + 'es' #assuming that the (e) is a single index and removed
                    elif root[-1] == 't':
                        root = root[:-1] + 's'
                    else:
                        root = root + token
            elif (first_letter == "6" or first_letter == "m" or first_letter == "v") \
                                    and len(root) >= 2 \
                                    and root[-1] == "t" \
                                    and not self.isEnding \
                                    and (root[-2] in voiced_fricatives \
                                        or root[-2] in voiceless_fricatives \
                                        or root[-2] in voiced_nasals \
                                        or root[-2] in voiceless_nasals \
                                        or root[-2] in stops):
                #print('yes')
                if root[-2] in stops:
                    root = root[:-1]
                elif root[-2] == 'm':
                    root = root[:-1]+'7'
                elif root[-2] == 'n':
                    root = root[:-1]+'8'
                elif root[-2] == '6':
                    root = root[:-1]+'9'
                elif root[-2] == 'v':
                    root = root[:-1]+'1'
                elif root[-2] == 'l':
                    root = root[:-1]+'2'
                elif root[-2] == 's':
                    root = root[:-1]+'3'
                elif root[-2] == 'g':
                    root = root[:-1]+'4'
                elif root[-2] == 'r':
                    root = root[:-1]+'5'

            elif (first_letter == "6" or first_letter == "m" or first_letter == "v") \
                                    and root[-1] == "t" \
                                    and '(e)' in root:
                root = root[:-1]+'l'
            elif (first_letter == "6" or first_letter == "m" or first_letter == "v") \
                                    and len(root) >= 2 \
                                    and root[-1] == "t" \
                                    and root[-2] in vowels:
                root = root[:-1]+'s' #IT MAY BE EASIER TO HAVE CODE THAT REPRESENTS (E) as a single token
        elif token == "(u)" and self.begins_with("(u)") and not self.isEnding:
            if len(root) >= 2 and root[-1] == "t" and root[-2] in vowels:
                root = root[:-1] + "y"
            elif len(root) >= 6 and root[-6:] == "(e)te":
                root = root[:-2] + "l"
        elif first_letter == "y" and not self.isEnding and self.tokens.index(token) == first_letter_index:
            if len(root) >= 2 and root[-1] == "t":
                root = root[:-1] + "c" #NEEDS A WAY TO REMEMBER NOT TO ADD THE Y of 'yug', BECAUSE OTHERWISE KIPUCU is KIPUCYU
            else:
                root = root + "y"
        elif token == "?": # TODO
            pass
        elif re.search(re.compile("\("), token): # All the (g), (g/t), etc
            letters = [x for x in re.split(re.compile("\(|\)|\/"), token) if len(x) > 0]
            conditions = {
                "i": len(root) >= 2 and root[-2:] == "te",
                "6": root[-1] in vowels,
                "r": len(root) >= 2 and root[-2:] == "te",
                "s": root[-1] in vowels,
                "t": root[-1] in consonants,
                "u": root[-1] in consonants or root[-1] == "e",
                "g": len(root) >= 2 and root[-2] in consonants and root[-1] in consonants,
                # FIXME (q)must be used with demonstrative adverb bases,
                # but is optional with positional bases (p.179)
                "q": False,
                "ar": False,
                "aq": False,
                "ur": False,
            }
            for letter in letters:
                if conditions[letter]:
                    root += letter
                    break
        elif token == "\\" or token == ":":
            pass # not an ending
        elif token in vowels or token in consonants:
            if self.debug>=2: print("Default token", token)
            if token in vowels and root[-1] == 'e':
                root = root[:-1] + token
            else:
                root = root + token
        #elif token[0] == ':':
        #    if len(token[1:]):
        #        self.tokens[self.tokens.index(token)] = token[1:]
        #        root = self.apply(token[1:], root)
        #    self.reappend = True
        else:
            print("Unknown token: %s (in postbase %s decomposed as %s)" % (token, self.formula, self.tokens))
            #raise Exception("Unknown token: %s (in postbase %s decomposed as %s)" % (token, self.formula, self.tokens))
        return root

# antislash means something comes after
postbases = [
    "-llru\\",
    "-lli\\",
    "-nrite\\",
    "@~+yug\\",
    "-qatar\\",
    "+'(g/t)uq"
    ]

if __name__== '__main__':
    p1 = Postbase("-llru\\")
    p2 = Postbase("-nrite\\")
    p3 = Postbase("+'(g/t)ur:6ag")
    w = "nerenrituq"
    #p2.tokens = [':6','a']
    # Check in dictionary
    #print p1.parse("pissur-", w)
    #print(p2.apply("~", "nere"))
    #print(p2.apply("-", "pissur"))
    #print(p2.apply(":6", "pissuru"))
    #print(p2.apply(":g", "pissur"))
    #print(p2.tokens)
    #print(p2.concat("nere"))
    #print(p3.tokens)
    #print(p3.concat("nere"))
    p4 = Postbase("@~+yug\\", debug=2)
    print(p4.concat("ce8irte"))
    # Run docstring tests
    #import doctest
    #doctest.testmod()
