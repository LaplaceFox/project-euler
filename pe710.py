from timeme import timeme

# Reference implementations

def ord_partitions(n):
    if n == 0:
        return []

    partitions = [[n]]

    for i in range(1,n+1):
        partitions += list(map(lambda x: [i] + x, ord_partitions(n-i)))

    return partitions

def num_twopals(n):
    return len(list(filter(lambda p: 2 in p, ord_partitions(n))))

def num_pal_twopals(n):
    twopals = list(filter(lambda p: 2 in p, ord_partitions(n)))

    ct = 0

    for l in twopals:
        if l == l[::-1]:
            print(l)
            ct += 1

    return ct

# # # Faster stuff

def twopal_fast(n):
    (a,b,c,d) = (1,0,0,0)

    for i in range(n-1):
        (a,b,c,d) = (a+d, a, b+2*c, b+d)
    
    return b+c

def pal_twopal_fast(n):
    k = n // 2

    res = 0

    for i in range(k+1):
        res += twopal_fast(i)
    
    if n % 2 == 0:
        res -= twopal_fast(k-1)
        res += 2**(k-2)

    return res

def test():
    for i in range(1,24):
        x1 = timeme(lambda: num_twopals(i))
        x2 = timeme(lambda: twopal_fast(i))

        assert(x1 == x2)