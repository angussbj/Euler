import math
for b in xrange (0, 500):
	for a in xrange (0, 500):
		c = math.sqrt(a**2+b**2)
		if a+b+c == 1000:
			print a*b*c
			print a
			print b
			print c