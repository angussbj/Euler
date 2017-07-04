abundants = []
for n in xrange(1, 28123):
	s = 0
	for d in xrange(1, n/2+1):
		if n % d == 0:
			s += d
	if s > n:
		abundants.append(n)

print "A"
total = 0
for n in xrange(1, 28123):
	sumfound = False
	for abundant1 in abundants:
		if abundant1 > n-12:
			break
		if sumfound:
			break
		for abundant2 in abundants:
			if abundant2 > n-12:
				break
			if abundant1 + abundant2 == n:
				sumfound = True
	if not(sumfound):
		total += n

print total
