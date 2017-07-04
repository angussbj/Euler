import math
import time
from bisect import bisect_left
from bisect import bisect_right

def isprime(n):
	for p in primes:
		if p > math.sqrt(n):
			return True
		if n % p == 0:
			return False
	return "ERROR"

def adjcount(prime, row):
	rowstart = (row-1)**2/2 + (row-1)/2 + 1
	rowend = (row)**2/2 + row/2
	adjcount = 0
	if prime == rowstart:
		if isprime(prime+row):
			adjcount += 1
		if isprime(prime+row+1):
			adjcount += 1
		if isprime(prime-row+1):
			adjcount += 1
		if isprime(prime-row+2):
			adjcount += 1
	elif prime == rowend-1:
		if isprime(prime+row):
			adjcount += 1
		if isprime(prime+row-1):
			adjcount += 1
		if isprime(prime+row+1):
			adjcount += 1
		if isprime(prime-row):
			adjcount += 1
		if isprime(prime-row+1):
			adjcount += 1
	elif prime == rowend:
		if isprime(prime+row):
			adjcount += 1
		if isprime(prime+row-1):
			adjcount += 1
		if isprime(prime+row+1):
			adjcount += 1
		if isprime(prime-row):
			adjcount += 1
	else:
		if isprime(prime+row):
			adjcount += 1
		if isprime(prime+row-1):
			adjcount += 1
		if isprime(prime+row+1):
			adjcount += 1
		if isprime(prime-row):
			adjcount += 1
		if isprime(prime-row+1):
			adjcount += 1
		if isprime(prime-row+2):
			adjcount += 1
	return adjcount

start = time.time()
rows = [5678027, 7208785]
r = max(rows)
m = int(math.sqrt(((r)**2 + r)/2))
print "m = ", m
primes = [2]
crosses = [1]* m
for i in xrange(1, int(math.ceil(m/3))):
	print i
	for j in xrange(1, i+1):
		c = i + j + 2*i*j
		if c >= m:
			break
		crosses[c] = 0
for i in xrange(1, m):
	if crosses[i]:
		primes.append(2*i+1)
print "Primes found. Time = ", time.time()-start
# print primes

Ss = []
for row in rows:
	rowprimes = []
	tripprimes = []
	rowstart = (row-1)**2/2 + (row-1)/2 + 1
	rowend = ((row)**2 + row)/2
	for n in xrange(rowstart, rowend+1):
		if isprime(n):
			rowprimes.append(n)
			print n, " / ", rowend
	print "rowprimes length = ", len(rowprimes)
	for prime in rowprimes:
		adjcountthing = adjcount(prime, row)
		if adjcountthing  >= 2:
			tripprimes.append(prime)
			continue
		elif adjcountthing == 1:
			if prime == rowstart:
				if isprime(prime+row) and adjcount(prime+row, row+1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime+row+1) and adjcount(prime+row+1, row+1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime-row+1) and adjcount(prime-row+1, row-1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime-row+2) and adjcount(prime-row+2, row-1) >= 2:
					tripprimes.append(prime)
					continue
			elif prime == rowend-1:
				if isprime(prime+row) and adjcount(prime+row, row+1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime+row+1) and adjcount(prime+row+1, row+1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime+row-1) and adjcount(prime+row-1, row+1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime-row+1) and adjcount(prime-row+1, row-1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime-row) and adjcount(prime-row, row-1) >= 2:
					tripprimes.append(prime)
					continue
			elif prime == rowend:
				if isprime(prime+row) and adjcount(prime+row, row+1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime+row+1) and adjcount(prime+row+1, row+1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime+row-1) and adjcount(prime+row-1, row+1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime-row) and adjcount(prime-row, row-1) >= 2:
					tripprimes.append(prime)
					continue
			else:
				if isprime(prime+row) and adjcount(prime+row, row+1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime+row+1) and adjcount(prime+row+1, row+1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime+row-1) and adjcount(prime+row-1, row+1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime-row+1) and adjcount(prime-row+1, row-1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime-row) and adjcount(prime-row, row-1) >= 2:
					tripprimes.append(prime)
					continue
				elif isprime(prime-row+2) and adjcount(prime-row+2, row-1) >= 2:
					tripprimes.append(prime)
					continue
	Ss.append(sum(tripprimes))
	print sum(tripprimes)
print sum(Ss)



