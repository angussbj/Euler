from decimal import *


b = Decimal(1000000000000)
found = False
while not found:
	b += 1
	a = 1+2*(b*b - b)
	a = (1+a.sqrt())/2
	fracPart = a - a.to_integral()
	if fracPart == 0:
		print a
		found = True
