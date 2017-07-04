import math
from decimal import *
getcontext().prec = 20
T = Decimal(1000000000000)
while True:
	B = (1+(1+2*T*(T-1)).sqrt())/2
	if B.compare(B.quantize(Decimal(1))) == 0:
		print B
		print T
		break
	T += 1
	if T % 100000 == 0:
		print T