import math
import sys

primes = [2]

n = 3
while True:
	if n % 2 == 0:
		n += 1
		# print "even ", n
		continue
	prime = True
	for p in primes:
		if p > math.sqrt(n):
			break
		if n % p == 0:
			prime = False
			break
	if prime:
		primes.append(n)
		# print "prime ", n
	else:
		conjecture = False
		for p in primes:
			if (math.sqrt((n-p)/2) == int(math.sqrt((n-p)/2))):
				conjecture = True
				print n, " = ", p, " + 2 * ", math.sqrt((n-p)/2), "^2"
				break
		if not(conjecture):
			print "ANSWER = ", n
			sys.exit()
	n += 1