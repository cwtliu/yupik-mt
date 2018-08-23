# coding: utf-8
from convert import *
#from edrop import *
from constants import *
word = 'pissur'
root_examples = ['alaqe-','ane-','aqui-','assir-','aurre-','ayag-','cali-','ce+irte-','cuka-','elite-','inarte-','iqvar-','kaig-','kuimar-','nere-','qalarte-','qavar-','qia-','tai-','taqe-','tuqu-','yurar-']
precessive_flag = False #before
consequential_flag = False #because
contingent_flag = False #whenever
conditional_flag = True #if, when (in the future)
concessive_flag = False #although, even though, even if
first_contemporative_flag = False #when (in the past)
second_contemporative_flag = False #while
indicative_flag = False #normal
int31 = False
int32 = False
int33 = False
int11 = True
int12 = False
int13 = False
int21 = False
int22 = False
int23 = False
int41 = False
int42 = False
int43 = False

def isShort(root): #if the base in the form VCe- or CVCe-, later add an apostrophe if not in VCVV form.
	if root[0] in consonants and root[1] in vowels and root[2] in consonants and root[3] == 'e':
		return True
	elif root[0] in vowels and root[1] in consonants and root[2] == 'e':
		return True
	else:
		return False

def precessive(root): #apply @~+(t)vaileg-
	if root[-1] == '-': #if ending has a dash
		root = root[:-1]
	if root[-1] == 'e': #if ending is an e
		root = root[:-1]
		if root[-1] == 't': #if ending was te, the tv becomes p
			return(root[:-1] + 'paileg-')
		else: #if ending was e but not preceded with a t
			return(root + 'vaileg-') 
	if root[-1] in consonants:
		return(root + 'paileg-') #if ending was a consonant, add (t)v becoming p
	else:
		return(root + 'vaileg-') #if ending was not a consonant or e

# def consequential(root):
# 	if root[-1] == '-': #if ending has a dash
# 		root = root[:-1]
# 	if root[-1] == 'e': #if ending is an e
# 		root = root[:-1]
# 		if root[-1] == 't': #if ending was te, the tv becomes c, but if it is a special te it becomes an l
# 			print("doesn't handle special te case, could be an l instead of a c")
# 			return(root[:-1] + 'ca-')
# 		if root[-1] in consonants:
# lot of complex cases here, tupagama -> tupiima, iterama -> itrama, and aqumngami, needs a second stressed vowel check

def contingent(root): #apply +'(g)aqa-
	#print('the attached verb has to have a -lar- or -tu- meaning regularly, or @~-yuite- meaning never or similar, cenirtaqatnga assilalartua')
	if root[-1] == '-': #remove dash
		root = root[:-1]
	if root[-1] == 'e': #if last e, follow apostrophe
		return (root[:-1]+'aqa-')
	if root[-1] in vowels and root[-2] in vowels: #if last two letters of root are vowels, attach a g
		return(root+'gaqa-')
	else:
		return(root+'aqa-')

def conditional(root): #apply @~-ku-
	specialte = False
	if root[-1] == '-': #remove dash
		root = root[:-1]
	if root[-1] == 'e': #if ending is an e
		root = root[:-1]
		if root[-1] == 't' and not specialte: #if ending was not special te
			if root[-2] in consonants:
				return(root[:-1] + 'esku-')
			else:
				return(root[:-1] + 'sku-')
		elif root[-1] == 't' and specialte: #if ending was special te
			return(root[:-1] + 'lku-')
		else: 
			return(root + 'ku-') 
	if root[-1] == 'r': #if ending is r, the k becomes a q
		return(root[:-1] + 'qu-')
	elif root[-1] == 'g': #if ending is final consonant, drop it
		return(root[:-1] + 'ku-')
	else:
		return(root + 'ku-')

def concessive(root): #apply @-ngr(ar)-
	specialte = False
	if root[-1] == '-': #remove dash
		root = root[:-1]
	if root[-2] == 't' and root[-1] == 'e' and specialte:
		return(root[:-2]+'lengrar-')
	elif root[-1] == 'r' or root[-1] == 'g':
		return(root[:-1]+'ngrar-')

def first_contemporative(root):
	if root[-1] == '-': #remove dash
		root = root[:-1]
	if root[-1] == 'g' or root[-1] == 'r':
		return(root[:-1] + 'ller-')
	else:
		return(root + 'ller')

def second_contemporative(root):
	pass

def apply_ending(root):
	if root[-1] == '-': #if ending has a dash
		root = root[:-1]
	if int31: #if ending is intransitive 3rd person 1 (singular)
		pass
	if int32: #if ending is intransitive 3rd person 2 (dual)
		pass
	if int33: #if ending is intransitive 3rd person 3 (plural)
		pass
	if int11: #if ending is intransitive 1st person 1 (singular)
		if concessive_flag:
			root = root[:-3] # remove the ar- case page 292
			if root[-2] in consonants:# or if letter before ng root[-2] is stressed_vowel:
				return(root + 'erma') #don't geminate
			else:
				return(root + "'erma")
		return(root+'ma')
	if int12: #if ending is intransitive 1st person 2 (dual)
		if root[-1] == 'g' or root[-1] == 'r':
			return(root[:-1]+'mta')
		else:
			return(root+'mta')
	if int13: #if ending is intransitive 1st person 3 (plural)
		if root[-1] == 'g' or root[-1] == 'r':
			return(root[:-1]+'megnuk')
		else:
			return(root+'megnuk')
	if int21: #if ending is intransitive 2nd person 1 (singular)
		pass #concessive is interesting?
	if int22: #if ending is intransitive 2nd person 2 (dual)
		pass #concessive is interesting?
	if int23: #if ending is intransitive 2nd person 3 (plural)
		pass #concessive is interesting?
	if int41: #if ending is intransitive 4th person 1 (singular)
		pass #concessive is interesting?
	if int42: #if ending is intransitive 4th person 2 (dual)
		pass #concessive is interesting?
	if int43: #if ending is intransitive 4th person 3 (plural)
		pass #concessive is interesting?

def apply_connective_mood(word):
	if precessive_flag:
		return(precessive(word))
	elif consequential_flag:
		return(consequential(word))
	elif contingent_flag:
		return(contingent(word))
	elif conditional_flag:
		return(conditional(word))
	elif concessive_flag:
		return(concessive(word))
	elif first_contemporative_flag:
		return(first_contemporative(word))
	elif second_contemporative_flag:
		return(second_contemporative(word))
	else: 
		return(indicative(word))

for word in root_examples:
	word1 = apply_connective_mood(word)
	final = apply_ending(word1)

	#drop hatted e
	
	if isShort(word): #add apostrophe if not in geminated VCVV or CVCVV form already
		if final[0] in vowels and final[1] in consonants and final[2] in vowels and final[3] in consonants and final[4] in vowels:
			final = final[0:2]+"'"+final[2:]
		elif final[0] in consonants and final[1] in vowels and final[2] in consonants and final[3] in vowels and final[4] in consonants and final[5] in vowels:
			final = final[0:3]+"'"+final[3:]
	
	print(final)


