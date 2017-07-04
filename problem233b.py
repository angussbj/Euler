import numpy as np

# brute force method: check all the points on an eighth of the circle and multiply up using symmetry
def f(N):
	count = 0
	for x in xrange(int(np.ceil(N*(1-np.sqrt(2))/2)), 0):
		y = N/2.0 + np.sqrt(N**2/2.0 - (N/2.0 - x)**2)
		if y % 1 == 0:
			count += 2
		if count >= 105:
			return 0
	#deal with extreme points of x or y being over counted
	x = N*(1+np.sqrt(2))/2
	if x % 1 == 0:
		if N/2.0 + np.sqrt(N**2/2.0 - (N/2.0 - x)**2) % 1 == 0:
			count -= 2
	return count * 4 + 4

# gcd algorithm assuming a > b
def gcd_fast(a, b):
	if b == 0:
		return a
	else:
		return gcd_fast(b, a % b)

# gcd algorithm without that assumption
def gcd(a, b):
	if a < b:
		return gcd_fast(b, a)
	if a > b:
		return gcd_fast(a, b)
	else:
		return a

def lcm_pair(a, b):
	return a*b/gcd(a,b)

def lcm(numbers):
	if len(numbers) == 1:
		return numbers[0]
	new_numbers = []
	for i in xrange(0, len(numbers) - 1, 2):
		new_numbers.append(lcm_pair(numbers[i], numbers[i+1]))
	if len(numbers) % 2 == 1:
		new_numbers.append(numbers[-1])
	print new_numbers
	return lcm(new_numbers)

def factorise(n, primes):
	return None

def generate_primes_up_to(n):
	alength = int(np.floor(n/2))
	values = [True] * alength
	for i in xrange(1, int(np.floor(alength/3))):
		print "AAA"
		for j in xrange(1, i + 1):
			c = i + j + 2*i*j
			if c < alength:
				break
			values[c] = False
			print values
	primes = [2]
	for i in xrange(1, alength):
		if values[i]:
			primes.append(2*i + 1)
	return primes

print generate_primes_up_to(20)






'''
cs = []
m = 2
capp = 500**2 # 10**11
cap = np.sqrt(capp)
while m < cap:
	if m % 1000 == 0:
		print m
	if m % 2 == 0:
	 	for n in xrange(1, m, 2):
	 		c = m**2 + n**2
	 		if c > capp:
	 			break
	 		if gcd(m, n) == 1:
	 			cs.append(m**2 + n**2)
	else:
	 	for n in xrange(2, m, 2):
	 		c = m**2 + n**2
	 		if c > capp:
	 			break
	 		if gcd(m, n) == 1:
	 			cs.append(m**2 + n**2)
 	m += 1

print "number of cs: ", len(cs)


print cs[:52]
cs.sort()
print cs[:52]
print lcm(cs[:52])
'''


'''
for n in xrange(1,10**7):
	total = 4
	for c in cs:
		if n % c == 0:
			total += 8
	if total > 20:
		print n, total
	if n % 100 == 0:
		print n
'''

#for i in xrange(10**3):
#	print i, f(i)




















