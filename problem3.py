number = 600851475143
divisor = 2
while number/divisor != 1:
	if number % divisor == 0:
		number /= divisor
	divisor += 1

print number