m = 0
for a in xrange(1, 100):
	for b in xrange(1, 100):
		s = sum(map(int, list(str(a**b))))
		if s > m:
			m = s
print m