low = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
ties = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
positions = ['', '', 'hundred', 'thousand']
summ =  ''
for n in xrange(1,1001)
	value = n
	andneeded = False
	while value > 0:
		if value < 20:
			if andneeded:
				summ += 'and'
			summ += low[value]
			value = 0
		elif value < 100:
			if andneeded:
				summ += 'and'
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
print len(summ)