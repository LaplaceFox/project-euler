from math import *
from timeme import timeme
from primes import megasieve

TARGET = 800800
LOG_TARGET = TARGET * log(TARGET)

# Binary search for largest integer x such that
# p^x * x^p <= (800800 ** 800800)
def bin_search_step(p,lo,hi):
    assert(lo <= hi)

    while lo < hi:
        mid = ceil((lo+hi)/2)

        val = mid*log(p) + p*log(mid)

        if val <= LOG_TARGET:
            lo = mid
        else:
            hi = mid - 1 # Can result in hi < lo
    return lo 

def largest_less_than(L,val):
    lo = 0
    hi = len(L) - 1

    while lo < hi:
        mid = ceil((lo+hi)/2)

        if val < L[mid]:
            hi = mid - 1
        else:
            lo = mid
    return L[lo]

def solution():
    num_hybrid = 0

    bound = bin_search_step(2,0,20000000) # Largest number we'll have to deal with

    primes = megasieve(bound)

    for p in primes:
        # Calculate new bound
        bound = bin_search_step(p,0,bound+1)

        q = largest_less_than(primes,bound)

        if q <= p:
            break

        # Number of primes p < x <= q
        num_hybrid += primes.index(q) - primes.index(p)
    
    return num_hybrid

timeme(solution)