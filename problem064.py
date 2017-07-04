import math
lengths = []
count = 0
for n in xrange(1, 41):
	if n % 100 == 0:
		print n
	x = math.sqrt(n)
	if x == int(x):
		continue
	x = x - math.floor(x)
	sequence = []
	xs = [x]
	complete = False
	while not complete:
		c = 1/x
		sequence.append(math.floor(c))
		x = c - math.floor(c)
		xs.append(x)
		if abs(x - xs[0]) < 0.000001:
			complete = True
	if len(sequence) % 2 == 1:
		count += 1
	lengths.append(len(sequence))
	print xs
print count
print lengths