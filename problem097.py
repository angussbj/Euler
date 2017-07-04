# print 28433*2**7830457+1

number = 1
for iterations in xrange(0, 7830457):
	number *= 2
	s = str(number)
	if len(s) > 10:
		number = int(s[(len(s)-10):])
		if iterations % 100 == 0:
			print iterations

p = str(28433*number + 1)
print int(p[(len(p)-10):])
