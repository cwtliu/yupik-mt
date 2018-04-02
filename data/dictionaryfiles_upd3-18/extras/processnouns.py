# -*- coding:utf-8 -*-
with open('root_nouns_rootform_edit_5.txt','r') as fin:
	with open('root_nouns_rootform_edit_6.txt','w') as fout:
		for line in fin:
			lined = line.rstrip()
			if '(' in lined:
				print(lined)
			# 	if lined[-1] == 't':
			# 		print(lined[:-1]+'r-')
			# 		fout.write(lined[:-1]+'r-')
			# 		fout.write('\n')
			# 	else:
			# 		fout.write(lined)
			# 		fout.write('\n')
			# else:
			# 	fout.write(lined)
			# 	fout.write('\n')
