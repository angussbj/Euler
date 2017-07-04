import math

primes = [2]
m = 14062
array = [True] * m
for i in xrange(1, int(math.floor(m/3.0))):
	for j in xrange(1, i+1):
		c = i + j + 2*i*j
		if c < m:
			array[c] = False
		else:
			break
for i in xrange(1, len(array)):
	if array[i]:
		primes.append(2*i + 1)

print "primes done"

abundants = []
for n in xrange (12, 28122):
	if n % 1000 == 0:
		print n
	divisors = [1]
	for d in xrange(2, n/2 + 1):
		if n % d == 0:
			divisors.append(d)
	if sum(divisors) > n:
		abundants.append(n)

print len(abundants), " abundants found"

l = [True] * 28124
for i in xrange(0, len(abundants)):
	for j in xrange(0, i+1):
		c = abundants[i] + abundants[j]
		if c <= 28123:
			l[c] = False
		else:
			break

print "sums found"

s = 0
for i in xrange(0, 28123):
	if l[i]:
		s += i
print s