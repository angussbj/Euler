def d(n):
	s = 0
	for i in xrange(1, n / 2 + 1):
		if n % i == 0:
			s += i
	return s

summ = 0
for n in xrange(1, 10000):
	if d(n) != n and d(d(n)) == n:
		summ += n

print summ
