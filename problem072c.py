# relies on the conjecture that phi(ab) = phi(a)phi(b)

import math

maxd = 1000000

m = maxd
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


factorslist = [[], []]
for n in xrange(2, maxd+1):
	if n % 1000 == 0:
		print n
	factors = []
	for i in xrange(0, len(primes)):
		if n % primes[i] == 0:
			if n == primes[i]:
				factors = [0] * i
				factors.append(1)
				factorslist.append(factors)
				break
			factors = factorslist[n/primes[i]]
			factors[i] += 1
			factorslist.append(factors)
			break

print "Factors found."

total = 0

for j in xrange(2, len(factorslist)):
	if j % 1000 == 0:
		print j
	contribution = 1
	for i in xrange(0, len(factorslist[j])):
		if factorslist[j][i] > 0:
			contribution *= (primes[i] - 1) * (primes[i]**(factorslist[j][i]-1))
	total += contribution

print total