from math import *
from primes import megasieve
from timeme import *

def solution():
    primes = megasieve(10**8)

    squares = list(map(lambda x: str(x*x), primes))

    sq_lookup = set(squares)

    ct = 0
    tot = 0

    for s in squares:
        rev = s[::-1]
        if s != rev and rev in sq_lookup:
            ct += 1
            print(ct)
            tot += int(s)
        
        if ct == 50:
            return tot

timeme(solution)