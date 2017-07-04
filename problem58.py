import math

def isprime(n):
	s = math.sqrt(n)
	for p in primes:
		if p > s:
			return True
		if n % p == 0:
			return False
	return True

print "doing primes"
m = 1000000
primes = [2]
slots = [True] * m
for i in xrange(1, m/3):
	for j in xrange(1, i+1):
		c = i + j + 2*i*j
		if c < m:
			slots[c] = False
		else:
			break
for k in xrange(1, m):
	if slots[k]:
		primes.append(2*k + 1)
print "primes done"

topright = [3, 13]
topleft = [5, 17]
bottomleft = [7, 21]
sidelength = 5
primecount = 5
ratio = 5.0/9
while ratio >= 0.1:
	topright.append(topright[-1] + (topright[-1]-topright[-2]+8))
	topleft.append(topleft[-1] + (topleft[-1]-topleft[-2]+8))
	bottomleft.append(bottomleft[-1] + (bottomleft[-1]-bottomleft[-2]+8))
	if isprime(topright[-1]):
		primecount += 1
	if isprime(topleft[-1]):
		primecount += 1
	if isprime(bottomleft[-1]):
		primecount += 1
	sidelength += 2
	ratio = float(primecount) / (2*sidelength - 1)
	print sidelength
print sidelength