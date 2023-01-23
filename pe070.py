from primes import megasieve

# Return list of all 1 < n < bound such that n has prime factors pfacts
def with_radical(pfacts,bound):
    found = []
    
    vec = [1] * len(pfacts)

    # Already too big?
    if get_val(pfacts, vec) >= bound:
        return found

    while get_val(pfacts,vec) < bound:
        val = get_val(pfacts, vec)
        while val < bound:
            # Increment smallest factor's exponent
            found.append(val)
            vec[0] += 1
            val = get_val(pfacts, vec)

        # Rollover
        for i in range(len(vec)+1):
            # Overflow
            if i == len(vec):
                return found

            if vec[i] > 1:
                vec[i] = 1
            else:
                vec[i] += 1
                break

    return found

def get_val(pfacts,vec):
    val = 1
    for i in range(len(vec)):
        val *= pfacts[i] ** vec[i]
    
    return val

def unique_facts(n, primelist):
    res = []
    i = 0
    for p in primelist:
        if n % p == 0:
            res.append(p)
        
        while n % p == 0:
            n //= p

        if n == 1:
            return res
        
    return res

def unique_radicals(bound):
    primelist = megasieve(bound)

    to_check = list(range(bound))

    # Ignore 0 and 1
    to_check[0:2] = [None]*2

    for i in to_check:
        if i == None:
            continue

        with_rad = with_radical(unique_facts(i, primelist), bound)

        for k in with_rad[1:]:
            to_check[k] = None
        
    return list(filter(lambda x: x != None, to_check))