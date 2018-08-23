"""
Spellcheck for Yup'ik words. Looks for English letters, illegal characters & combinations. Does not make spelling
corrections
"""

#__author__ = "Baxter Bond"
#__version__ = "0.0.0"

import re


def spellcheck(word):  #returns true when all spell checks have passed, otherwise returns false
    word = word.lower()  #sterilize capitilizations
    result = True
    if re.search(r"[^-'acegiklmnpqrstuvwy]", word):  #illegal letters or special characters not use
        #print("English letter or illegal symbol error")
        result = False
    if re.search(r"[aui]{3,}|[auie]e|e[eaui]", word): #triple vowels or vowels with e
        #print("Triple vowels or improper vowel error")
        result = False
    if re.search(r"([glrsv])\1\1|([ckmnpqtwy])\2", word): #two or more non-fricatives or 3 or more fricatives
        #print("consonant combination error")
        result = False
    if re.search(r"[ckpqt]'*([glrsv])\1|([glrsv])\2'*[ckpqt]", word): #stop followed/preceded by two or more fricatves
        #print("stop devoicing error")
        result = False
    if re.search(r"([glrsv])\1([glrsv])\2|[glrsv]([glrsv])\3", word): #voiceless fricative followed by two fricatives
        #print("fricative devoicing error")
        result = False
    if re.search(r"[cgklmnpqrstvwXy]{3,}", re.sub(r"([glrsv])\1|ng", "X", word)):
        #print("triple consonant error")
        result = False
    #print(re.sub(r"([glrsv])\1", "X", word))
    return result

#print(spellcheck("Beayakkaggtarllinirtluni"))
