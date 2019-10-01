import argparse
import hashlib
import multiprocessing
import dictionary
import hybrid
import brute
import sys
from joblib import Parallel, delayed
from tqdm import tqdm
from itertools import combinations

parser = argparse.ArgumentParser()
   
# -a: attack mode
# dic: dictionary
parser.add_argument('-a', type=str, choices={'b','d','h'})
parser.add_argument('-hf', metavar='hashfile', type=str)
parser.add_argument('-wf', metavar='wordfile', type=str)
args = parser.parse_args()

atype = args.a
hlist = '../res/' + args.hf
if atype != 'b':
	wlist = '../res/' + args.wf

H = []
with open(hlist) as f:
    for line in f:
        l = line.strip().split(':')
        H.append(l)

W = set()

if atype == 'b':
	W = brute.get_wordlist()
elif atype == 'd':
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