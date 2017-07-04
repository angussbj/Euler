import itertools

# values = (200, 100, 50, 20, 10, 5, 2, 1) # note possibility entry denotes number of coins of the type with value equal to the number of pence in the value tuple entry with corresponding index

possibilities = [[1,0,0,0,0,0,0,0]]

level_lengths = [1]

i = 0							#i is the position in the list of possibilities (which will grow)
while i < len(possibilities):
	for j in xrange(0, 7):		#j is the position within any tuple that encodes a possibility
		if possibilities[i][j] != 0:
			newposs = possibilities[i][:]
			newposs[j] -= 1
			if j == 2 or j == 5:
				newposs[j+1] += 2
				newposs[j+2] += 1
			else:
				newposs[j+1] += 2
			new = True
			for k in xrange(sum(level_lengths), len(possibilities)):
				if possibilities[k] == newposs:
					new = False
					break
			if new:
				possibilities.append(newposs)
	i += 1
	if i = sum(level_lengths):
		level_lengths.append(len(possibilities) - sum(level_lengths))
	print i, "/", len(possibilities)

print len(possibilities)