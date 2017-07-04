from bisect import bisect_left

m = 500000
array = [True] * m
primes = [2]
for i in xrange(1, m/3):
	for j in xrange(1, i+1):
		c = i + j + 2*i*j
		if c < m:
			array[c] = False
		else:
			break
for i in xrange(1, len(array)):
	if array[i]:
		primes.append(2*i+1)

print len(primes), "primes found"

longestlength = 0
theprime = 0
l = len(primes)
for i in xrange(0, l):
	s = 0
	j = i
	while s < 1000000 and j < l:
		s += primes[j]
		j += 1
		if j - i > longestlength: #if this will be a long enough sum for us to care about
			if primes[bisect_left(primes, s, lo = 0, hi = l-1)] == s: #if s is in our list of primes
				theprime = s
				longestlength = j - i

print longestlength
print theprime