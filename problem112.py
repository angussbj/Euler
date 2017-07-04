bcount = 0
n = 1
proportion = 0
while proportion < 0.99:
	n += 1
	increasing = True
	decreasing = True
	digits = map(int, list(str(n)))
	for i in xrange(1, len(digits)):
		if digits[i] < digits[i-1]:
			increasing = False
		if digits[i] > digits[i-1]:
			decreasing = False
	if not (increasing or decreasing):
		bcount += 1
	proportion = float(bcount)/n
print n