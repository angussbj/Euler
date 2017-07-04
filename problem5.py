allfactors = []

for numbers in xrange(1, 21):
	number = numbers
	factors = []
	divisor = 2
	while number != 1:
		if number % divisor == 0:
			number /= divisor
			factors.append(divisor)
		else:
			divisor += 1

	for factor in factors:
		fscount = 0
		for factor2 in factors:
			if factor == factor2:
				fscount += 1
		afscount = 0
		for factor2 in allfactors:
			if factor == factor2:
				afscount += 1
		for count in xrange(0, fscount-afscount):
			allfactors.append(factor)

product = 1
for factor in allfactors:
	product *= factor

print product