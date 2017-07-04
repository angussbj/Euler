import itertools

permutations_tuples = itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
permutations_ints = []
for permutation in permutations_tuples:
	permutations_ints.append(int(''.join(map(str, permutation))))
permutations_ints.sort()
print permutations_ints[999999]