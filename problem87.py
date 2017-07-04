max = 50000000

a = 2
square = a**2
numbers = []
while square < max - 24:
	b = 2
	cube = b**3
	sqcb = square + cube
	while sqcb < max-16:
		c = 2
		quart = c**4
		number = sqcb + quart
		while number < max:
			numbers.append(number)
			c += 1
			quart = c**4
			number = sqcb + quart
		b += 1
		cube = b**3
		sqcb = square + cube
	a += 1
	square = a**2


count = len(numbers)
print count
for number in numbers:
	thing = numbers.count(number)
	if thing > 1:
		count -= thing - 1
print count
