import math
import itertools
from bisect import bisect_left
import sys

primes = []
a = 2
b = 100000
while True:
	for n in xrange(a,b):
		prime = True
		for p in primes:
			if p > math.sqrt(n):
				break
			if n%p == 0:
				prime = False
				break
		if prime:
			primes.append(n)

	for p in primes:
		if p >= a:
			pstr = str(p)
			plst = list(pstr)
			perms = list(itertools.product([0,1], repeat = len(pstr)-1))
			for perm in perms:
				pset = []
				for x in xrange(10):
					if len(perm) != 0:
						if perm[0] == 1 and x == 0:
							continue
					newlst = plst
					for pos in xrange(len(perm)):
						if perm[pos] == 1:
							newlst[pos] = str(x)
					newstr = ''.join(newlst)
					newint = int(newstr)
					pos = bisect_left(primes, newint, 0, len(primes)-1) #Finds the position in the ordered list above that newint should be inserted to maintain order
					if primes[pos] == newint:							#Iff this position holds a prime equal to newint, then newint is prime
						pset.append(newint)
				if len(pset) == 6:
					print pset
					sys.exit()
	a = b
	b *= 10





