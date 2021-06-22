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

def run():
    inc = 1504170715041707
    modulus  = 4503599627370517

    inverse = invEuclid(modulus, inc)

    total = inc
    mn = total

    current = total

    # Loop for initial mining
    while mn > 10**9:
        current = (current + inc) % modulus

        if current < mn:
            # Found a coin!
            print("Coin:", current)
            total += current

            diff = mn - current

            while diff < current:
                current -= diff # Next coin
                print("Coin:", current)
                total += current

            mn = current

    # Goal is now "small"
    while mn > 0:
        best_n = (mn * inverse) % modulus

        for test in range(mn-1,0,-1):
            n = (test * inverse) % modulus

            if n > best_n:
                best_n = n

                current = test
                diff = mn - current

                while diff < current:
                    current -= diff # Next coin
                    print("Coin:", current)
                    total += current

                mn = current
                break

    return total


timeme(run)