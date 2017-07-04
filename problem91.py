ma = 50
count = 0
for x1 in xrange(0, ma + 1):
	for y1 in xrange(0, ma + 1):
		if y1 == 0:
			if x1 == 0:
				continue
			else:
				count += ma
				# print (x1,y1)
		else:
			m = -float(x1)/y1
			b = y1 - m * x1
			for x in xrange(0, ma + 1):
				if x != x1:
					y = m * x + b
					if y <= ma and y == int(y):
						count += 1
						# print [(x1,y1), (x,y)]
count += ma**2
print count