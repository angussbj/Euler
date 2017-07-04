# THIS IS BRUTE FORCED
import math

def ispent(k):
	# Check if pentagonal:
	value = (math.sqrt(1+24*k)+1)/6
	if value == int(value):
		return True
	else:
		return False

pents = []
Ds = []

for n in xrange(1, 10001):
	print n
	pents.append(n*(3*n-1)/2)
	for i in xrange(0, len(pents)-2):
		if ispent(pents[-1]-pents[i]) and ispent(pents[i]+pents[-1]):
			Ds.append(pents[-1]-pents[i])

print min(Ds)