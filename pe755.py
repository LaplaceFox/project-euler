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

def s(n, subcall = False):
    fib = fib_up_to(n)

    if n < 0:
        return 0
    
    if n == 0:
        return 1

    # largest such that fib[k+2]-2 <= n
    k = fib.index(max(filter(lambda x: x <= n+2, fib))) - 2

    res = 2**k

    k += 1

    while n - fib[k] >= 0:
        if not subcall:
            print(res, "+", "calling", "s(%i)"%(n - fib[k]))
        
        res += s(n - fib[k], True)
        k += 1
    
    return res