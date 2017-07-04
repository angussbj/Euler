import sys

lengths = [0, 1]

for n in xrange(2,1000000):
	count = 0;
	value = n
	while value >= n:
		if value % 2 == 0:
			value /= 2
		else:
			value = 3 * value + 1
		count += 1
	lengths.append(count + lengths[value])

m = max(lengths)
for n in xrange(0,1000000):
	if m == lengths[n]:
		print n