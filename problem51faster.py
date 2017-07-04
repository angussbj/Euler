def isprime(n):
	s = math.sqrt(n)
	for p in primes:
		if p > s:
			return True
		if n % p == 0:
			return False

import math
import itertools
from bisect import bisect_left
import sys

primes = []
n = 2
while True:
	prime = True
	for p in primes:
		if p > math.sqrt(n):
			break
		if n%p == 0:
			prime = False
			break
	if prime:
		primes.append(n)
		plst = list(str(n))
		perms = list(itertools.product([0,1], repeat = len(plst)-1))
		del perms[0]
		if int(plst[0]) != 1: 				#not necessary to consider primes that have already been considered as part of a smaller prime collection (first digit consideration)
			i = 0
			while i < len(perms):
				if perms[i][0] == 1:
					del perms[i]
				else:
					i += 1
		for j in xrange(1, len(plst)-1):	#same idea considering other digits indexed by j
			if int(plst[j]) > 1:
				i = 0
				while i < len(perms):
					if perms[i][j] == 1:
						del perms[i]
					else:
						i += 1
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
				newint = int(''.join(newlst))
				if isprime(newint):
					pset.append(newint)
				# if newint <= primes[-1]:
				# 	pos = bisect_left(primes, newint, 0, len(primes)-1) #Finds the position in the ordered list above that newint should be inserted to maintain order
				# 	if primes[pos] == newint:							#Iff this position holds a prime equal to newint, then newint is prime
				# 		pset.append(newint)
				# else:
				# 	isprime = True
				# 	for p in primes:
				# 		if p > math.sqrt(newint):
				# 			break
				# 		if newint%p == 0:
				# 			isprime = False
				# 			break
				# 	if isprime:
				# 		pset.append(newint)
			if len(pset) == 8:
				print pset
				sys.exit()
	n += 1
	if n % 1000 == 0:
		print n