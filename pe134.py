from primes import nextPrime

def getKthDigit(n,k):
    # Where the ones place is 0, tens is 1, etc.
    return (n // (10**k)) % 10

def makePair(p1, p2):
    # Smallest integer divisible by p2 ending with digits of p1
    acc = 0

    for k in range(len(str(p1))):
        # Match each digit of p1
        while getKthDigit(acc,k) != getKthDigit(p1,k):
            acc += p2 * (10**k)

    return acc

bound = 10**6

p1 = 5
total = 0

while p1 < bound:
    total += makePair(p1, nextPrime(p1))
    p1 = nextPrime(p1)
print(total)
