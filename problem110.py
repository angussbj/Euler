import math

def isprime(n): # relies on list of primes up to at least the square root of n
	prime = True
	s = math.sqrt(n)
	for p in primes:
		if p > n:
			return True
		if p % n == 0:
			return False
	return True

def sols(n):
	count = 0
	for x in xrange(n + 1, 2*n + 1):
		y = float(n*x)/(x - n)
		if y == int(y):
			count += 1
	return count

primes = [2]
m = 1000000
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

m = 0
n = 0
while True:
	n += 1
	number = n
	factors = []
	for p in primes:
		if number == 1:
			break
		if p > math.sqrt(number):
			factors.append(number)
			break
		while number % p == 0:
			factors.append(p)
			number /= p
	s = sols(n)
	if len(factors) >= 4:
		print n, s, factors
	# if s > m:
	# 	print n, s
	# 	m = s
	if s > 1000:
		print n
		break 