import sys

exit = False
a = 1
b = 10
cubes = [1]
n = 2
c = n**3
while True:
	while c < b:
		cubes.append(c)
		n += 1
		c = n**3
	cubeintcounts = []
	for cube in cubes:
		cubelist = map(int, list(str(cube)))
		cubeintcounts.append([])
		for dig in xrange(0,10):
			cubeintcounts[-1].append(cubelist.count(dig))
	for x in xrange(0, len(cubeintcounts)):
		if cubeintcounts.count(cubeintcounts[x]) == 5:
			print cubes[x]
			exit = True
	if exit:
		sys.exit()
	cubes = []
	a*=b
	b*=10

