import math
primes = []
for n in xrange(2,2000000):
	prime = True
	for p in primes:
		if p > math.sqrt(n):
			break
		if n%p == 0:
			prime = False
			break
	if prime:
		primes.append(n)
print sum(primes)
