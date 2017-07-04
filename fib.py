fibs = [1, 1]
while len(fibs) < 13:
	fibs.append( fibs[-1] + fibs[-2] )
print fibs