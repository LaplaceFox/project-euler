from primes import megasieve
from timeme import *

# Remainder of (a+1)**n + (a-1)**n mod n**2
def remainder(a,n):
    if n % 2 == 0:
        return 2
    else:
        return 2*a*n

def solution():
    primelist = megasieve(10**6)

    for i in range(len(primelist)):
        n = i+1
        if remainder(primelist[i],n) > 10**10:
            return n
        
    return None

timeme(solution)