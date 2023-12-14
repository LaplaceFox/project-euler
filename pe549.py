from copy import deepcopy as copy
from primes import megasieve
from timeme import timeme

# Smallest factorial that has p^k as a factor
def prime_power_s(p,k):
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

def list_dict_insert(D, k, v):
    if k in D:
        D[k].append(v)
    else:
        D[k] = [v]

def S(n):
    primelist = megasieve(n)

    print("primes found")

    small_primes = [p for p in primelist if p**2 <= n]
    big_primes = [p for p in primelist if p**2 > n]

    print("primes sorted")

    total = 0

    found = {0:[1]}

    new_dict = {}

    for p in small_primes:
        #print(p)
        threshold = n/p  # If a number is above this, don't add to new dict, then add s-value to total

        for key in found:
            for num in found[key]:
                if num > threshold:
                    total += key # add s-value to total
                    #print(num, "too big, total is", total)
                    continue

                k = 0
                while num * (p**k) <= n:
                    new_key = max(key, prime_power_s(p,k))
                    list_dict_insert(new_dict, new_key, num * (p**k))

                    k += 1

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

timeme(solution)