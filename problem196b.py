import math
import	time
from bisect import bisect_left

def euler196(row, primes):
	areastart, areaend = (m-2)*(m-1)/2, (m+2)*(m+3)/2
	aprimes = [True] * (areaend - areastart + 1)
	for p in primes:
		n = bisect_left(primes, int(math.ceil(areastart/p)), lo = 0, hi = len(primes)-1)
		while primes[n] * p <= areaend:
			aprimes[primes[n] * p - areastart] = False
			n += 1
	print aprimes
	return 1



rows = [8, 9]

start = time.time()
r = max(rows)+2
m = int(math.sqrt(((r)**2 + r)/2))
primes = [2]
crosses = [True]* m
for i in xrange(1, int(math.ceil(m/3))):
	for j in xrange(1, i+1):
		c = i + j + 2*i*j
		if c >= m:
			break
		crosses[c] = False
for i in xrange(1, m):
	if crosses[i]:
		primes.append(2*i+1)
print time.time() - start

print euler196(rows[0], primes) + euler196(rows[1], primes)