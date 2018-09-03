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
b11="ate"
b12='aqui'
b13='kipute'
b14="kite"
b15='nangte'
b16='apte'
b17='ce8irte'
b18='miili'
b19='taqe'
#wordlist = [b13,b16]

postbases = ['+(s)ciigali-','+(s)ciigate-','+ciqe-','@ciiqe-','-ksaite-','-lar-','-llini-','-llru-','@~+ngaite-','@~+niarar-','-nqigte-','-nrir-','-nrite-','-nru-','-qatar-','-qcaar(ar)-','-sqe-','-ssiyaag-','@~+yaaqe-','@~+yarpiar-','@~+yartur-','@~+yug-','@~+yugar-','@~+yugnairute-','@~+yugnarqe-','@~+yugnga-','@~-yuite-','@~+yunqegg-','@~+yuumiir(ar)te-','@~+yuumite-','@~+yuumir-','-ngnaqe-'] #'\%(e)sqe-'

wordlist = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19]

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

a = "+'(g/t)u:6a" #3rdperson singular intrans
b = "+'(g)aanga"  #3rd person singular 3rd person object singular
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
endings=["+'(g/t)u:6a", "+'(g/t)ukuk","+'(g/t)ukut","+'(g/t)uten","+'(g/t)utek","+'(g/t)uci","+'(g/t)uq","+'(g/t)uk","+'(g/t)ut","+'(g)amken","+'(g)amtek","+'(g)amci","+'(g)aqa","+'(g)agka","+'(g)anka","+'(g)amegten","+'(g)amegtek","+'(g)amegci","+'(g)apuk","+'(g)agpuk","+'(g)apuk","+'(g)amteggen","+'(g)amcetek","+'(g)amceci","+'(g)aput","+'(g)agput","+'(g)aput","+'(g)arpenga","+'(g)arpekuk","+'(g)arpekut","+'(g)an","+'(g)agken","+'(g)aten","+'(g)arpetegnga","+'(g)arpetegkuk","+'(g)arpetegkut","+'(g)atek","+'(g)agtek","+'(g)atek","+'(g)arpecia","+'(g)arpecikuk","+'(g)arpecikut","+'(g)aci","+'(g)agci","+'(g)aci","+'(g)anga","+'(g)akuk","+'(g)akut","+'(g)aten","+'(g)atek","+'(g)aci","+'(g)aa","+'(g)ak","+'(g)ai","+'(g)agnga","+'(g)agkuk","+'(g)agkut","+'(g)agten","+'(g)agtek","+'(g)agci","+'(g)aak","+'(g)agkek","+'(g)akek","+'(g)atnga","+'(g)aitkuk","+'(g)aitkut","+'(g)atgen","+'(g)aicetek","+'(g)aiceci","+'(g)aat","+'(g)agket","+'(g)ait",]
interrogative_endings = ["~+(t)sia",  "@~+ceuk", "@~+ceta", "~+(t)sit", "@~+cetek",  "@~+ceci", "+'(g/t)a", "+'(g/t)ak", "+'(g/t)at","~+(t)sia","~+(t)sikuk","~+(t)sikut","~+(t)siu","~+(t)sikek","~+(t)siki","@~+cetegenga","@~+cetegkuk","@~+cetegkut","@~+cetegnegu","@~+cetegkek","@~+cetegki","@~+cecia","@~+cecikuk","@~+cecikut","@~+ceciu","@~+cecikek","@~+ceciki","+'(g/t)anga","+'(g/t)akuk","+'(g/t)akut","+'(g/t)aten","+'(g/t)atek","+'(g/t)aci","+'(g/t)a:gu","+'(g/t)akek","+'(g/t)aki","+'(g/t)agnga","+'(g/t)agkuk","+'(g/t)agkut","+'(g/t)agten","+'(g/t)agtek","+'(g/t)agci","+'(g/t)agnegu","+'(g/t)agkek","+'(g/t)agki","+'(g/t)atnga","+'(g/t)atkuk","+'(g/t)atkut","+'(g/t)atgen","+'(g/t)acetek","+'(g/t)aceci","+'(g/t)atgu","+'(g/t)atkek","+'(g/t)atki"]
optative_endings = ["$","&","@~+lii", "@~+luk", "-lta", "@+tek", "@+ci", "@~+li", "@~+lik", "@~+lit","@~+lamken","@~+lamtek", "@~+lamci","@~+laku","@~+lakek", "@~+laki","@~+lamegten","@~+lamegtek", "@~+lamegci","@+lauk","@+lagpuk", "@+lapuk","@~+lamteggen","@~+lamcetek", "@~+lamceci","@+laut","@+lagput", "@+laput","@+nga","@+kuk","@+kut","@+", "@+kek","@+ki","@+tegnga","@+tegkuk","@+tegkut","@+tegu","@+tegkek","@+tegki","@+cia","@+cikuk","@+cikut","@+ciu","@+ciki","@+cikek","@~+linga","@~+likuk","@~+likut","@~+liten","@~+litek","@~+lici","@~+liku","@~+likek","@~+liki","@~+lignga","@~+ligkuk","@~+ligkut","@~+ligten","@~+ligtek","@~+ligci","@~+ligtegu","@~+ligtegkek","@~+ligtegki","@~+litnga","@~+litkuk","@~+litkut","@~+litgen","@~+licetek","@~+liceci","@~+lignegu","@~+ligkek","@~+ligki"]
subordinative_endings = ["@~+lua", "@~+lunuk", "@~+luta", "@~+luten", "@~+lutek", "@~+luci", "@~+luni", "@~+lutek", "@~+luteng","@~+luten","@~+lutek", "@~+luci","@~+luku","@~+lukek", "@~+luki","@~+luten","@~+lutek", "@~+luci","@~+luku","@~+lukek", "@~+luki","@~+luten","@~+lutek", "@~+luci","@~+luku","@~+lukek", "@~+luki","@~+lua","@~+lunuk", "@~+luta","@~+luku","@~+lukek", "@~+luki","@~+lua","@~+lunuk", "@~+luta","@~+luku","@~+lukek", "@~+luki","@~+lua","@~+lunuk", "@~+luta","@~+luku","@~+lukek", "@~+luki","@~+lua","@~+lunuk", "@~+luta","@~+luten","@~+lutek", "@~+luci","@~+luku","@~+lukek", "@~+luki","@~+lua","@~+lunuk", "@~+luta","@~+luten","@~+lutek", "@~+luci","@~+luku","@~+lukek", "@~+luki","@~+lua","@~+lunuk", "@~+luta","@~+luten","@~+lutek", "@~+luci","@~+luku","@~+lukek", "@~+luki"]
#interrogative_endings = ["$","&","+'(g/t)a:gu"]
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
	for ending in optative_endings:
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



