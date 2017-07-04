import math

def dfs(n):
	s = 0
	for d in map(int, list(str(n))):
		s += math.factorial(d)
	return s

def countIsZeroOriIsOutOfRange(i):
	if i > 1000000:
		return True
	elif counts[i] == 0:
		return True
	else:
		return False

counts = [0] * 1000001
counts[169] = 3
counts[363601] = 3
counts[1454] = 3
counts[871] = 2
counts[45361] = 2
counts[872] = 2
counts[45362] = 2

for i in xrange(0, 1000001):
	print i, " : "
	chain = [i]
	count = 0
	while countIsZeroOriIsOutOfRange(i):
		i = dfs(i)
		if i == chain[-1]:
			counts[i] = 1
			break
		chain.append(i)
		count += 1
	count += counts[i]
	for j in xrange(0, len(chain) - 1):
		if chain[j] <= 1000000:
			counts[chain[j]] = count - j

print counts[69]
print counts.count(60)