from math import *
from timeme import timeme

def solution():
    n = 1
    k = 0
    found = 0

    while found < 678910:
        n *= 2
        k += 1

        if n >= 1000:
            n /= 10

        if floor(n) == 123:
            found += 1
            #print(found)
    
    return k

timeme(solution)