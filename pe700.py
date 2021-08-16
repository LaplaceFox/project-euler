from timeme import *

def invEuclid(a,b):
    modulus = a
    # a > b
    coeff = []

    while b > 0:
        coeff.append(a // b)
        a, b = b, a%b

    # Now inverse

    m, n = (0,1)

    # Skip last coefficient
    for c in coeff[:-1]:
        m, n = n, m - c*n

    return n % modulus

def bigones():
    inc = 1504170715041707
    modulus  = 4503599627370517

    total = inc

    inverse = invEuclid(modulus, inc)

    def inv(n):
        return (n * inverse) % modulus

    current = inc
    mn = current

    while True:
        current = (current + inc) % modulus

        if current < mn:
            total += current
            print("Coin:", current, "at", inv(current))

            # Mining time!
            diff = mn - current

            while current > diff:
                current -= diff
                total += current
                idx = inv(current)
                print("Coin:", current, "at", inv(current))

            mn = current

        if current == 15806432:
            return total


def smallones():
    inc = 1504170715041707
    modulus  = 4503599627370517

    inverse = invEuclid(modulus, inc)

    def inv(n):
        return (n * inverse) % modulus

    biggest = 1
    idx = inv(1)

    total = 1

    current = 1

    while current < inc:

        current += 1

        # If we find next largest number we'd hit earlier
        if inv(current) < idx:
            total += current
            idx = inv(current)
            print("Coin:", current, "at", idx)
            
            if current == 15806432:
                return total - 15806432 # Don't double count

def run():
    return smallones() + bigones()

timeme(run)