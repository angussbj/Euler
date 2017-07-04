from __future__ import print_function
import math
import sys

def isprime(n): # relies on list of primes up to at least the square root of n
	prime = True
	s = math.sqrt(n)
	for p in primes:
		if p > n:
			return True
		if p % n == 0:
			return False
	return True

q = 0 # so that people can type q to quit as well
exit = 0 # that too

while True:
	number = input('Please enter a positive integer to factorise (enter 0 to exit): ')
	if number == 0:
		sys.exit()

	primes = [2]
	m = int(math.floor(math.sqrt(number)/2))
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

	if isprime(number):
		primes.append(number)

	factors = []
	for p in primes:
		if p > math.sqrt(number):
			if number == 1:
				break
			factors.append(number)
			break
		while number % p == 0:
			factors.append(p)
			number /= p

	
	i = 0
	while i < len(factors):
		count = factors.count(factors[i])
		print (factors[i], end = '')
		if count > 1:
			print ('^', count, end = '', sep='')
		i += count
		if i < len(factors):
			print (' * ', end = '')
	print ()