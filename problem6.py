summ = 0
sumOfSquares = 0
for n in xrange (1, 101):
	summ += n
	sumOfSquares += n*n
difference = summ*summ - sumOfSquares
print summ
print sumOfSquares
print difference