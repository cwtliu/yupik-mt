# *-* encoding:utf-8 *-*
import re
from constants import *

class Postbase(object):
    def __init__(self, formula, debug=True):
        self.formula = formula
        self.final = not "\\" in formula
        self.debug = debug
        self.tokens = self.tokenize(self.formula) # meaningful tokens

    def __repr__(self):
        return self.formula

    def tokenize(self, formula):
        """
        Tokenize postbase formula.

        >>> p = Postbase("+'(g/t)u:6a")
        >>> p.tokens
        ['+', "'", '(g/t)', 'u', ':6', 'a']
        """
        return filter(None, re.split(re.compile("(\([\w|/]+\))|(:[\w|\d])|([\w|+|@|'|-|%|~|.|?|—])"), formula))

    def concat(self, word):
        new_word = word
        for token in self.tokens:
            new_word = apply(token, new_word)
        return new_word

    def apply(self, token, root):
        """
        token and word are (properly encoded) strings.
        Apply token to word. Modify word in place.
        """

        flag = False
        if token == '~':
            if root[-2] == 'e':
                root = root[:-2]+root[-1]
        elif token == "+"
            pass
        elif token == "-"
            if root[-2] in consonants:
                root = root[:-2]+root[-1]
        elif token == "%"
            if root[-2] == r and root[-3] in vowels and root[-4] in vowels and root[-5] in consonants:
                flag = True
            if flag:
                root = root[:-2]+root[-1]
            elif root[-2] == 'g' or r[-3:] == 'er-' or '*' in root:
                root = root[:-2]+root[-1]
            flag = False
        elif token == ":ng"
        elif token == ":r"
        elif token == ":g"
        elif token == "n@"
        elif token == "ng"
        elif token == "-"
        elif token == "-"
        elif token == "-"
        elif token == "-"
        elif token == "-"
        elif token == "-"
        elif token == "-"
        elif token == "-"
        elif token == "-"


        return root

    def parse(self, root, subword, remaining_root):
        """
        root: dictionary root
        subword: remaining of the word (without root)
        remaining_root: remaining of the root
        return:
        - string (updated remain of the root = new dropped_word)
        - boolean (whether the current postbase can match word or not)
        """
        if self.debug: print "Parsing ", root, " + ", subword
        keep_on = True
        self.i_formula = 0
        self.i_subword = 0
        self.dropped_dash = 0
        remaining_root = remaining_root.strip('-')
        while keep_on and self.i_formula < len(self.formula) and self.i_subword < len(subword):
            keep_on, remaining_root = self.transition(subword, remaining_root)
            self.i_formula += 1
        success = (self.i_formula == len(self.formula) \
            or (not self.final and (len(self.formula) - self.i_formula <= 2))) \
            and len(remaining_root) == 0
        return remaining_root, success

    def transition(self, subword, remaining_root):
        """
        subword : word without its supposed root
        return: boolean (whether current postbase character matches current subword's character)
        """
        character = self.formula[self.i_formula]
        subword_character = subword[self.i_subword]
        keep_on = True
        updated_remaining_root = remaining_root
        if character == "-":
            # Remove one consonant from remaining root
            if remaining_root and remaining_root[-1] in consonants and self.dropped_dash == 0:
                updated_remaining_root = remaining_root[1:]
                self.dropped_dash += 1
        elif character == "~":
            # Drop final e of remaining root
            if remaining_root[0] == 'e':
                updated_remaining_root = remaining_root[1:]
        elif character == "+":
            # no changes
            pass
        elif character.isalpha(): # letter
            self.i_subword += 1
            keep_on = character == subword_character
        elif character == '\\': # Ending of the postbase
            self.i_subword += 1
        else:
            raise Exception
        return keep_on, updated_remaining_root

# antislash means something comes after
postbases = [
    "-llru\\",
    "-lli\\",
    "-nrite\\"
    ]

if __name__== '__main__':
    p1 = Postbase("-llru\\")
    p2 = Postbase("-nrite\\")
    p3 = Postbase("+'(g/t)ur:6ag")
    w = "nerenrituq"
    # Check in dictionary
    #print p1.parse("pissur-", w)
    print(p2.apply("~", "nere-"))
    print(p2.apply("-", "pissur-"))

    # Run docstring tests
    import doctest
    doctest.testmod()
