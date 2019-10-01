from itertools import combinations

# toggle last character
def c1(word): 
	if word[-1].isupper():
		return word[:-1] + word[-1].lower()
	else:
		return word[:-1] + word[-1].upper()

# toggle first character
def c2(word): 
	if word[0].isupper():
		return word[0].lower() + word[1:]
	else:
		return word[0].upper() + word[1:]

def c3(word): return word + "0"
def c4(word): return word + "1"
def c5(word): return word + "7"
def c6(word): return "0" + word
def c7(word): return "1" + word
def c8(word): return "7" + word
def c9(word): return word + word
def c10(word): return word[::-1]
def c11(word): return word.replace('I','1').replace('i','1')
def c12(word): return word.replace('E','3').replace('e','3')
def c13(word): return word.replace('A','4').replace('a','4')
def c14(word): return word.replace('O','0').replace('o','0')

# uppercase every odd character
def c15(word):
    w = ''; i = 0
    for c in word:
        if i%2==0:
            w += c.upper(); i += 1
        else:
            w += c; i += 1
    return w

# uppercase every even character
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
	
	
	# list of permutations for the algorithm to go through
	func = [c1,c2,c3,c4]
	perm_list = sum([list(map(list, combinations(func, i))) for i in range(len(func) + 1)], [])

	# permutate every word in the .txt file
	W = set()
	for word in D:
		for comb in perm_list:
			temp = word
			if not comb:
				W.add(temp)
			else:
				for ac in comb:
					temp = ac(temp)
				W.add(temp)

	return W






