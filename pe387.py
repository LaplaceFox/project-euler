from primes import isPrime
from time import time

def digitSum(n):
    return sum(map(int,str(n)))

def buildHarshad(seed):
    # Test extending with digits, return list of Harshad numbers
    digSum = digitSum(seed)
    return list(map(lambda x: x[0], 
                    filter(lambda y: y[0] % y[1] == 0, 
                           map(lambda z: (seed*10+z, digSum+z),
                               range(10)))))

def isStrong(n):
    # Assume n is Harshad
    return isPrime(n // digitSum(n))

def buildPrime(seed):
    return list(filter(isPrime, map(lambda x: seed*10+x, [1,3,7,9])))

def SRTHP(size):
    begin = time()

    # Size is max # of digits in SRTHP
    n = size - 1 # Size of largest allowed Harshad

    found = []

    workset = list(range(1,10))

    while workset != []:
        cur = workset.pop(0)

        if isStrong(cur):
            found += buildPrime(cur)

        if len(str(cur)) < n:
            workset = buildHarshad(cur) + workset

    print("Time taken:", time()-begin)

    return found