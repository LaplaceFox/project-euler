from math import prod
from primes import megasieve
from timeme import timeme

# Prime factorization of n!
def factorial_pfact(n):
    primelist = megasieve(n)

    pfact = []

    for p in primelist:
        total_factors = 0
        i = 1
        while p**i <= n:
            total_factors += n//(p**i)
            i += 1
        pfact.append((p,total_factors))
    
    return pfact

def factorial_pfact_modified(n,m):
    primelist = megasieve(n)

    pfact = []

    for p in primelist:
        total_factors = 0
        i = 1
        while p**i <= n:
            total_factors += n//(p**i)
            i += 1
        pfact.append(pow(p,2*total_factors,m)+1) # Terms that need to be multiplied to get sum of squares of unitary divisors
    
    return pfact

def solution():
    m = 1000000009
    L = factorial_pfact_modified(10**8, m)
    print("Found prime factorization, list length", len(L))
    res = 1
    for i in L:
        res = (res * i) % m
    return res

timeme(solution)