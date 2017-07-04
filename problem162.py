dec = 16**16 - 15**16 + 14**16 - 13**16
power = 0
while 16**power <= dec:
	power += 1
power -= 1
h = []
while power >= 0:
	multiple = 0
	while multiple * 16**power <= dec:
		multiple += 1
	multiple -= 1
	dec -= multiple * 16**power
	h.append(multiple)
	power -= 1
print h