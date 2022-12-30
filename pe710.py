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

MILLION = 1000000

vector_memo = {}

vector_memo[0] = (1,0,0,0)
vector_memo[1] = (1,0,0,0)

def twopal_vector(n):
    if n in vector_memo:
        return vector_memo[n]
    
    (a,b,c,d) = twopal_vector(n-1)

    a %= MILLION
    b %= MILLION
    c %= MILLION
    d %= MILLION

    res = (a+d, a, b+2*c, b+d)
    vector_memo[n] = res
    
    return res

def twopal_fast(n):
    (_,b,c,_) = twopal_vector(n)

    return b+c

def pal_twopal_fast(n):
    k = n // 2

    res = 0

    for i in range(k+1):
        res += twopal_fast(i)
    
    if n % 2 == 0:
        res -= twopal_fast(k-1)
        res += 2**(k-2)

    return res % MILLION

def pal_twopals_seq():
    k = 20

    even = pal_twopal_fast(2*k)
    odd = pal_twopal_fast(2*k+1)

    while True:
        print(2*k,": ", even)
        print(2*k+1,": ",odd)

        input()

        even += twopal_fast(k+1) - twopal_fast(k) + twopal_fast(k-1) + 2**(k-2)
        odd += twopal_fast(k+1)

        even %= MILLION
        odd %= MILLION

        if even % MILLION == 0:
            return 2*k
        if odd % MILLION == 0:
            return 2*k+1

        k += 1

def test():
    for i in range(1,20):
        x1 = timeme(lambda: num_twopals(i))
        x2 = timeme(lambda: twopal_fast(i))

        assert(x1 == x2)

timeme(pal_twopals_seq)