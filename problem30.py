n = 0
summ = 0
while n<10000000:
	nlst = map(int, list(str(n)))
	powsum = 0
	for digit in nlst:
		powsum += digit**5
	if powsum == n:
		summ += n
		print summ
	n += 1
	if n%1000000 == 0:
		print n