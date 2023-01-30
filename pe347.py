from math import *
from primes import megasieve
from timeme import timeme

def M(p,q,N):
    if p * q > N:
        return 0

    vals = []

    k = 1
    while p**k <= N:
        l = floor(log(N/(p**k),q))

        if l == 0:
            break

        vals.append(p**k * q**l)
        k += 1

    return max(vals)

def solution():
    N = 10**7

    p = megasieve(N)

    tot = 0

    for i in range(len(p)):
        if p[i]**2 > N:
            break

        for j in range(i+1,len(p)):
            res = M(p[i],p[j],N)

            if res == 0:
                break

            tot += res

    return tot 

timeme(solution)