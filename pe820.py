from math import floor
from mylib import powmod
from timeme import timeme

def nth_digit(n,d):
    return floor(pow(10,n-1,d)*10/d)

def S(n):
    res = 0
    for k in range(1,n+1):
        res += nth_digit(n,k)
    return res

def solution():
    return S(10**7)

timeme(solution)