import math
from bisect import bisect_left
import itertools

primes = []

for n in xrange(2, 10000):
	prime = True
	for p in primes:
		if p > math.sqrt(n):
			break
		if n % p == 0:
			prime = False
			break
	if prime:
		primes.append(n)

pos = bisect_left(primes, 1000, lo = 0, hi = len(primes) - 1)
for i in xrange(pos, len(primes)):
	diglist = list(str(primes[i]))
	slpermutations = itertools.permutations(diglist)
	perms = []
	for slperm in slpermutations:
		perms.append(int(''.join(slperm)))
	j = 0
	while j < len(perms):
		for p in primes:
			if p > math.sqrt(perms[j]):
				break
			if perms[j] % p == 0:
				del perms[j]
				j -= 1
				break
		j += 1
	if len(perms) >= 3:
		combs = itertools.combinations(perms, 3)
		for comb in combs:
			if comb[0] != comb[1] and comb[0] != comb[2] and comb[1] != comb[2]:
				if comb[2] - comb[1] == comb[1] - comb[0]:
					print comb

