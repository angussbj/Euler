import math
import itertools

m = 1000000

# find primes up to m (not sure if this works for odd m)
m2 = int(math.ceil(m/2))
primes = [2]
bools = [True]*(m2)
for i in xrange(1, int(math.ceil(m2/3)) - 1):
	for j in xrange(1, i+1):
		c = i + j + 2*i*j
		if c >= m2:
			break
		bools[c] = False
for i in xrange(1, m2):
	if bools[i]:
		primes.append(2*i + 1)
print "Primes done."

factorslist = [[], []]
for n in xrange(2, m+1):
	s = math.sqrt(n)
	for p in primes:
		if p > s:
			factorslist.append([n])
			break
		elif n % p == 0:
			q = n / p # this is the number we look at to find the other factors of n
			if factorslist[q][0] == p:
				factorslist.append(factorslist[q])
			else:
				factorslist.append([p])
				factorslist[-1].extend(factorslist[q])
			break
print "Factors list done"

total = 0
counts = []
for n in xrange(1, m):
	fprod = 1
	phprod = 1
	for f in factorslist[n]:
		fprod *= f
		phprod *= f-1
	total += phprod * math.floor((m-n)/fprod)
	k = m % fprod
	f = k
	for i in xrange(1, len(factorslist[n]) + 1):
		s = 0
		for fsubset in list(itertools.combinations(factorslist[n], r = i)):
			prod = 1
			for factor in list(fsubset):
				prod *= factor
			s += math.floor(k/prod)
		f += ((-1)**i) * s
	total += f
print total


















