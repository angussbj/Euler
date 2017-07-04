import math
number = 1001
factors = []
divisor = 2
while number != 1:
	if number % divisor == 0:
		number /= divisor
		factors.append(divisor)
	else:
		divisor += 1

print factors