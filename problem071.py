from bisect import bisect_left
import math

primes = []
for n in xrange(2, 1000):
	prime = True
	s = math.sqrt(n)
	for p in primes:
		if p > s:
			break
		if n % p == 0:
			prime = False
			break
	if prime:
		primes.append(n)

properfractions = []
decimalvalues = []

for i in xrange(2, 1000001):
	if i % 1000 == 0:
		print i
	s = math.sqrt(i)
	j = int(math.floor(3*i/7))
	proper = True
	for p in primes:
		if p > s:
			break
		if i % p == 0 and j % p == 0:
			proper = False
			print i,"/",j
			print p
			break
	if proper:
		properfractions.append((j,i))
		decimalvalues.append(float(j)/i)

thelist = [x for (y,x) in sorted(zip(decimalvalues, properfractions))]
decimalvalues = sorted(decimalvalues)

index = -1 + bisect_left(decimalvalues, float(3)/7, lo = 0, hi = len(decimalvalues)-1)
print index
print len(thelist)
print len(decimalvalues)
print thelist[index]