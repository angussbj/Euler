def dot(A, B):
	if len(A) != len(B):
		return 0
	return sum(i[0]*i[1] for i in zip(A,B))

values = [1, 2, 5, 10, 20, 50, 100, 200]

comb = [0, 0, 0, 0, 0, 0, 0, 1]
total = dot(comb, values)
print (total)
combs = [comb, comb]
deadends = []
i = 1
while comb[0] != total:
	i += 1
	j = len(combs)
	if comb[1] != 0:
		newcomb = list(comb)
		newcomb[1] -= 1
		newcomb[0] += 2
		if combs[-1] != newcomb:
			if combs[-2] != newcomb:
				if combs.count(newcomb) == 0:
					combs.append(newcomb)
	if comb[2] != 0:
		newcomb = list(comb)
		newcomb[2] -= 1
		newcomb[1] += 2
		newcomb[0] += 1
		if combs[-1] != newcomb:
			if combs[-2] != newcomb:
				if combs.count(newcomb) == 0:
					combs.append(newcomb)
		if comb[2] % 2 == 0:
			newcomb = list(comb)
			newcomb[2] -= 2
			newcomb[1] += 5
			if combs[-1] != newcomb:
				if combs[-2] != newcomb:
					if combs.count(newcomb) == 0:
						combs.append(newcomb)
	if comb[3] != 0:
		newcomb = list(comb)
		newcomb[3] -= 1
		newcomb[2] += 2
		if combs[-1] != newcomb:
			if combs[-2] != newcomb:
				if combs.count(newcomb) == 0:
					combs.append(newcomb)
	if comb[4] != 0:
		newcomb = list(comb)
		newcomb[4] -= 1
		newcomb[3] += 2
		if combs[-1] != newcomb:
			if combs[-2] != newcomb:
				if combs.count(newcomb) == 0:
					combs.append(newcomb)
	if comb[5] != 0:
		newcomb = list(comb)
		newcomb[5] -= 1
		newcomb[4] += 2
		newcomb[3] += 1
		if combs[-1] != newcomb:
			if combs[-2] != newcomb:
				if combs.count(newcomb) == 0:
					combs.append(newcomb)
		if comb[5] % 2 == 0:
			newcomb = list(comb)
			newcomb[5] -= 2
			newcomb[4] += 5
			if combs[-1] != newcomb:
				if combs[-2] != newcomb:
					if combs.count(newcomb) == 0:
						combs.append(newcomb)
	if comb[6] != 0:
		newcomb = list(comb)
		newcomb[6] -= 1
		newcomb[5] += 2
		if combs[-1] != newcomb:
			if combs[-2] != newcomb:
				if combs.count(newcomb) == 0:
					combs.append(newcomb)
	if comb[7] != 0:
		newcomb = list(comb)
		newcomb[7] -= 1
		newcomb[6] += 2
		if combs[-1] != newcomb:
			if combs[-2] != newcomb:
				if combs.count(newcomb) == 0:
					combs.append(newcomb)
	comb = combs[i]

	if i % 100 == 0:
		print len(combs) - i

del combs[0]
print len(combs)
