
vowels = ['a','e','i','u']
consonants = ['p','t','c','k','q','v','l','s','y','g','r','m','n','g']
with open('allnouns.txt','r') as fdata:
    with open('allnouns_root.txt','w') as fout:
    	for line in fdata:
    		flag = False
    		line = line.strip()
    		line = line.replace(' ','')
    		fout.write(line)
    		if line[-1:] == '*':
    			line = line[:-1]
    			flag = True
    		if line[-1:] == 'k':
    			fout.write(line[:-1])
    			fout.write('g-')
    		if line[-1:] == 'q':
    			fout.write(line[:-1])
    			fout.write('r-')
    		if line[-1:] == 'i':
    			fout.write(line)
    			fout.write('-')
    		if line[-1:] == 'u':
    			fout.write(line)
    			fout.write('-')
    		if line[-1:] == 'a':
    			fout.write(line)
    			fout.write('-')
    		if len(line) > 1:
      			if line[-1:] == 'n' and line[-2] in vowels:
    				fout.write(line[:-2])
    				fout.write(line[-2])
    				fout.write('te-')
    			if line[-2:] == 'ae':
    				fout.write(line[:-2])
    				fout.write('e-')
    		if len(line) > 2:
    			if line[-2:] == 'ta' and line[-3] in consonants:
    				fout.write(line[:-3])
    				fout.write(line[-3])
    				fout.write('te-')
    		if len(line) > 5:
    			if line[-5:] == '(aq*)':
    				fout.write(line[:-5])
    				fout.write('ar-')
    				flag = True
    		if flag:
    			fout.write('*')
    		fout.write('\n')


    
