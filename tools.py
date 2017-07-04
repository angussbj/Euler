import math

# A class 
def factorise(n, string=True):
	if not isinstance(n, int) or n < 1:
		raise ValueError("\'factorise\' only works on integers greater than or equal to 1")

	primes = primes_to(math.sqrt(n))

	if isprime(n):
		primes.append(n)

	factors = []
	for p in primes:
		if p > math.sqrt(n):
			if n == 1:
				break
			factors.append(n)
			break
		while n % p == 0:
			factors.append(p)
			n /= p

	if n > primes[-1]:
		factors.append(n)
	
	if string:
		out = ""
		i = 0
		while i < len(factors):
			count = factors.count(factors[i])
			out += str(factors[i])
			if count > 1:
				out += '^' + str(count)
			i += count
			if i < len(factors):
				out += ' * '
		return out
	else:
		return factors


# A class for Gaussian Integers
class GaussianInteger(object):
	
	def __init__(self, a,b):
		if not (a % 1 == 0 and b % 1 == 0):
			raise ValueError("These are Gaussian *integers*. Please give integer inputs.")
		self.a = int(a)
		self.b = int(b)

	def __repr__(self):
		if self.a == 0:
			return "%ii" %(self.b)
		if self.b == 0:
			return str(self.a)
		return "%i + %ii" %(self.a, self.b)

	def __add__(self, other):
		return GaussianInteger(self.a + other.a, self.b + other.b)

	def __neg__(self):
		return GaussianInteger(-self.a, -self.b)

	def __sub__(self, other):
		return self + other.__neg__()

	def __mul__(self, other):
		new_a = self.a * other.a - self.b * other.b
		new_b = self.a * other.b + self.b * other.a
		return GaussianInteger(new_a, new_b)

	def conj(self):
		return GaussianInteger(self.a, -self.b)

	def N(self):
		return self.a^2 + self.b^2

	def __truediv__(self, other):
		if isinstance(other, int):
			if self.a % other == 0 and self.b % other == 0:
				return GaussianInteger(self.a / other, self.b / other)
			else:
				return float('NaN')
		return self * other.conj() / other.N()

# A method that generates all primes less than or equal to n using the Sieve of Sundaram
def primes_to(n):
	primes = [2]
	m = int(math.ceil(n/2))
	array = [True] * m
	for i in range(1, int(math.floor(m/3.0))):
		for j in range(1, i+1):
			c = i + j + 2*i*j
			if c < m:
				array[c] = False
			else:
				break
	for i in range(1, len(array)):
		if array[i]:
			primes.append(2*i + 1)
	return primes



