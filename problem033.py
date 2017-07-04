import math
numerators = []
denominators = []

for denominator in xrange(11, 100):
	dlist = map(int, list(str(denominator)))
	if dlist[0] == 0 or dlist[1] == 0:
		continue
	for numerator in xrange(11, denominator):
		nlist = map(int, list(str(numerator)))
		if nlist[0] == 0 or nlist[1] == 0:
			continue
		for i in xrange(0,2):
			for j in xrange(0,2):
				if nlist[i] == dlist[j] and i!=j:
					if float(nlist[(i+1)%2])/dlist[(j+1)%2] == float(numerator)/denominator:
						numerators.append(numerator)
						denominators.append(denominator)
						print numerator, "/", denominator

prodn = 1
for numerator in numerators:
	prodn *= numerator
prodd = 1
for denominator in denominators:
	prodd *= denominator

primes = [2]
array = [True] * 500
for i in xrange(1, 500/3):
	for j in xrange(1, i + 1):
		c = i + j + 2*i*j
		if c >= 500:
			break
		array[c] = False
for n in xrange(1, 500):
	if array[n]:
		primes.append(2*n+1)

for p in primes:
	if p > prodn or p > prodd:
		break
	while prodd % p == 0 and prodn % p == 0:
		prodd /= p
		prodn /= p

print prodn
print prodd