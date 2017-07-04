posses = [[[1,0,0,0,0,0,0,0]]]
s = 0
i = 0
while len(posses[i]) != 0:
	posses.append([])
	for poss in posses[i]:
		for j in xrange(0, 7):		#j is the position within any tuple that encodes a possibility
			if poss[j] != 0:
				newposs = poss[:]
				newposs[j] -= 1
				if j == 2 or j == 5:
					newposs[j+1] += 2
					newposs[j+2] += 1
				else:
					newposs[j+1] += 2
				new = True
				for oldposs in posses[i+1]:
					if oldposs == newposs:
						new = False
				if new:
					posses[i+1].append(newposs)
	s += len(posses[i])
	print len(posses[i])
	# if len(posses[i]) < 15:
	# 	print posses[i]
	i += 1

# print "==============================="
print s

# s = 0
# for posslist in posses:
# 	s += len(posslist)
# print s