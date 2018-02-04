# coding: utf-8
#test
import re
root_examples = ['alinge-','ane-','aqui-','assir-','aurre-','ayag-','cali-','ce+irte-','cuka-','elite-','inarte-','iqvar-','kaig-','kuimar-','nere-','qalarte-','qavar-','qia-','tai-','taqe-','tuqu-','yurar-']
vowels = ['a','e','i','u']
high_vowels = ['i','u']
front_vowels = ['i']
mid_vowels = ['e']
low_vowels = ['a']
back_vowels = ['u']
#letter entry can contain multiple letters right now, but am hoping to represent it by single character
#vv = 1
#ll = 2
#ss = 3
#gg = 4
#rr = 5
#ng = 6
#μ = m2 = 7
#+ = n2 = 8
#TMg = ng2 = 9
#¥r = rounded ur = j
#¥rr = rounded urr = z 
#¥g = rounded ug = x
#¥k = rounded uk = h
#¥q = rounded uq = d
consonants = ['p','t','c','k','q','v','l','s','y','g','w','r','m','n','1','2','3','4','5','6','7','8','9','j','z','x','h','d']
stops = ['p','t','c','k','q']
voiced_fricatives = ['v','l','s','y','g','r']
voiceless_fricatives = ['1','2','3','4','5']
voiced_nasals = ['m','n','6']
voiceless_nasals = ['7','8','9']
labials = ['p','v','1','m','7']
apicals = ['t','l','2','n','8','c','s','y','3']
front_velars = ['k','g','4','6','9']
back_velars = ['q','r','5']
def is_english(word):
	#does word contain non-Yup'ik consonants, then it is probably English
	return True
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
def isVowel(letter):
	if letter in vowels:
		return True
	else:
		return False
def isConsonant(letter):
	if letter in consonants:
		return True
	else:
		return False
def isSingleSyllable(word):
	if len(word) > 3:
		return False
	else:
		return True
def third_person_singular(word):
	#first check if e is last letter
	word = word[:-1]
	if word[-1] == 'e':
		word = word[:-1]
		#rule case for +' ASSUMING ONLY APPLIES TO E- ENDINGS ????????????CHNGE NOT ALL SINGLE SYLLABLES END IN E?????????????
		if isSingleSyllable(word):
			return(word+"'uq")
		#return(word+"uq$$$$$$")
	#rule case for +g
	if isVowel(word[-1]) and isVowel(word[-2]):
		return(word+"guq")
	#rule case for +t
	if word[-1] == 'g' or word[-1] == 'r':
		return(word+"tuq")
	#no special rule case
	return(word+"uq")
def third_person_dual(word):
	#first check if e is last letter
	word = word[:-1]
	if word[-1] == 'e':
		word = word[:-1]
		#rule case for +' ASSUMING ONLY APPLIES TO E- ENDINGS
		if isSingleSyllable(word):
			return(word+"'uk")
		#return(word+"uk$$$$$$")
	#rule case for +g
	if isVowel(word[-1]) and isVowel(word[-2]):
		return(word+"guk")
	#rule case for +t
	if word[-1] == 'g' or word[-1] == 'r':
		return(word+"tuk")
	#no special rule case
	return(word+"uk")
def third_person_plural(word):
	#first check if e is last letter
	word = word[:-1]
	if word[-1] == 'e':
		word = word[:-1]
		#rule case for +' ASSUMING ONLY APPLIES TO E- ENDINGS
		if isSingleSyllable(word):
			return(word+"'ut")
		#return(word+"ut$$$$$$")
	#rule case for +g
	if isVowel(word[-1]) and isVowel(word[-2]):
		return(word+"gut")
	#rule case for +t
	if word[-1] == 'g' or word[-1] == 'r':
		return(word+"tut")
	#no special rule case
	return(word+"ut")
def first_person_singular(word):
	#first check if e is last letter
	word = word[:-1]
	if word[-1] == 'e':
		word = word[:-1]
		#rule case for +' ASSUMING ONLY APPLIES TO E- ENDINGS
		if isSingleSyllable(word):
			if isVowel(word[-1]):
				return(word+"'u6a")
			else:
				return(word+"'ua")
	#rule case for +g MUST VELAR DROP AFTER G
	if isVowel(word[-1]) and isVowel(word[-2]):
		return(word+"gua")
	#rule case for +t
	if word[-1] == 'g' or word[-1] == 'r':
		return(word+"tua")
	#no special rule case MUST VELAR DROP AFTER T
	if isVowel(word[-1]):
		return(word+"u6a")
	else:
		return(word+"ua")
