#checks punctuation between two files
from collections import defaultdict
import re
with open('Nelson_Island_Stories_yupik_edit_1.txt','r') as yupikdata:
	counter = 0
	yupik = []
	for line in yupikdata:
		counter+=1
		yupik.append(line)
with open('Nelson_Island_Stories_english_edit_1.txt','r') as englishdata:
	english = []
	for line in englishdata:
		english.append(line)
i = 650
for i in range(i,i+10):
	print("Yup'ik: {} English: {}".format(yupik[i], english[i]))
	print(" ")
