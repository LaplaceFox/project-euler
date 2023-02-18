from itertools import *
from primes import megasieve
from timeme import timeme

primelist = megasieve(50)

def prime_factorization(n, primelist):
    res = []

    for i in range(len(primelist)):
        if n <= 1:
            return res

        p = primelist[i]

        ct = 0
        while n % p == 0:
            n //= p
            ct += 1
        
        res.append(ct)

    return res

def add_elementwise(A,B,fill):
    return [a+b for (a,b) in zip_longest(A,B,fillvalue=fill)]

def sub_elementwise(A,B,fill):
    return [a-b for (a,b) in zip_longest(A,B,fillvalue=fill)]

factorial_pfacts = {0:[]}

def populate_dict():
    acc = []
    for i in range(51):
        acc = add_elementwise(acc,prime_factorization(i, primelist),0)
        factorial_pfacts[i] = acc

populate_dict()

# Prime factorization for a binomial coefficient
def binomial_pfact(n,k):
    acc = factorial_pfacts[n]
    acc = sub_elementwise(acc, factorial_pfacts[k], 0)
    acc = sub_elementwise(acc, factorial_pfacts[n-k], 0)

    return acc

# Max defaulting to 0
def my_max(L):
    if L == []:
        return 0
    return max(L)

def pf_to_value(pf):
    res = 1

    for i in range(len(pf)):
        res *= primelist[i]**pf[i]
    
    return res

def solution():
    to_check = [(n,k) for (n,k) in product(range(51),range(51)) if k <= n]
    squarefree = [binomial_pfact(n,k) for (n,k) in to_check if my_max(binomial_pfact(n,k)) < 2]

    return sum(set([pf_to_value(pf) for pf in squarefree]))

timeme(solution)