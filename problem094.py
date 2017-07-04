import time
import math

#area of triangle with sides a, a, b
def area(a, b):
	return b * math.sqrt(a**2 - b**2 / 4) / 2

t = time.time()
s = 0
for a in xrange(1000000/3):
	b = a + 1
	A = area(a, b)
	if A - math.floor(A) == 0:
		s += 2 * a + b
	b = a - 1
	A = area(a, b)
	if A - math.floor(A) == 0:
		s += 2 * a + b

print time.time() - t
print s