# let interrogative_intransitive_endings = { 

#  "~+(t)sia",  "@~+ceuk", "@~+ceta",
#  "~+(t)sit", "@~+cetek",  "@~+ceci",
#  "+'(g/t)a", "+'(g/t)ak", "+'(g/t)at",
# "~+(t)sia","~+(t)sikuk","~+(t)sikut",
# "~+(t)siu","~+(t)sikek","~+(t)siki",
# "@~+cetegenga","@~+cetegkuk","@~+cetegkut","@~+cetegnegu","@~+cetegkek","@~+cetegki",
# "@~+cecia","@~+cecikuk","@~+cecikut",
# "@~+ceciu","@~+cecikek","@~+ceciki",
# "+'(g/t)anga","+'(g/t)akuk","+'(g/t)akut",
# "+'(g/t)aten","+'(g/t)atek","+'(g/t)aci",
# "+'(g/t)a:gu","+'(g/t)akek","+'(g/t)aki",
# "+'(g/t)agnga","+'(g/t)agkuk","+'(g/t)agkut",
# "+'(g/t)agten","+'(g/t)agtek","+'(g/t)agci",
# "+'(g/t)agnegu","+'(g/t)agkek","+'(g/t)agki",
# "+'(g/t)atnga","+'(g/t)atkuk","+'(g/t)atkut",
# "+'(g/t)atgen","+'(g/t)acetek","+'(g/t)aceci",
# "+'(g/t)atgu","+'(g/t)atkek","+'(g/t)atki"
# let optative_intransitive_endings = { 

# "@~+lii", "@~+luk", "-lta",
#  "@+tek", "@+ci",,
#  "@~+li", "@~+lik", "@~+lit",
# "@~+lamken","@~+lamtek", "@~+lamci",
# "@~+laku","@~+lakek", "@~+laki",
# "@~+lamegten","@~+lamegtek", "@~+lamegci",
# "@+lauk","@+lagpuk", "@+lapuk",
# "@~+lamteggen","@~+lamcetek", "@~+lamceci",
# "@+laut","@+lagput", "@+laput",
# "@+nga","@+kuk","@+kut",
# "@+", "@+kek","@+ki",
# "@+tegnga","@+tegkuk","@+tegkut",
# "@+tegu","@+tegkek","@+tegki",
# "@+cia","@+cikuk","@+cikut",
# "@+ciu","@+ciki","@+cikek",
# "@~+linga","@~+likuk","@~+likut",
# "@~+liten","@~+litek","@~+lici",
# "@~+liku","@~+likek","@~+liki",
# "@~+lignga","@~+ligkuk","@~+ligkut",
# "@~+ligten","@~+ligtek","@~+ligci",
# "@~+ligtegu","@~+ligtegkek","@~+ligtegki",
# "@~+litnga","@~+litkuk","@~+litkut",
# "@~+litgen","@~+licetek","@~+liceci",
# "@~+lignegu","@~+ligkek","@~+ligki"
# let subordinative_intransitive_endings = {  
# "@~+lua", "@~+lunuk", "@~+luta",
#  "@~+luten", "@~+lutek", "@~+luci",
#  "@~+luni", "@~+lutek", "@~+luteng",
# "@~+luten","@~+lutek", "@~+luci",
# "@~+luku","@~+lukek", "@~+luki",
# "@~+luten","@~+lutek", "@~+luci",
# "@~+luku","@~+lukek", "@~+luki",
# "@~+luten","@~+lutek", "@~+luci",
# "@~+luku","@~+lukek", "@~+luki",
# "@~+lua","@~+lunuk", "@~+luta",
# "@~+luku","@~+lukek", "@~+luki",
# "@~+lua","@~+lunuk", "@~+luta",
# "@~+luku","@~+lukek", "@~+luki",
# "@~+lua","@~+lunuk", "@~+luta",
# "@~+luku","@~+lukek", "@~+luki",
# "@~+lua","@~+lunuk", "@~+luta",
# "@~+luten","@~+lutek", "@~+luci",
# "@~+luku","@~+lukek", "@~+luki",
# "@~+lua","@~+lunuk", "@~+luta",
# "@~+luten","@~+lutek", "@~+luci",
# "@~+luku","@~+lukek", "@~+luki",
# "@~+lua","@~+lunuk", "@~+luta",
# "@~+luten","@~+lutek", "@~+luci",
# "@~+luku","@~+lukek", "@~+luki"
