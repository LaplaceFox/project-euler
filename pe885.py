from timeme import timeme

def compositions(n, b):
    # List of compositions of n into b bins
    bins = 0
    comps = [[]]

    while bins < b-1:
        newcomps = []

        for c in comps:
            remaining  = n - sum(c) # How many objects left to place

            #print("extending", c)
            new = [c + [i] for i in range(remaining+1)]
            #print(new)

            #input()

            newcomps += new
        
        comps = newcomps
        bins += 1

    # Last bin is forced
    return [c + [n-sum(c)] for c in comps]

def digit_composition_to_number(c):
    if len(c) != 10:
        assert ValueError
    
    s = "".join([str(i)*c[i] for i in range(10)])
    return int(s)

memo = {0:1}

def fact(n):
    if n in memo:
        return memo[n]
    
    res = n * fact(n-1)
    memo[n] = res
    return res

def multinomial(c):
    res = fact(sum(c))

    for k in c:
        res //= fact(k)

    return res

def solution():
    MODULUS = 1123455689

    comps = compositions(18,10)

    total = 0

    for c in comps:
        total += multinomial(c) * digit_composition_to_number(c)
        total %= MODULUS

    return total


timeme(solution)