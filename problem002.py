fibs = [1,1]
summ = 0
while fibs[-1] <= 4000000:
	fibs.append(fibs[-1]+fibs[-2])
	if fibs[-1] % 2 == 0:
		summ = summ + fibs[-1]

print summ