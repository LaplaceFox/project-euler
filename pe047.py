from primes import nextPrime
from copy import copy
import time

start = time.time()

N = 4

class PFObj:
    def __init__(self, primes, exps):
        self.primes = primes
        self.exps = exps

        self.val = 1
        for i in range(N):
            self.val *= self.primes[i] ** self.exps[i]
    
    def __repr__(self):
        return "{P: " + str(self.primes) + ", E: " + str(self.exps) + "}"

    def val(self):
        return self.val

    def nexts(self):
        nextlist = []
        nextp = nextPrime(max(self.primes))
        if self.exps == [1] * N:
            for i in range(N):
                newPrimes = copy(self.primes)
                newPrimes[i] = nextp
                newPrimes.sort()
                nextlist.append(PFObj(newPrimes, self.exps))
        for i in range(N):
            newExps = copy(self.exps)
            newExps[i] += 1
            nextlist.append(PFObj(self.primes, newExps))

        return nextlist

seed = PFObj([2,3,5,7],[1,1,1,1])
found = []

amt = 2500
thresh = amt

small = [seed]
big = []


while True:
    if small == []:
        thresh += amt
        small = list(filter(lambda x: x.val < thresh, big))
        big = list(filter(lambda x: x.val >= thresh, big))

    top = small.pop(small.index(min(small, key = lambda x: x.val)))
    
    if top.val in found:
        continue

    #print(top.val)

    found.append(top.val)

    newPFs = top.nexts()

    for x in newPFs:
        if x.val < thresh:
            small.append(x)
        else:
            big.append(x)

    if found[-N:] == list(range(found[-1]-N+1, found[-1]+1)):
        print(found[-N:])
        break

print("Time taken:",time.time()-start,chr(7))