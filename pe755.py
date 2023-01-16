from timeme import *

def fib_up_to(n):
    fib = []

    tup = (1,1)

    # hopefully 2n is a safe upper bound?
    while tup[0] <= 2*n:
        (a,b) = tup
        fib.append(a)

        tup = (b,a+b)

    return fib

def s(n, maxfib=float("inf"), subcall = False):
    fib = fib_up_to(n)

    if n < 0:
        return 0
    
    if n == 0:
        return 1

    # largest such that fib[k+2]-2 <= n
    k = fib.index(max(filter(lambda x: x <= n+2, fib))) - 2

    res = 2**k
    #print(2**k)

    k += 1

    while n - fib[k] >= 0 and fib[k] < maxfib:
        #if not subcall:
            #print("Place a %i, s(%i)"%(fib[k],n-fib[k]))
            #print(res, "+", "calling", "s(%i)"%(n - fib[k]))
        
        res += s(n - fib[k], fib[k], True)
        k += 1
    
    return res

# Bitvecs up to value v
def bitvecs(v):
    ct = 0
    i = 0
    while True:
        vec = list(map(int,"{0:b}".format(i)))[::-1]

        if value(vec) <= v:
            print(vec, value(vec))
            ct += 1
    
        if value(vec) > 2*v:
            break

        i += 1
    return ct

# Value of bitvector as a Fibonacci sum
def value(vec):
    fib = fib_up_to(2**len(vec))
    fib = fib[1:] # get rid of duplicate 1

    res = 0
    for i in range(len(vec)):
        res += vec[i] * fib[i]
    
    return res

def solution():
    return s(10**13)

timeme(solution)