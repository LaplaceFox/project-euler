from primes import isPrime
from math import sqrt, floor

cur = 33 # Given this much in the problem statement
while True:
    found = False
    if not isPrime(cur): # Composite
        for i in range(1, floor(sqrt(cur/2)) + 1):
            if isPrime(cur - (2 * i**2)):
                found = True
                print(cur, "= 2 *", i**2, "+", cur - (2 * i**2))
                break
        if not found:
            print(cur)
            break

    cur += 2 # Only care about odd
