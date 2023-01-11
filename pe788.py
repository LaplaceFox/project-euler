from math import *
from timeme import *

MODULUS = 1000000007

memo = {0:1}

def fact(n):
    if n in memo:
        return memo[n]
    
    res = n * fact(n-1)
    memo[n] = res
    return res

def d(k):
    res = 0
    for i in range(k//2 + 1, k+1):
        res += 9**(k-i) * fact(k)//(fact(i)*fact(k-i))
    
    return (res * 9) % MODULUS

def dominating(n):
    res = 0
    for i in range(1,n+1):
        res += d(i)
    
    return res % MODULUS

def solution():
    return dominating(2022)

timeme(solution)