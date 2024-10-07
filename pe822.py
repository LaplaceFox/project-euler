from mylib import bigpowmod
from primes import isPrime
from timeme import timeme

# Reference implementation
def squaresmall_naive(n,k):
    l = list(range(2,n+1))

    for i in range(k):
        l[l.index(min(l))] **= 2
        
    return sum(l)

# Initial steps
def onestep(l):
    l[l.index(min(l))] **= 2
    return l

# One squaring step, mod m
def onestep_mod(l,m):
    i_min = l.index(min(l))
    l[i_min] = l[i_min]**2 % m
    return l

# "Steady state" of L where repeated steps square each element once before repeating
def invariant_state(L):
    return max(L) < min(L)**2

# Computes n**(2**k) % p
# p must be prime
def fast_squarings(n,k,p):
    # Fermat's Little Theorem to find exponent
    exp = bigpowmod(2,k,p-1)

    return bigpowmod(n,exp,p)

def solution():
    MODULUS = 1234567891
    STEPS_GOAL = 10**16
    SIZE = 10**4 - 1

    L = list(range(2,SIZE + 2)) # In this case, list goes from 2 to 10000

    steps = 0

    while not invariant_state(L):
        L = onestep(L)
        steps += 1

    # List is now in steady state

    while (STEPS_GOAL - steps) % SIZE != 0:
        L = onestep(L)
        steps += 1
    
    # Remaining steps hit all elements the same number of times
    # Therefore, order no longer matters

    squarings = (STEPS_GOAL - steps) // SIZE # Number of squarings on each element

    L = [fast_squarings(x,squarings,MODULUS) for x in L]

    return sum(L) % MODULUS

timeme(solution)