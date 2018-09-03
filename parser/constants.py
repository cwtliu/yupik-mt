# *-* encoding:utf-8 *-*

vowels = ['a','e','i','u']
high_vowels = ['i','u']
front_vowels = ['i']
mid_vowels = ['e']
low_vowels = ['a']
back_vowels = ['u']
prime_vowels = ['a','i','u']
voiced_converter = {'v':'1','l':'2','s':'3','g':'4','r':'5','n':'8','m':'7','6':'9'}
voiceless_converter = {'1':'v','2':'l','3':'s','4':'g','5':'r','8':'n','7':'m','9':'6'}

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
fricatives = ['v','l','s','y','g','r','1','2','3','4','5']
voiced_nasals = ['m','n','6']
voiceless_nasals = ['7','8','9']
nasals = ['m','n','6','7','8','9']
labials = ['p','v','1','m','7']
apicals = ['t','l','2','n','8','c','s','y','3']
front_velars = ['k','g','4','6','9']
back_velars = ['q','r','5']
