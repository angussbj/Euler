import time

def countposs(number, maxcomponent):
	maxcomponent = min(number, maxcomponent)
	count = 0
	for component in xrange(maxcomponent, 0, -1):
		newnumber = number - component
		if newnumber <= 1:
			count += 1
		else:
			if newnumber <= maxcomponent:
				if prevs[newnumber] != 0:
					count += prevs[newnumber]
				else:
					countadd = countposs(newnumber, component)
					count += countadd
					prevs[number] = countadd
			else:
				count += countposs(newnumber, component)
	return count

t = time.time()
number = 50
prevs = [0] * (number + 1)
print countposs(number, number - 1)
print time.time() - t