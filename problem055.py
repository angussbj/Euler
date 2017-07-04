lychcount = 0
for n in xrange(1, 10001):
	print n
	value = n
	strval = str(value)
	itercount = 0
	Lychrel = True
	while itercount < 50 and Lychrel:
		value += int(strval[::-1])
		strval = str(value)
		if strval == strval[::-1]:
			Lychrel = False
		itercount += 1
	if itercount >= 50:
		lychcount += 1
print lychcount