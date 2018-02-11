# *-* encoding:utf-8 *-*
import re
from constants import *

class Postbase(object):
    def __init__(self, formula, debug=True):
        self.formula = formula
        self.final = not "\\" in formula
        self.debug = debug

    def __repr__(self):
        return self.formula

    def concat(self, word):
        pass

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

postbases = [
    "-llru\\",
    "-lli\\",
    "-nrite\\"
    ]

if __name__== '__main__':
    # antislash means something comes after
    p1 = Postbase("-llru\\")
    p2 = Postbase("-nrite\\")
    w = "nerenrituq"
    # Check in dictionary
    #print p1.parse("pissur-", w)
    print w[4:]
    print p2.parse("nere-", w[4:], "-")
