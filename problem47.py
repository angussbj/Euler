#What does the question actually mean???
import math

def factorcount(n):
	count = 0
	for p in primes:
		if p > n:
			break
		if n % p == 0:
			count += 1
			while n % p == 0:
				n /= p
	return count


m = 100000
primes = [2]
bools = [True]*m
for i in xrange(1, int(math.ceil(m/3)) - 1):
	for j in xrange(1, i+1):
		c = i + j + 2*i*j
		if c >= m:
			break
		bools[c] = False
for i in xrange(1, m):
	if bools[i]:
		primes.append(2*i + 1)

done = False
n = 2
factorcounts = [0, 0]
while True:
	factorcounts.append(factorcount(n))
	if factorcounts[-1] == 4 and factorcounts[-2] == 4 and factorcounts[-3] == 4 and factorcounts[-4] == 4:
		print len(factorcounts) - 4
		break
	n += 1