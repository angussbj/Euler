import math

def factors(n):
	factors = []
	for p in primes:
		factors.append(0)
		if p > n:
			break
		if n % p == 0:
			factors[-1] = 1
			while n % p == 0:
				n /= p
	return factors

maxd = 1000001

m = 1000000
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

print "Primes done."

factorslist = [0, 0]
for n in xrange(2, maxd):
	if n % 1000 == 0:
		print n
	i = 0
	while True:
		if n % primes[i] == 0:
			# print n, " is divisible by ", primes[i]
			factorslist.append( (factorslist[n/primes[i]]) | (2**i) )
			break
		i += 1

print "Factors done."

count = 0
for denominator in xrange(2, maxd):
	if denominator % 1000 == 0:
		print denominator
	for numerator in xrange(1, denominator):
		if factorslist[numerator] & factorslist[denominator] == 0:
			count += 1
print count