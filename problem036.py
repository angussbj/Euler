bipals = []
for n in xrange(0, 1000000):
	decdiglist = map(int, list(str(n)))
	good = True
	for i in xrange(0, len(decdiglist)):
		if decdiglist[i] != decdiglist[-i-1]:
			good = False
			break
	if not good:
		continue
	bindiglist = list(bin(n))
	del bindiglist[0]
	del bindiglist[0]
	bindiglist = map(int, bindiglist)
	for i in xrange(0, len(bindiglist)):
		if bindiglist[i] != bindiglist[-i-1]:
			good = False
			break
	if good:
		bipals.append(n)
		print n
print sum(bipals)