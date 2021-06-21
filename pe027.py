import primes

best = (0,0)
mostPrimes = 39 # Start at n = 39; given that much

sieve = set(primes.sieve(100000))

def isPrime(n, sieve):
    if n in sieve:
        return True
    return primes.isPrime(n)

for a in range(-999,1000):
    print(a)
    for b in range(-a,1001):
        n = 0
        while isPrime(n**2 + a*n + b, sieve):
            n += 1
        if n-1 > mostPrimes:
            best = (a,b)
            mostPrimes = n-1
print(best)
