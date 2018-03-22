#removes the page headers
from collections import defaultdict
with open('Nelson_Island_Stories_yupik_edit.txt','r') as fdata:
	with open('Nelson_Island_Stories_yupik_edit_1.txt','w') as fout:
		for line in fdata:
			splitted = line.split()
			for word in splitted:
				if '.' in word or '!' in word or '?' in word:
					fout.write(word)
					fout.write('\n')
				else:
					fout.write(word)
				fout.write(' ')