primes = [2]

for counter in range(3, 100):
    isprime = True
    for p in primes:
        if (counter % p == 0):
            isprime = False
    if isprime:
        primes = primes.append(counter)
    print primes

print primes