def first_person_dual(word):
	#first check if e is last letter
	word = word[:-1]
	if word[-1] == 'e':
		word = word[:-1]
		#rule case for +' ASSUMING ONLY APPLIES TO E- ENDINGS
		if isSingleSyllable(word):
			return(word+"'ukuk")
		#return(word+"ukuk$$$$$$")
	#rule case for +g
	if isVowel(word[-1]) and isVowel(word[-2]):
		return(word+"gukuk")
	#rule case for +t
	if word[-1] == 'g' or word[-1] == 'r':
		return(word+"tukuk")
	#no special rule case
	return(word+"ukuk")
def first_person_plural(word):
	#first check if e is last letter
	word = word[:-1]
	if word[-1] == 'e':
		word = word[:-1]
		#rule case for +' ASSUMING ONLY APPLIES TO E- ENDINGS
		if isSingleSyllable(word):
			return(word+"'ukut")
		#return(word+"ukut$$$$$$")
	#rule case for +g
	if isVowel(word[-1]) and isVowel(word[-2]):
		return(word+"gukut")
	#rule case for +t
	if word[-1] == 'g' or word[-1] == 'r':
		return(word+"tukut")
	#no special rule case
	return(word+"ukut")
def second_person_singular(word):
	#first check if e is last letter
	word = word[:-1]
	if word[-1] == 'e':
		word = word[:-1]
		#rule case for +' ASSUMING ONLY APPLIES TO E- ENDINGS
		if isSingleSyllable(word):
			return(word+"'uten")
		#return(word+"ukuk$$$$$$")
	#rule case for +g
	if isVowel(word[-1]) and isVowel(word[-2]):
		return(word+"guten")
	#rule case for +t
	if word[-1] == 'g' or word[-1] == 'r':
		return(word+"tuten")
	#no special rule case
	return(word+"uten")
def second_person_dual(word):
	#first check if e is last letter
	word = word[:-1]
	if word[-1] == 'e':
		word = word[:-1]
		#rule case for +' ASSUMING ONLY APPLIES TO E- ENDINGS
		if isSingleSyllable(word):
			return(word+"'utek")
		#return(word+"ukuk$$$$$$")
	#rule case for +g
	if isVowel(word[-1]) and isVowel(word[-2]):
		return(word+"gutek")
	#rule case for +t
	if word[-1] == 'g' or word[-1] == 'r':
		return(word+"tutek")
	#no special rule case
	return(word+"utek")
def second_person_plural(word):
	#first check if e is last letter
	word = word[:-1]
	if word[-1] == 'e':
		word = word[:-1]
		#rule case for +' ASSUMING ONLY APPLIES TO E- ENDINGS
		if isSingleSyllable(word):
			return(word+"'uci")
		#return(word+"ukuk$$$$$$")
	#rule case for +g
	if isVowel(word[-1]) and isVowel(word[-2]):
		return(word+"guci")
	#rule case for +t
	if word[-1] == 'g' or word[-1] == 'r':
		return(word+"tuci")
	#no special rule case
	return(word+"uci")
def apply_past(word):
	word = word[:-1]
	if word[-1] == 'g' or word[-1] == 'r':
		return(word[:-1]+"2ru-")
	return(word+"2ru-")
def apply_negation(word):
	word = word[:-1]
	if word[-1] == 'g' or word[-1] == 'r':
		return(word[:-1]+"nrite-")
	return(word+"nrite-")
def apply_want(word):
	word = word[:-1]
	if word[-1] == 'e':
		word = word[:-1]
	#print(word)
	if word[-1] == 'p' or word[-1] == 'c' or word[-1] == 'k' or word[-1] == 'q' or word[-1:] == '1' or word[-1:] == '2' or word[-1:] == '3' or word[-1:] == '4' or word[-1:] == '5':
		return(word+"sug-")
	if word[-1:] == 't':
		return(word[:-1]+"cug-")
	return(word+"yug-")
#def apply_make(word):
#	word = word[:-1]
#	#if word[-1] == 'e':
#	#	word = word[:-1]
#	if word[-1] == 'g' or word[-1] == 'r':
#		return(word[:-1]+"li-")
#	return(word+"li-")
for word in root_examples:
	word = convert(word)
	print('\n')
	print(word)
	print(third_person_singular(word))
	print(first_person_singular(word))
	print(third_person_dual(word))
	print(third_person_plural(word)+'\n')
	print(first_person_singular(word))
	print(first_person_dual(word))
	print(first_person_plural(word)+'\n')
	print(second_person_singular(word))
	print(second_person_dual(word))
	print(second_person_plural(word))
	make = False
	want = False
	past = True
	negation = True
	#print(second_person_plural(apply_negation(apply_past(apply_want(apply_make(word))))))
	#if make:
	#	word = apply_make(word)
	if want:
		word = apply_want(word)
	if past:
		word = apply_past(word)
	if negation:
		word = apply_negation(word)
	word = deconvert(word)
	print(second_person_plural(word))
