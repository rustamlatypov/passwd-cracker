import argparse
import hashlib
from tqdm import tqdm
from joblib import Parallel, delayed

import dictionary
import hybrid



def main():

	# parsing user input
	parser = argparse.ArgumentParser()
	parser.add_argument('a', metavar='attacktype', type=str, choices={'d','h'})
	parser.add_argument('h', metavar='hashfile', type=str)
	parser.add_argument('w', metavar='wordfile', type=str)
	args = parser.parse_args()

	atype = args.a
	hlist = '../res/' + args.h
	wlist = '../res/' + args.w

	# collecting (salt,hash) tuples into set H
	H = set()
	with open(hlist) as f:
	    for line in f:
	        l = line.strip().split(':')
	        H.add(tuple(l))

	# saving password guesses from the attack scripts into set W
	W = set()
	if atype == 'd':
		W = dictionary.get_wordlist(wlist)
	elif atype == 'h':
		W = hybrid.get_wordlist(wlist)


	def crack(i):
			for h, s in H:
			    encrypted = hashlib.sha256((i+s).encode('utf-8')).hexdigest()
			    if encrypted == h:
			        print(i + ':' + h + ':' + s, '\n')


	# creating a progress bar 
	inputs = tqdm(W)

	## Sequential
	# for i in inputs: crack(i) 

	## Parallel 
	Parallel(n_jobs=-1)(delayed(crack)(i) for i in inputs)

main()






