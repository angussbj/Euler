total = 0

#numbers ending in 0:
total += 10

#numbers ending in 1:
n = 1
while n < 981:
	total += n
	n += 10
total += 991

#numbers ending in 2:
total += 2 + 22

#numbers ending in 3:
n = 3
while n < 963:
	total += n
	n += 10
total += 973

#numbers ending in 4:
total += 4 + 14 + 34

#numbers ending in 5:
n = 5
while n < 945:
	total += n
	n += 10
total += 955

#numbers ending in 6:
total += 6 + 16 + 26 + 46

#numbers ending in 7:
n = 1
while n < 957:
	total += n
	n += 10
total += 967

#numbers ending in 8:
total += 8 + 28

#numbers ending in 9:
n = 1
while n < 969:
	total += n
	n += 10
total += 970

print total