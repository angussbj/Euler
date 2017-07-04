from math import *

x = 1.4
y = -9.6
ml = -19.7/1.4
thetal = atan(ml)
b = 10.1
escaped = False
bounces = 0
print "y = ", ml, "x + ", b
while not escaped:
	bounces += 1
	thetat = atan(-4*x/y)
	thetal = pi - thetal + 2*thetat
	ml = tan(thetal)
	b = y - ml * x
	print "y = ", ml, "x + ", b
	c1 = -b*ml
	c2 = 2*sqrt(25*ml**2+100-b**2)
	c3 = 4 + ml**2
	print x, (c1+c2)/c3, (c1-c2)/c3
	if abs(x - (c1+c2)/c3) <= 0.001:
		x = (c1-c2)/c3
	elif abs(x - (c1-c2)/c3) <= 0.001:
		x = (c1+c2)/c3
	else:
		print "PROBLEM!!!!!"
		break
	y = ml*x + b
	if y > 0 and abs(x) <= 0.01:
		escaped = True
print bounces