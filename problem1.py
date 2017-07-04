summ = 0
for number in xrange(1, 1000):
	if number % 3 == 0 or number % 5 == 0 :
		summ = summ + number

print(summ)