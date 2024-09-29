from factors import Factorization
from timeme import *

def pisano_naive(n):
    if n == 1:
        return 0
    
    s = (1,1) # Most recent two Fibonacci numbers
    count = 0

    while True:
        s = (s[1], (s[0] + s[1]) % n)
        count += 1

        if s == (1,1):
            return count
        
fib_memo = {1:1, 2:1}

def fib(n):
    if n in fib_memo:
        return fib_memo[n]
    ans = fib(n-1) + fib(n-2)
    fib_memo[n] = ans
    return ans

def pisano_candidates(n):
    f = Factorization(fib(n)).gcd(Factorization(fib(n-1)-1))
    return f.getDivisors()

def solution():
    bound = 10**9

    p120 = pisano_candidates(120)
    p60 = pisano_candidates(60)
    p40 = pisano_candidates(40)
    p24 = pisano_candidates(24)

    pisano = list(set(p120) - set(p60) - set(p40) - set(p24))

    return sum([x for x in pisano if x < bound])

def solution2(): # Also works! Bit less clever, but just barely slower
    bound = 10**9
    p120 = pisano_candidates(120)
    return sum([x for x in p120 if x < bound and pisano_naive(x) == 120])

timeme(solution)