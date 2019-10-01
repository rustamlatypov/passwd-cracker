import argparse
import hashlib
import multiprocessing
from joblib import Parallel, delayed
from tqdm import tqdm

import dictionary
import hybrid



def crack(i):
    for s, h in H:
        encrypted = hashlib.sha256((i+s).encode('utf-8')).hexdigest()
        if encrypted == h:
            print(s + ':' + h, i, '\n')



def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('a', metavar='attacktype', type=str, choices={'d','h'})
	parser.add_argument('h', metavar='hashfile', type=str)
	parser.add_argument('w', metavar='wordfile', type=str)
	args = parser.parse_args()

	atype = args.a
	hlist = '../res/' + args.h
	wlist = '../res/' + args.w

	H = set()
	with open(hlist) as f:
	    for line in f:
	        l = line.strip().split(':')
	        H.add(tuple(l))


	W = set()
	if atype == 'd':
		W = dictionary.get_wordlist(wlist)
	elif atype == 'h':
		W = hybrid.get_wordlist(wlist)


	def crack(i):
	    for s, h in H:
	        encrypted = hashlib.sha256((i+s).encode('utf-8')).hexdigest()
	        if encrypted == h:
	            print(s + ':' + h, i, '\n')


	inputs = tqdm(W)
	num_cores = multiprocessing.cpu_count()
	processed_list = Parallel(n_jobs=num_cores)(delayed(crack)(i) for i in inputs)


main()