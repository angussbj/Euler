import math

counts = []
for p in xrange(0, 1001):
	count = 0
	for a in xrange(1, int(math.floor(p/2))):
		b = float(p**2 - 2*a*p)/(2*(p-a))
		if b == int(b):
			count += 1
	counts.append(count)
m = max(counts)
for i in xrange(0,len(counts)):
	if counts[i] == m:
		print i