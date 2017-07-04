def rectanglecount(m,n):
	count = 0
	for i in xrange(m):
		for j in xrange(n):
			count += (m-i)*(n-j)
	return count

done = False
m = 1
while not done:
	for n in xrange(1, m+1):
		recs = rectanglecount(m,n)
		if recs > 1999990 and recs < 2000010:
			print m, n, recs
	m += 1