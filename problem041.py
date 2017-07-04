import math
import itertools

def isprime(n, primes):
	for p in primes:
		if p > math.sqrt(n):
			return True
		if n % p == 0:
			return False
	return True

n = 7

m = int(10**(n/2.0))/2
print "m = ", m
primes = [2]
bools = [True]*m
for i in xrange(1, int(math.ceil(m/3)) - 1):
	for j in xrange(1, i+1):
		c = i + j + 2*i*j
		if c >= m:
			break
		bools[c] = False
for i in xrange(1, m):
	if bools[i]:
		primes.append(2*i + 1)

panprimes = []

digits = range(1, n+1)
perms = itertools.permutations(digits)
for perm in perms:
	intperm = int(''.join(map(str, list(perm))))
	if isprime(intperm, primes):
		panprimes.append(intperm)

print panprimes
print max(panprimes)