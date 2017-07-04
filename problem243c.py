import math

threshold = 15499.0/94744
minres = 1
primes = [2]
factors = [[], [], [2]]
n = 3
done = False
while not done:
	if n % 100000 == 0:
		print n
	s = math.sqrt(n)
	for p in primes:
		if p > math.sqrt(n):
			primes.append(n)
			factors.append([n])
			break
		if n % p == 0:
			factors.append([p])
			factors[-1].extend(factors[n/p])
			break
	phi = 1
	for i in xrange(0, len(factors[-1])):
		if i == 0:
			phi *= factors[-1][i] - 1
		elif factors[-1][i] != factors[-1][i-1]:
			phi *= factors[-1][i] - 1
		else:
			phi *= factors[-1][i]
	resilience = (phi)/float(n-1)
	# print "resilience(", n, ") = ", resilience
	if resilience < minres:
		print n
		minres = resilience
		print minres
		if resilience < threshold:
			print n
			done = True
			break
	n += 1