import numpy as np

def next(n):
	total = 1
	for i in range(2, int(np.floor(np.sqrt(n)))+1):
		if n % i == 0:
			total += i + n/i
			if i**2 == n:
				total -= i
	return total

cap = 1000000

lengths = [-1] * cap
for i in range(cap):
	if i % 10000 == 0:
		print i
	if lengths[i] == -1:
		chain = [i]
		while True:
			chain.append(next(chain[-1]))
			if chain[-1] in chain[:-1]:
				p = chain.index(chain[-1])
				length = len(chain) - p - 1
				for number in chain[:p]:
					lengths[number] = 0
				for number in chain[p:-1]:
					lengths[number] = length
				break
			if chain[-1] > cap or lengths[chain[-1]] != -1:
				for number in chain[:-1]:
					lengths[number] = 0
				break

m = max(lengths)
print lengths.index(m), m