numbers = []
for k in xrange(1, 10000):
	i = 1
	digits = []
	while len(digits) < 9:
		digits.extend(map(int, list(str(i*k))))
		i += 1
	if len(digits) != 9:
		continue
	else:
		c = int(''.join(map(str, digits)))
		digits.sort()
		pandigital = True
		for i in xrange(0, 9):
			if digits[i] != i+1:
				pandigital = False
				break
		if pandigital:
			numbers.append(c)
			print c
print max(numbers)