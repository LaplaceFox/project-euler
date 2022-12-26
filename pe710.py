from timeme import timeme

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

def twopal_vector_iter(n):
    (a,b,c,d) = (1,0,0,0)

    for i in range(n-1):
        (a,b,c,d) = (a+d, a, b+2*c, b+d)
    
    return b+c

for i in range(1,24):
    x1 = timeme(lambda: num_twopals(i))
    x2 = timeme(lambda: twopal_vector_iter(i))

    assert(x1 == x2)