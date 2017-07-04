products = []
for a in xrange(0,10):
	for b in xrange(1000,10000):
		c = a*b
		digits = map(int, list(str(a)))
		digits.extend(map(int, list(str(b))))
		digits.extend(map(int, list(str(c))))
		if len(digits) != 9:
			continue
		else:
			digits.sort()
			pandigital = True
			for i in xrange(0, 9):
				if digits[i] != i+1:
					pandigital = False
					break
			if pandigital:
				alreadygotit = False
				for product in products:
					if product == c:
						alreadygotit = True
						break
				if not(alreadygotit):
					products.append(c)
					print c
for a in xrange(10,100):
	for b in xrange(100,1000):
		c = a*b
		digits = map(int, list(str(a)))
		digits.extend(map(int, list(str(b))))
		digits.extend(map(int, list(str(c))))
		if len(digits) != 9:
			continue
		else:
			digits.sort()
			pandigital = True
			for i in xrange(0, 9):
				if digits[i] != i+1:
					pandigital = False
					break
			if pandigital:
				alreadygotit = False
				for product in products:
					if product == c:
						alreadygotit = True
						break
				if not(alreadygotit):
					products.append(c)
					print c
print sum(products)