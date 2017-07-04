import sys
import math

m = 1000000
primes = [2]
crosses = [1]* m
for i in xrange(1, int(math.ceil(m/3))):
	for j in xrange(1, i+1):
		c = i + j + 2*i*j
		if c >= m:
			break
		crosses[c] = 0
for i in xrange(1, m):
	if crosses[i]:
		primes.append(2*i+1)

t = 0
n = 1
while True:
	t += n
	print n, ", ", t
	pfact = []
	t2 = t
	for p in primes:
		if p > t2:
			break
		pfact.append(1)
		while t2 % p == 0:
			pfact[-1] += 1
			t2 /= p
	dcount = 1
	for fact in pfact:
		dcount *= fact
	print dcount
	if dcount > 500:
		print t
		sys.exit()
	n += 1