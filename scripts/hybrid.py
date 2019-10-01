from itertools import combinations

def c1(word): return word[:-1] + word[-1].upper()
def c2(word): return word.capitalize()
def c3(word): return word + "_0"
def c4(word): return word + "_1"
def c5(word): return word + "_7"
def c6(word): return "0_" + word
def c7(word): return "1_" + word
def c8(word): return "7_" + word
def c9(word): return word + word
def c10(word): return word[::-1]

def c11(word):
    w =  word.replace('I','1')
    return w.replace('i','1')

def c12(word):
    w = word.replace('E','3')
    return w.replace('e','3')

def c13(word):
    w = word.replace('A','4')
    return w.replace('a','4')

def c14(word):
    w = word.replace('O', '0')
    return w.replace('o','0')

# uppercase every even character
def c15(word):
    w = ''; i = 0
    for c in word:
        if i%2==0:
            w += c.upper(); i += 1
        else:
            w += c; i += 1
    return w

# uppercase every odd character
def c16(word):
    w = ''; i = 0
    for c in word:
        if i%2==1:
            w += c.upper(); i += 1
        else:
            w += c; i += 1
    return w


def get_wordlist(s):

	# going through the .txt file
	D = set()
	with open(s, encoding='latin-1') as f:
	    for line in f:
	        D.add(line.strip())
	
	# list of permutations to go through
	func = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16]
	todo = sum([list(map(list, combinations(func, i))) for i in range(len(func) + 1)], [])

	# permutate every word in the .txt file
	W = set()
	for word in D:
	    for comb in todo:
	        temp = word
	        if not comb:
	            W.add(temp)
	        for ac in comb:
	            w = ac(temp)
	            W.add(w)

	return W






