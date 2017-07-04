import itertools

numbers = []
resiliences = []
primes = [2,3,5,7,11,13,17,19,23,29]
for lowpow in itertools.product([1,2,3,4], repeat = 5):
	for highpow in itertools.product([0,1,2], repeat = len(primes)-5):
		powers = list(lowpow)
		powers.extend(list(highpow))
		number = 1
		factors = []
		for i in xrange(0,len(primes)):
			number *= primes[i]**powers[i]
			factors.extend([primes[i]] * powers[i])
		phi = 1
		for i in xrange(0, len(factors)):
			if i == 0:
				phi *= factors[i] - 1
			elif factors[i] != factors[i-1]:
				phi *= factors[i] - 1
			else:
				phi *= factors[i]
		resilience = (phi)/float(number-1)
		numbers.append(number)
		resiliences.append(resilience)

output = sorted(zip(numbers,resiliences))
minres = 1
print output[1]
for point in output:
	if point[1] < minres:
		minres = point[1]
		print point