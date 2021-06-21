from math import sqrt
from time import time

def isSquare(n):
    return n == int(sqrt(n))**2


def run(bound):
    begin = time()

    candidates = [0]

    for k in range(1,bound):
        new = []
        for i in range(100):
            for n in candidates:
                test = i*10**(2*k-1) + n

                if (test**2 // 10**(2*k)) % 10 == 10-k:
                    if str(test**2)[::2] == "1234567890":
                        return test

                    new.append(test)
        candidates = new

    print("Time taken:", time()-begin)