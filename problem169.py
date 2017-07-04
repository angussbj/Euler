import time

number = 10**12

def isequal(lst1, lst2):
	if len(lst1) != len(lst2):
		return False
	for i in xrange(0, len(lst1)):
		if lst1[i] != lst2[i]:
			return False
	return True

start = time.time()
lst = []
n = 0
while 2**(n+1) <= number:
	n += 1
p = 2**n
lst.append(p)
number -= p
while number != 0:
	while 2**(n) > number:
		n -= 1
	p = 2**n
	lst.append(p)
	number -= p

lsts = [lst]
progress = [0]
j = 0
while j < len(lsts):
	for i in xrange(progress[j], len(lsts[j])):
		# print lsts[j], ", ", progress[j], ", ", i
		if lsts[j][i] == 1:
			continue
		if i != len(lsts[j])-1:
			if lsts[j][i] == lsts[j][i+1] or lsts[j][i] == 2*lsts[j][i+1]:
				continue
		lsts.append(lsts[j][:])
		if i == 0:
			progress.append(0)
		elif lsts[j][i-1] == 2*lsts[j][i]:
			progress.append(i-1)
		else:
			progress.append(i)
		lsts[-1].insert(i + 1, lsts[j][i] / 2)
		lsts[-1][i] = lsts[j][i]/2
		# print lsts[j], ", ", lsts
		# for k in xrange(0, len(lsts) - 1):
		# 	if isequal(lsts[k], lsts[-1]):
		# 		del lsts[-1]
		# 		del progress[-1]
		# 		print "USED"
		# 		break	
	j += 1
print time.time()-start

# print lsts
# print progress
print len(lsts)
