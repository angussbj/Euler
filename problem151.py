from random import randint

def mean(A):
	return sum(A)/float(len(A))

counts = []
while True:
	count = 0
	sheets = [1,1,1,1] #each entry gives the number of sheets of each size (A2,A3,A4,A5)
	for batch in xrange(0, 14):
		if sum(sheets) == 1:
			count += 1
		sheet = randint(1, sum(sheets))
		s = 0
		size = 0
		while s < sheet:
			s += sheets[size]
			size += 1
		sheets[size-1] -= 1
		place = size
		while place <= 3:
			sheets[place] += 1
			place += 1
		#arealeft = 8*sheets[0] + 4*sheets[1] + 2*sheets[2] + sheets[3]
		#print (sheet, sheets, size==4)
	counts.append(count)
	print (mean(counts))