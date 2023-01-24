from timeme import *

memo = {0:1}

def fact(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = n * fact(n-1)
        return n * fact(n-1)

def choose(n,k):
    return fact(n) // fact(k) // fact(n-k)

def solution():
    expecteds = [0]
    # expecteds[i] is expected value for problem with i-bit numbers

    # 1 to 32
    for k in range(1,33):
        tot = 2**k

        for i in range(0,k):
            tot += choose(k,i) * expecteds[i]

        expecteds.append(tot/(2**k - 1))

        print(k, expecteds[k])

    return expecteds[32]

timeme(solution)