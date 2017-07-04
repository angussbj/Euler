low = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
ties = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
positions = [0, 0, 7, 8]
summ =  0
for n in xrange(1,1001):
	value = n
	andneeded = False
	while value > 0:
		if value < 20:
			if andneeded:
				summ += 3
			summ += low[value]
			value = 0
		elif value < 100:
			if andneeded:
				summ += 3
			diglist = list(str(value))
			summ += ties[int(diglist[0])]
			summ += low[int(diglist[1])]
			value = 0
		else:
			diglist = list(str(value))
			summ += low[int(diglist[0])]
			summ += positions[len(diglist)-1]
			value -= int(diglist[0]) * 10**(len(diglist)-1)
			andneeded = True

print summ