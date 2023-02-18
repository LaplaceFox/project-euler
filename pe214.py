import math
from timeme import timeme

def totsieve(n):
    toSieve = list(range(n+1))
    toSieve[0] = None
    toSieve[1] = None

    totients = [1]*(n+1)
    totients[0] = None
    totients[1] = None

    for p in range(n+1):
        if toSieve[p] != None: # k is prime
            if p <= math.floor(math.sqrt(n+1))+1:
                toSieve[2*p::p] = [None]*len(toSieve[2*p::p])

            for i in range(p,n+1,p):
                totients[i] *= p-1

            k = 2
            while p**k <= n:
                for i in range(p**k,n+1,p**k):
                    totients[i] *= p
                k += 1
    
    primelist = list(filter(lambda x: x != None, toSieve))

    return (primelist,totients)

def chainlength(n, tots):
    ct = 1
    while n != 1:
        n = tots[n]
        ct += 1
    return ct

def solution():
    (pl, tots) = totsieve(4*10**7)
    return sum(filter(lambda x: chainlength(x,tots) == 25, pl))


timeme(solution)