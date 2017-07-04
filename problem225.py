import math

def factorise(n):
	return True

primes = [2]
n = 3

tribs = [1,1,1]
factors = [[],[],[]]

done = False
while not done:
	tribs.append(tribs[-1] + tribs[-2] + tribs[-3])
	while n < tribs[-1]:
		s = math.sqrt(n)
		for p in primes:
			if p > s:
				primes.append(n)
				break
			if n % p == 0:
				break
		n += 1
	number = tribs[-1]
	factors.append([])
	for p in primes:
		if number == 1:
			break
		if p > math.sqrt(number):
			factors[-1].append(number)
			break
		while number % p == 0:
			factors[-1].append(p)
			number /= p
	if tribs[-1] > 1000000:
		done = True

z = zip(tribs, factors)

for point in z:
	print point