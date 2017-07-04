import itertools
import numpy
coins = [1,2,5,10,20,50,100,200]
combinations = itertools.product(range(0,200), range(0,100), range(0, 40), range(0, 20), range(0, 10), range(0, 4), range(0, 2), range(0, 1))
ways = 8
for combination in combinations:
	if numpy.dot(coins, combination) == 200:
		ways += 1

print ways