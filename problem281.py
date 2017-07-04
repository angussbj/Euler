import math

def f(m,n):
	return float(math.factorial(m*n - 1))/(math.factorial(n)**3)
	# nope - rotations are a bitch.

	
print f(2,1), f(2,2), f(3,1), f(3,2)