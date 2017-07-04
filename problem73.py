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

count = 0

for i in xrange(4, 12001):
	s = math.sqrt(i)
	# print "i = ", i
	for j in xrange(int(math.ceil(float(i)/3)), int(math.ceil(float(i)/2))):
		proper = True
		for p in primes:
			if p > s:
				break
			if i % p == 0 and j % p == 0:
				proper = False
				break
		if proper:
			count += 1
			print j,"/",i

print count