import math
import time

def firstindexnot(L, value):
	for i in xrange(len(L)):
		if L[i] != value:
			return i
	return len(L)

def findposs(remaining, highestpower, powercounts):
	count = 0
	highestpower = min(highestpower, int(math.floor(math.log(remaining, 2))))
	for power in xrange(highestpower, -1, -1):
		if powercounts[power] < 2:
			if remaining - 2**power > 0:
				powercounts[power] += 1
				unusedpowers = firstindexnot(powercounts, 0) - 1
				if unusedpowers < 0 or previousanswers[remaining][unusedpowers] == -1:
					childposs = findposs(remaining - 2**power, power, list(powercounts))
					previousanswers[remaining][unusedpowers] = childposs
				else:
					childposs = previousanswers[remaining][unusedpowers]
					print remaining, unusedpowers, childposs
				count += childposs
			elif remaining - 2**power == 0:
				powercounts[power] += 1
				count += 1
	return count


t = time.time()
number = 10
maxpower = int(math.floor(math.log(number, 2)))
powercounts = [0] * (maxpower + 1)
previousanswers = [[-1] * maxpower] * (number + 1)
print findposs(number, maxpower, powercounts)
print time.time() - t