import math
from operator import mul

m = 10000
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

i = 0
factors = []
while True:
	factors.append(primes[i])
	n = reduce(mul, factors)
	numbers = range(1, n)
	for factor in factors:
		j = 0
		while j < len(numbers):
			if numbers[j] % factor == 0:
				del numbers[j]
			j += 1
	r = float(len(numbers))/(n-1)
	print "R(", n, ") = ", r
	if r < float(15499)/94744:
		print "ANSWER: ", n
		break
	i += 1
