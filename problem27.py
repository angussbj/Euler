import math

primes = []
for n in xrange(2, 1000):
	prime = True
	for p in primes:
		if p > math.sqrt(n):
			break
		if n % p == 0:
			prime = False
	if prime:
		primes.append(n)

lengthss = []
for a in xrange(-999, 1000):
	lengths = []
	for b in primes:
		n = 0
		out = b
		while primes.count(out) != 0:
			out = n**2 + a*n + b
			n += 1
		lengths.append(n)
	lengthss.append(lengths)

maxs = []
for i in xrange(0, len(lengthss)):
	maxs.append(max(lengthss[i]))
m = max(maxs)
for i in xrange(0, len(lengthss)):
	for j in xrange(0, len(primes)):
		if lengthss[i][j] == m:
			print (i-999) * primes[j], m 