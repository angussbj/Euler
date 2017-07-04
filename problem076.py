import time

def countposs(number, maxcomponent):
	maxcomponent = min(number, maxcomponent)
	count = 0
	for component in xrange(maxcomponent, 0, -1):
		newnum = number-component
		if newnum <= 1:
			count += 1
		else:
			count += countposs(newnum, component)
	return count

t = time.time()
number = 100
print countposs(number, number - 1)
print time.time() - t