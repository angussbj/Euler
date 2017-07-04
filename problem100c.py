import math

ns = []
bs = []

n = 2
s = math.sqrt(0.5)
while True:
	b = math.ceil(n*s)
	numerator = b*(b-1)
	denominator = n*(n-1)
	if denominator == 2*numerator:
		ns.append(n)
		bs.append(b)
		if len(ns) >= 2:
			print n, b, float(n)/bs[-2], float(n)/ns[-2], float(b)/ns[-2], float(b)/bs[-2]
	n += 1
	# if n % 100000 == 0:
	# 	print n, b, numerator, denominator, numerator/denominator