import math

numbers = []
for x in xrange(0, 1001*1001):
	numbers.append(0)

point = 500*1001 + 500
direction = 0
dcountceiling = 1
dcount = 0
for x in xrange(1, 1001*1001+1):
	print point
	numbers[point] = x
	if direction == 0:
		point += 1
	elif direction == 1:
		point += 1001
	elif direction == 2:
		point -= 1
	else:
		point -= 1001
	dcount += 1
	if dcount == math.floor(dcountceiling):
		dcountceiling += 0.5
		direction = (direction + 1) % 4
		dcount = 0

s = 0
pointa = 0
pointb = 1000
for i in xrange(0,1001):
	s += numbers[pointa]+numbers[pointb]
	pointa += 1002
	pointb += 1000

print s-1