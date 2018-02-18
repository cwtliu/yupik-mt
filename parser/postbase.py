# *-* encoding:utf-8 *-*
import re
from constants import *

class Postbase(object):
    def __init__(self, formula, debug=True):
        self.formula = formula
        self.final = not "\\" in formula
        self.debug = debug
        self.token = []
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
        """
        if root[-1] == "-":
            raise Exception("Root should not have a dash at the end.")

        flag = False
        if token == '~':
            if root[-1] == 'e':
                root = root[:-1]
        elif token == "+":
            pass
        elif token == "-":
            if root[-1] in consonants:
                root = root[:-1]
        elif token == "%":
            if root[-1] == 'r' and root[-2] in vowels and root[-3] in vowels and root[-4] in consonants:

                flag = True
            if flag:
                pass
            elif root[-1] == 'g' or root[-2:] == 'er' or '*' in root:
                pass
            elif root[-1] in consonants:
            	root = root[:-1]
            flag = False

        elif token == ":ng":
        	position = self.tokens.index(token)
        	if position+2 == len(self.tokens):
        		if self.tokens[position+1] in vowels and root[-1] in vowels and root[-2] not in vowels:
        			root = ''.join(root)+''.join(self.tokens[:position])
        		else:
        			root = ''.join(root)+''.join(self.tokens[:position])+'6'
        	elif position+2 < len(self.tokens):
        		if self.tokens[position+1] in vowels and self.tokens[position+2] not in vowels and root[-1] in vowels and root[-2] not in vowels:
        			root = ''.join(root)+''.join(self.tokens[:position])
        		else:
        			root = ''.join(root)+''.join(self.tokens[:position])+'6'
        elif token == ":g":
        	position = self.tokens.index(token)
        	if position+2 == len(self.tokens):
        		if self.tokens[position+1] in vowels and root[-1] in vowels and root[-2] not in vowels:
        			root = ''.join(root)+''.join(self.tokens[:position])
        		else:
        			root = ''.join(root)+''.join(self.tokens[:position])+'g'
        	elif position+2 < len(self.tokens):
        		if self.tokens[position+1] in vowels and self.tokens[position+2] not in vowels and root[-1] in vowels and root[-2] not in vowels:
        			root = ''.join(root)+''.join(self.tokens[:position])+''.join(self.tokens[position+1:])
        		else:
        			root = ''.join(root)+''.join(self.tokens[:position])+'g'
        elif token == ":r":
        	position = self.tokens.index(token)
        	if position+2 == len(self.tokens):
        		if self.tokens[position+1] in vowels and root[-1] in vowels and root[-2] not in vowels:
        			root = ''.join(root)+''.join(self.tokens[:position])
        		else:
        			root = ''.join(root)+''.join(self.tokens[:position])+'r'
        	elif position+2 < len(self.tokens):
        		if self.tokens[position+1] in vowels and self.tokens[position+2] not in vowels and root[-1] in vowels and root[-2] not in vowels:
        			root = ''.join(root)+''.join(self.tokens[:position])
        		else:
        			root = ''.join(root)+''.join(self.tokens[:position])+'r'
        #elif token == ":r"
        #elif token == ":g"
        elif token == "'":
            if root[-6] == '(' \
                and root[-5] in consonants \
                and root[-4] == ')' \
                and root[-3] in vowels \
                and root[-2] in consonants \
                and root[-1] == 'e':
                root = root + "'"
        elif token == ".":
            pass
        elif token == "@":
            if root[-2:] == "te":
                root = root[:-1]
            elif self.begins_with("n") and root[-1] == "t" and (root[-2] in voiced_fricatives \
                                    or root[-2] in voiceless_fricatives \
                                    or root[-2] in voiced_nasals \
                                    or root[-2] in voiceless_nasals \
                                    or root[-2] in stops):
                root = root[:-1]
            # FIXME what if there is (6) or :6 in the suffix? Does it count as beginning with 6 ?
            elif (self.begins_with("6") or self.begins_with("m") or self.begins_with("v"))
                                    and root[-1] == "t"
                                    and (root[-2] in voiced_fricatives \
                                        or root[-2] in voiceless_fricatives \
                                        or root[-2] in voiced_nasals \
                                        or root[-2] in voiceless_nasals \
                                        or root[-2] in stops):
                root = root[:-1]
            elif self.begins_with("(u)"):
                if root[-1] == "t" and root[-2] in vowels:
                    root = root[:-1] + "y"
                elif root[-6:] == "(e)te":
                    root = root[:-2] + "l"
            elif self.begins_with("y"):
                if root[-2] == "t":
                    root = root[:-2] + "c"
        elif token == "?": # TODO
            pass
        elif re.search(re.compile("\("), token): # All the (g), (g/t), etc
            letters = [x for x in re.split(re.compile("\(|\)|\/"), token) if len(x) > 0]
            conditions = {
                "i": root[-2] == "te",
                "6": root[-1] in vowels,
                "r": root[-2] == "te",
                "s": root[-1] in vowels,
                "t": root[-1] in consonants,
                "u": root[-1] in consonants or root[-1] == "e",
                "g": root[-2] in consonants and root[-1] in consonants
            }
            for letter in letters:
                if conditions[letter]:
                    root += letter
                    break
        else:
            raise Exception("Unknown token: %s" % token)
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
    p2.tokens = [':ng','a']
    # Check in dictionary
    #print p1.parse("pissur-", w)
    print(p2.apply("~", "nere"))
    print(p2.apply("-", "pissur"))
    print(p2.apply(":ng", "pissuru"))
#    print(p2.apply(":g", "pissur"))

    # Run docstring tests
    import doctest
    doctest.testmod()
