from copy import deepcopy as copy
from math import floor, log
from primes import megasieve
from timeme import timeme

# Smallest factorial that has p^k as a factor
def prime_power_s(p,k):
    if k <= p:
        return k*p

    n = 0
    num_factors = 1
    res = 0

    while num_factors < k:
        n += 1
        num_factors += p**n

    while k > 0:
        res += (k // num_factors) * p**n
        k %= num_factors
        num_factors -= p**n
        n -= 1

    return res * p

def sieve_solution(n):
    primelist = megasieve(n)

    small_primes = [p for p in primelist if p**2 <= n]
    big_primes = [p for p in primelist if p**2 > n]

    total = 0

    to_sieve = [0]*(n+1)
    
    pairs = [(prime_power_s(p,k),p**k) for p in small_primes for k in range(1,floor(log(n,p))+1)]

    pairs.sort()

    for (x,gap) in pairs:
        to_sieve[gap::gap] = [x]*len(to_sieve[gap::gap])

    for p in big_primes:
        to_sieve[p::p] = [0]*len(to_sieve[p::p])
        total += p * (n//p)

    return total + sum(to_sieve)

def list_dict_insert(D, k, v):
    if k in D:
        D[k].append(v)
    else:
        D[k] = [v]

def S(n):
    primelist = megasieve(n)

    small_primes = [p for p in primelist if p**2 <= n]
    big_primes = [p for p in primelist if p**2 > n]

    total = 0

    found = {0:[1]}

    new_dict = {}

    for p in small_primes:
        #print(p)
        threshold = n/p  # If a number is above this, don't add to new dict, then add s-value to total

        precompute = [prime_power_s(p,k) for k in range(floor(log(n,p))+1)]

        for key in found:
            for num in found[key]:
                if num > threshold:
                    total += key # add s-value to total
                    #print(num, "too big, total is", total)
                    continue

                k = 0
                bound = log(n/num, p)

                for b in range(floor(bound)):
                    new_key = max(key, precompute[k])
                    list_dict_insert(new_dict, new_key, num * (p**k))

                    k += 1

                total += max(key, prime_power_s(p,k)) #don't bother adding this one to the dict

        found = copy(new_dict)
        new_dict = {}

        #print(found)

    for k in found:
        total += k * len(found[k])

    for p in big_primes:
        total += p * (n//p)

    return total

def solution():
    return S(10**8)

def sieve_attempt():
    return sieve_solution(10**8)

timeme(sieve_attempt)