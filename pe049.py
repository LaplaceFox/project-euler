from primes import isPrime

def strSort(s):
    return "".join(sorted(list(str(s))))

digits = {}

for i in range(1000,10000):
    if isPrime(i):
        ss = strSort(i)
        if ss in digits:
            digits[ss].append(i)
        else:
            digits[ss] = [i]

allKeys = list(digits.keys())

for ss in allKeys:
    if len(digits[ss]) < 3:
        del digits[ss]

for ss in digits:
    primeList = digits[ss]

    for p in primeList:
        diff = list(map(lambda x: abs(x-p), primeList))
        if len(set(diff)) != len(diff):
            print(primeList)