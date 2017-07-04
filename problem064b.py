import math
count = 0
for n in xrange(1, 10001):
	if n % 100 == 0:
		print n
	x = math.sqrt(n)
	if x == int(x):
		continue
	floor = math.floor(x)
	a = -floor
	b = 1
	period = 0
	while (a != -floor or b != 1) or period == 0:
		b = (n-a**2)/b
		a = -a
		while (x+a)/b >= 1:
			a -= b
		period += 1
	if period % 2 == 1:
		count += 1
print count
