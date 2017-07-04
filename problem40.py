done = False
string = ""
n = 1
while not done:
	string += str(n)
	if len(string) >= 1000000:
		done = True
	n += 1
product = 1
for i in xrange(0, 7):
	product *= int(string[10**i-1])
print product