values = []

for a in xrange(2,101):
	for b in xrange(2,101):
		values.append(a**b)

terms = long(len(values))
print terms
for value in values:
	count = values.count(value)
	terms -= (count-1.0)/count
print terms