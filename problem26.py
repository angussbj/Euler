lengths = [0, 0]

for n in xrange(2, 1000):
	carries = []
	numerator = 1
	keeplooping = True
	carryposition = 0
	while keeplooping:
		carries.append(numerator)
		if numerator < n:
			numerator *= 10
		numerator = numerator % n
		carryposition = 0
		for carry in carries:
			carryposition += 1
			if numerator == carry:
				keeplooping = False
				break
	lengths.append(len(carries)-carryposition+1)

m = max(lengths)
for n in xrange(0, 1000):
	if lengths[n] == m:
		print n

print m