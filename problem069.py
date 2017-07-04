# this takes too long to run... try just multiplying as many primes as possible while staying below 1000000. Gives you 510510.

import math

primes = []
factors = [[], []]

rangemax = 1000001

for n in xrange(2,rangemax):
	m = n
	prime = True
	factors.append([])
	for p in primes:
		if p > n:
			break
		if n % p == 0:
			prime = False
			power = 1
			while n % p**power == 0:
				power += 1
			n /= p**(power-1)
			if len(factors[m]) == 0:
				factors[m].append(p)
			elif factors[m][-1] != p:
				factors[m].append(p)
	if prime:
		primes.append(n)
		factors[n].append(n)
	if m % 1000 == 0:
		print m

print "Found primes and factors"

relprimes = [[], []]
ratios = [0,0]

for n in xrange(2, rangemax):
	if len(factors[n]) < 4:
		ratios.append(0)
		continue
	relprimes.append([])
	for x in xrange(1, n):
		relprime = True
		for xfactor in factors[x]:
			for nfactor in factors[n]:
				if xfactor == nfactor:
					relprime = False
					break
		if relprime:
			relprimes[n].append(x)
	ratios.append(float(n)/len(relprimes[n]))
	if n % 1000 == 0:
		print n

m = max(ratios)
for n in xrange(2, rangemax):
	if ratios[n] == m:
		print n