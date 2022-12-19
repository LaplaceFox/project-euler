from math import *
from primes import sieve
from timeme import *

def solution():
    pile = [] # Pile for sieving primes
    reversible = [] # Found reversible primes
    
    for n in range(1,100):
        lo = ceil(sqrt(10**(n-1)))
        hi = floor(sqrt(10**n))
    
        new_primes = sieve(lo,hi,pile)

        # Primes that are length n when squared
        squares = set(map(lambda x: x**2, new_primes))

        # print(squares)

        for x in squares:
            s = str(x)

            # Ignore palindromes
            if s == s[::-1]:
                continue

            if int(s[::-1]) in squares:
                reversible.append(x)
        
        reversible.sort()

        print(len(reversible), ":", reversible)
        
        if len(reversible) >= 50:
            return reversible[49]

timeme(solution)