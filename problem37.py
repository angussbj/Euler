# I don't think this would be so hard with pen and paper...
import math

def isprime(n):
	if n == 1:
		return False
	s = math.sqrt(n)
	prime = True
	for p in primes:
		if p > s:
			break
		if n % p == 0:
			prime = False
			break
	return prime


tprimes = []
primes = [2, 3, 5, 7]
n = 11
done = False
while not done:
	s = math.sqrt(n)
	prime = True
	for p in primes:
		if p > s:
			break
		if n % p == 0:
			prime = False
			break
	if prime:
		primes.append(n)
		nlist = list(str(n))
		truncs = []
		for i in xrange(1, len(nlist)):
			truncs.append(int(''.join(nlist[i:])))
		for i in xrange(1, len(nlist)):
			truncs.append(int(''.join(nlist[:i])))
		print "prime: ", n, ", truncs: ", truncs
		truncble = True
		for trunc in truncs:
			if not isprime(trunc):
				truncble = False
				break
		if truncble:
			tprimes.append(n)
			print "tp: ", n
			if len(tprimes) == 11:
				done = True
	n += 1
print tprimes
print sum(tprimes)
