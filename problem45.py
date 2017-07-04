import math

def ispent(k):
	# Check if pentagonal:
	value = (math.sqrt(1+24*k)+1)/6
	if value == int(value):
		return True
	else:
		return False

def ishex(k):
	# Check if hexagonal:
	value = (math.sqrt(1+8*k)+1)/4
	if value == int(value):
		return True
	else:
		return False

n = 1
t = 0
while True:
	t += n
	if ispent(t) and ishex(t):
		if t == 40755 or t == 1:
		else:
			print t
			break
	n += 1