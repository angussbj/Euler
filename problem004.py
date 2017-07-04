pals = []
for i in xrange(900, 999):
	for j in xrange(900, 999):
		p = i*j
		pstr = str(p)
		plst = []
		plst.extend(pstr)
		pallindrome = True
		for count in xrange(1, len(plst)):
			if plst[count] != plst[-count-1]:
				pallindrome = False
				break
		if pallindrome == True:
			pals.append(p)

print pals
print max(pals)
