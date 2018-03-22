from __future__ import print_function
import pickle

'''
Appends generated english to english word mappings to two files. This will
provide an additional corpus to train an NN which takes an unaranged set of
english words and translates them to a coherent sentence.
The first set of english words are taken from raw translations of yupik roots, 
postbases, and endings from dictionary lookups.
The second set of english words are taken from the provided english translations.

author: kechavez
'''

# Retrieve all root, postbases, endings from pickled format.
 
