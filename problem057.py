count = 0
for l in xrange(0, 1000):
	n = 1
	d = 2
	for iterations in xrange(0, l):
		n += 2*d
		n,d = d,n
	n += d
	if len(str(n)) > len(str(d)):
		count += 1
		print l," : ",n,"/",d
print count