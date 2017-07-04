import math

def f(n):
	count = 0
	centre = n/2
	radiussquared = (n**2)/2
	for x in xrange(int(math.ceil(centre-math.sqrt(radiussquared))), int(math.ceil(centre+math.sqrt(radiussquared)))):
		delta = math.sqrt(radiussquared - (x - centre)**2)
		y = centre + delta
		if y == int(y):
			if delta == 0:
				count += 1
			else:
				count += 2
	return count

ncount = 0
for n in xrange(0, 100000000001):
	if n % 1000000 == 0:
		print n
	if f(n) == 420:
		count += 1
print ncount