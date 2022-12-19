from copy import copy
import math

def isPrime(n):
    if n < 2:
        return False
    for k in range(2, math.floor(math.sqrt(n)) + 1):
        if n%k == 0:
            return False
    return True

def nextPrime(n):
    while True:
        n += 1
        if isPrime(n):
            return n

# Sieve of Erosthastenes, over range [lo,hi] and pile is all primes less than lo
# Returns all newly found primes in range, destructively modifies pile
def sieve(lo, hi, pile=[]):
    # lo is at least 2
    lo = max(lo,2)

    toSieve = range(lo,hi+1)

    # List of all primes in desired range
    in_range = []

    for p in pile:
        if lo <= p <= hi:
            in_range.append(p)
        toSieve = list(filter(lambda x: x%p != 0, toSieve))

    while len(toSieve) > 0:
        toSieve = list(toSieve)
        p = toSieve.pop(0)

        print(p)
        if p*p > hi:
            pile.extend(toSieve)
            in_range.extend(toSieve)
            return in_range

        pile.append(p)
        in_range.append(p)
        toSieve = list(filter(lambda x: x%p != 0, toSieve))
    return in_range

def megasieve(n):
    toSieve = list(range(n+1))
    toSieve[0] = None
    toSieve[1] = None

    for k in range(math.floor(math.sqrt(n+1))+1):
        if toSieve[k] != None:
            toSieve[2*k::k] = [None]*len(toSieve[2*k::k])
            #print("tick",end=" ")

    #print()
    return list(filter(lambda x: x != None, toSieve))