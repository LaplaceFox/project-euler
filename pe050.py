from primes import *
from copy import copy as copy

consecutive = []
psum = 0

bestchain = []
bestlen = 0
bestnum = 0

bound = 1000000

n=1
while True:
    next = nextPrime(n)
    consecutive.append(next)
    psum += next
    n = next

    if psum >= bound:
        # Pop off last one
        psum -= consecutive.pop()
        break

while not isPrime(psum):
    psum -= consecutive.pop()

# We know this meets the conditions we need
bestchain = copy(consecutive)
bestlen = len(consecutive)
bestnum = psum


lowend = 2 # Lowest prime in the range
while True:
    lowend = nextPrime(lowend)
    chain = copy(bestchain)
    psum = sum(chain)

    # Shift best range until it starts with the correct prime
    while chain[0] < lowend:
        psum -= chain.pop(0)
        chain.append(nextPrime(chain[-1]))
        psum += chain[-1]

    if psum >= bound:
        break

    # Can continue to extend
    while psum < bound:
        chain.append(nextPrime(chain[-1]))
        psum += chain[-1]

        if isPrime(psum):
            # New best!
            bestchain = copy(chain)
            bestlen = len(chain)
            bestnum = psum

print(bestnum)
