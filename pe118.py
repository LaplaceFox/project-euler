from copy import copy
from primes import isPrime

def numFromDigits(digits, lo):
    digits.sort() # Just in case

    allNums = copy(digits)

    i = 0
    while i < len(allNums):
        cur = allNums[i]
        new = [cur*10 + d for d in digits if str(d) not in str(cur)]

        allNums.extend(new)
        i += 1

    return allNums

def primeSets(digits, lo, acc):
    if digits == []:
        print(acc)
        return 1

    if len(digits) < len(str(lo)):
        return 0

    allNums = numFromDigits(digits, lo)

    count = 0

    for n in allNums:
        if isPrime(n) and n > lo:
            count += primeSets([d for d in digits if str(d) not in str(n)], n, acc + [n])

    return count
