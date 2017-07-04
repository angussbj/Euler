import sys
import math

maxd = 1000000

m = maxd
primes = [2]
bools = [True]*m
for i in xrange(1, int(math.ceil(m/3)) - 1):
	for j in xrange(1, i+1):
		c = i + j + 2*i*j
		if c >= m:
			break
		bools[c] = False
for i in xrange(1, m):
	if bools[i]:
		primes.append(2*i + 1)

print "Primes done."

# total to add to at each step
total = 0

#all the denominators so that the ones that are left after the special cases can be dealt with
denominators = [False] * (maxd+1)

primesand1 = [1]
primesand1.extend(primes)

for p in primes:
	for q in primesand1:
		d = q*p
		if (q >= p and q != 1) or d > maxd:
			break
		for r in primesand1:
			d *= r
			if (r >= q and r != 1) or d > maxd:
				break
			for s in primesand1:
				d *= s
				if (s >= r and s != 1) or d > maxd:
					break
				for t in primesand1:
					d *= t
					if (t >= s and t != 1) or d > maxd:
						break
					for u in primesand1:
						d *= u
						if (u >= t and u != 1) or d > maxd:
							break
						for v in primesand1:
							d *= v
							if (v >= u and v!= 1) or d > maxd:
								break
							contribution = 1
							letters = [p,q,r,s,t,u,v]
							for letter in letters:
								if letter != 1:
									contribution *= letter - 1
							total += contribution
							denominators[d] = True
							for i in xrange(1, 7):
								if letters[-i] == 1:
									continue
								power = 1
								while letters[-i]**power < letters[-i-1]:
									d *= letters[-i]
									if d > maxd:
										break
									power += 1
									contribution *= letters[i]
									total += contribution
									denominators[d] = True


print "Long stuff done"

for p in primes:
	if p > math.sqrt(maxd):
		break
	power = 2
	while p**power <= maxd:
		if denominators[p**power]:
			print "ALREADY DONE!"
		total += (p-1) * (p**(power - 1))
		denominators[p**power] = True
		power += 1

print total
print "Still to do: ", denominators.count(False) - 2
for i in xrange(2, maxd+1):
	if not denominators[i]:
		print i



