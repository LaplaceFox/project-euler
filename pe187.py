from primes import sieve
from time import time
from math import sqrt, floor

def semiprimesUpTo(n):
    # First prime is 2, so we only need primes up to n//2

    primeList = megasieve(n//2)

    print("Primes computed.")

    count = 0

    while primeList != []:
        p = primeList[0]
        primeList = list(filter(lambda x: x <= (n//p), primeList))

        print(len(primeList))
        count += len(primeList)

        # Done with lowest prime
        if len(primeList) > 0:
            primeList.pop(0)

    return count

def megasieve(n):
    toSieve = list(range(n+1))
    toSieve[0] = None
    toSieve[1] = None

    for k in range(floor(sqrt(n+1))+1):
        if toSieve[k] != None:
            toSieve[2*k::k] = [None]*len(toSieve[2*k::k])
            print("tick",end=" ")

    print()
    return list(filter(lambda x: x != None, toSieve))


begin = time()
print(semiprimesUpTo(10**8))
print("Time taken:", time()-begin, chr(7))