from postbase import Postbase
from parser import *
from spellcheck import *
b1='utaqa'
b2='kiu'
b3='kegge'
b4='ige'
b5='emute'
b6='kenugte'
b7='narug'
b8='nayur'
b9='tangerr'
b10='eceg'
b11="at'e"
b12='nerenrite'
b13='kipute'
b14="kit'e"
b15='nangte'
b16='apte'
b17='ce8irte'
b18='maante'
#wordlist = [b13,b16]

postbases = ['+(s)ciigali-','+(s)ciigate-','+ciqe-','@ciiqe-','-ksaite-','-lar-','-llini-','-llru-','@~+ngaite-','@~+niarar-','-nqigte-','-nrir-','-nrite-','-nru-','-qatar-','-qcaar(ar)-','-sqe-','-ssiyaag-','@~+yaaqe-','@~+yarpiar-','@~+yartur-','@~+yug-','@~+yugar-','@~+yugnairute-','@~+yugnarqe-','@~+yugnga-','@~-yuite-','@~+yunqegg-','@~+yuumiir(ar)te-','@~+yuumite-','@~+yuumir-','-ngnaqe-'] #'\%(e)sqe-'

wordlist = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18]


# a = "+'(g/t)uq"
# b = "-llruuq"
# c = "+'(g)ait"
# d = "(g)i"
# e = "g(i)u"
# f = "@~+yugtuq"
# g = "@~+(t)vailegma"
# h = "@~+niuq"
# i = "@~-kuma"
# j = "@~+luni"
# k = "@~:(u)tuk"
# l = "@~:(u)ciq"

a = "+'(g/t)uq" #3rdperson singular intrans
b = "+'(g)aa"  #3rd person singular 3rd person object singular
c = "+'(g/t)at" #3rd person interrogative plural
d = "+'(g/t)atgu"  #3rd person plural, third person singular object
e = "~+(t)siki"  #2nd person ubject singular, 3rd person plural object
f = "@~+cetegnegu"  #2nd person dual subject third persun singular object
g = "@~+liki"  #3rd person singular, 3rd person plural obejct optative
h = "@~+lii"  #1st person singular optative
i = "@~+laku"  #1st person singular 3rd person singular optative
j = "-lta"  #1st person plural
k = "@~+luk"  #1st person dual
l = "@+ci"  #2nd person plural
m = "@+tegu"  #2nd person dual, 3rd person singular
n = ""  
o = ""
p = "@~+luni"  #subordinative 4th person singular
q = "@~+luku"
r = ""
s = '-lria'  
t = '+ssuun'
u = '+cuun'
v = '-tuli'
w = '@~+yaraq'
x = '@~-yuli'
y = '-lleq'
z = ''

c0 = "@~+(t)vaileg-"
c1="@~:(ng)a-"
c2="+'(g)aqa-"
c3="@+ngr(ar)-"
c4="@~-ku-"
c5="-ller"
c6="@:(ng)inaner-"

#clist = [c0,c1,c2,c3,c4,c5,c6]
clist=[c0]


ce1 = "aku"
ce2 = "-mkek"
ce3 = "-vgu"
ce4 = "+megnegu"

celist = [ce1,ce2,ce3,ce4]

endings = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
#endings=[a]

suffix = []
connective_suffix = []
# for word in wordlist:
# 	for postbase in postbases:
# 		for ending in endings:
# 			word = convert(word)
# 			postbase = convert(postbase)
# 			ending = convert(ending)
# 			suffix.append([word, postbase, ending])
for word in wordlist:
	for ending in endings:
		word = convert(word)
		ending = convert(ending)
		suffix.append([word, ending])
# for word in wordlist:
# 	for postbase in clist:
# 		for ending in celist:
# 			word = convert(word)
# 			postbase = convert(postbase)
# 			ending = convert(ending)
# 			connective_suffix.append([word, postbase, ending])
for items in suffix:
	for i, key in enumerate(items):
		if i == 0:
			word = key
		else:
			p = Postbase(key)
			word = p.concat(word)
	word = deconvert(word)
	print('')
	print(deconvert(items[0])+' '+deconvert(items[1]))
	print(word)

	# if not spellcheck(word):
	# 	print('')
	# 	print(deconvert(items[0])+' '+deconvert(items[1]))
	# 	print(word)


