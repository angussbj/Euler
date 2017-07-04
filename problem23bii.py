import math
import itertools

abundants = [12, 18, 20, 945, 5775, 6748, 20350, 23205, 26728] #whittled down 16 to 4 by hand




ivalues = []
l = [True] * 28124
for a in xrange(0, 20):
	# print a
	i = 12 * a
	if i > 28123:
		break
	for b in xrange(0, 20):
		i = 12 * a + 18 * b
		if i > 28123:
			break
		for c in xrange(0, 1407):
			i = 12 * a + 18 * b + 20 * c
			if i > 28123:
				break
			for d in xrange(0, 2):
				i = 12 * a + 18 * b + 20 * c + 945 * d
				if i > 28123:
					break
				l[i] = False
				if i == 28123:
					print [a,b,c,d]
				ivalues.append(i)
# print sorted(ivalues)

print 28123 * 28124 / 2

s = 0
i = 0
while i < len(l):
	if l[i]:
		s += i
		# print i
	i += 1
print s