import itertools

results = []
primes = [2, 3, 5, 7, 11, 13, 17]
digits = map(str, range(0,10))
perms = list(itertools.permutations(digits))
length = len(perms)
j = 0
for perm in perms:
	# if j % 10000 == 0:
	# 	print j, " / ", length
	holds = True
	for i in xrange(0, 7):
		if int(''.join(perm[(7-i):(10-i)])) % primes[6-i] != 0:
			holds = False
	if holds:
		results.append(int(''.join(perm)))
	j += 1
print results
print sum(results)
