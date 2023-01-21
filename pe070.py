from primes import megasieve

def totient(n, primelist):
    if n in primelist:
        return n-1

    tot = 1

    ind = 0
    while n > 1:
        p = primelist[ind]
        ct = 0
        while n % p == 0:
            ct += 1
            n //= p
        if ct > 0:
            tot *= p**(ct-1) * (p-1)
        ind += 1
    
    return tot

def solution():
    n = 10**7

    primelist = megasieve(n//2)

    for i in range(1,n):
        tot = totient(i,primelist)
        if i % 1000 == 0:
            print(i, tot)