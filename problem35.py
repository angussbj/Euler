import math
from bisect import bisect_left

primes = []

for n in xrange(2, 1000000):
	prime = True
	for p in primes:
		if p > math.sqrt(n):
			break
		if n % p == 0:
			prime = False
			break
	if prime:
		primes.append(n)

print "found ", len(primes), " primes"

count = 0
for p in primes:
	diglist = list(str(p))
	rotations = [p]
	for x in xrange(1, len(diglist)):
		r = []
		for i in xrange(0, len(diglist)):
			r.append(diglist[(i+x)%len(diglist)])
		rotations.append(int(''.join(r)))
	allprime = True
	for rotation in rotations:
		pos = bisect_left(primes, rotation, lo=0, hi=len(primes)-1)
		if primes[pos] != rotation:
			allprime = False
			break
	if allprime:
		count += 1

print count
