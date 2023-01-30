from math import *
from timeme import timeme

def solution():
    tmax = 1000000

    sizes = [0]*(tmax+1)

    for k in range(1,ceil(sqrt(tmax)/2) + 1):
        for i in range(4*k*(k+1), tmax, 4*k):
            sizes[i] += 1

    sizes = [s for s in sizes if s > 0]

    res = 0
    for x in range(1,11):
        res += sizes.count(x)

    return res

timeme(solution)