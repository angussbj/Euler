import math
primes = []
n = 2
while len(primes) < 10001:
	prime = True
	for p in primes:
		if p > math.sqrt(n):
			break
		if n % p == 0:
			prime = False
	if prime:
		primes.append(n)
	n += 1

print primes[-1]