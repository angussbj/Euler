ns = []
for z in xrange(1,1000000):
	for diff in xrange(1, 1000000):
		ns.append((z + 2*diff)**2 - (z + diff)**2 - z**2)
		if ns[-1] >= 1000000:
			print z, diff
			break
solcounts = []
for n in xrange(0, 1000000):
	solcounts.append(ns.count(n))
print solcounts
print solcounts.count(10)
