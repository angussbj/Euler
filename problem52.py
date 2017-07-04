done = False
n = 0
while not done:
	n += 1
	done = True
	listn = map(int, list(str(n)))
	digcounts = []
	for digit in xrange(0, 10):
		digcounts.append(listn.count(digit))
	for f in xrange(2, 7):
		listm = map(int, list(str(f*n)))
		newdigcounts = []
		for digit in xrange(0, 10):
			newdigcounts.append(listm.count(digit))
		if digcounts != newdigcounts:
			done = False
			break
print n