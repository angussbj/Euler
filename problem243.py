import math
from operator import mul

def resilience(d):
	count = [1]*(d-1)
	factors = []
	s = math.sqrt(d)
	for p in primes:
		if p > s:
			break
		if d % p == 0:
			factors.append(p)
	print factors
	for factor in factors:
		for n in xrange(1, d/factor):
			count[factor*n] = 0
	return float(sum(count))/(d-1)


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
print "done with primes"


d = 2
i = 1
while True:
	r = resilience(d)
	if r < float(15499)/94744:
		print "ANSWER: ", d
		break
	print "R(", d, ") = ", r
	d *= primes[i]
	i += 1
