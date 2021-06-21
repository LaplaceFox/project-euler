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

def sieve(size):
    toSieve = range(2,size)
    pile = []
    while len(toSieve) > 0:
        toSieve = list(toSieve)
        p = toSieve.pop(0)
        pile.append(p)
        toSieve = list(filter(lambda x: x%p != 0, toSieve))
    return pile

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