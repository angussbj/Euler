import math
import time

def findposs(remaining, highestpower, powercounts):
	count = 0
	highestpower = min(highestpower, int(math.floor(math.log(remaining, 2))))
	for power in xrange(highestpower, -1, -1):
		if powercounts[power] < 2:
			if remaining - 2**power > 0:
				powercounts[power] += 1
				count += findposs(remaining - 2**power, power, list(powercounts))
			elif remaining - 2**power == 0:
				powercounts[power] += 1
				count += 1
	return count


t = time.time()
number = 10000
maxpower = int(math.floor(math.log(number, 2)))
powercounts = [0] * (maxpower + 1)
print findposs(number, maxpower, powercounts)
print time.time() - t