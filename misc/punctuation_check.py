#checks punctuation between two files
from collections import defaultdict
import re
with open('Nelson_Island_Stories_yupik_edit_1.txt','r') as yupikdata:
	counter = 0
	yupik = []
	for line in yupikdata:
		counter+=1
		s = ""
		for w in line:
			if w == "!" or w == "?" or w == "." or w=="," or w==":":
				s += w
		yupik.append(s)
with open('Nelson_Island_Stories_english_edit_1.txt','r') as englishdata:
	english = []
	for line in englishdata:
		s = ""
		for w in line:
			if w == "!" or w == "?" or w == "." or w=="," or w==":":
				s += w
		english.append(s)
for i in range(counter):
	if yupik[i] != english[i]:
		print("Problem Line: {}".format(i+1))
		print("Yup'ik: {} English: {}".format(yupik[i], english[i]))
		break
