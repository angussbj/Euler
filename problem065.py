convergent = 100
a = []
k = 1
for i in xrange(0, convergent - 1):
	if i % 3 == 2 or i % 3 == 0:
		a.append(1)
	else:
		a.append(2*k)
		k += 1
numerator = 1
denominator = a[-1]
del a[-1]
print a
for i in xrange(1, convergent - 1):
	numerator += a[-i] * denominator
	denominator, numerator = numerator, denominator
numerator += 2 * denominator

print numerator, "/", denominator

print sum(map(int, list(str(numerator))))