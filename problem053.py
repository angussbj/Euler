total = 0
for r in xrange(0, 101):
	c = 1
	n = r
	while n < 100 and c <= 1000000:
		n += 1
		c *= float(n)/(n-r)
	print n, "C", r, " = ", c
	total += 100 - n
	if c > 1000000:
		total += 1
print total