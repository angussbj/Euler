import math

ub = 1000000

def isprime(n):
	s = math.sqrt(n)
	for p in primes:
		if p > s:
			return True
		if n % p == 0:
			return False
	return True

m = int(math.sqrt(ub)/2)
primes = [2]
a = [True] * m
for i in xrange(1, m/3):
	for j in xrange(1, i+1):
		c = i + j + 2*i*j
		if c < m:
			a[c] = False
		else:
			break
for i in xrange(1, m):
	if a[i]:
		primes.append(2*i+1)

cubes = [1, 8]
n = 3
while cubes[-1] - cubes[-2] < ub:
	cubes.append(n**3)
	n += 1
l = len(cubes) - 1 # minus one to ignore last cube

count = 0
for i in xrange(0, l):
	for j in xrange(i+1, l):
		d = cubes[j] - cubes[i]
		if d >= ub:
			break
		if isprime(d):
			count += 1
print count