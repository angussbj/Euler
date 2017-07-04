def sols(n):
	count = 0
	for x in xrange(n + 1, 2*n + 1):
		y = float(n*x)/(x - n)
		if y == int(y):
			count += 1
	return count

print sols(4), sols(1260)

m = 0
n = 0
while True:
	n += 2310
	s = sols(n)
	if s > m:
		print n, s
		m = s
	if s > 1000:
		print n
		break 