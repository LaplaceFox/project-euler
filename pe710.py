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

MODULUS = 1000000

vector_memo = {}

vector_memo[0] = (1,0,0,0)
vector_memo[1] = (1,0,0,0)

def twopal_vector(n):
    if n in vector_memo:
        return vector_memo[n]
    
    (a,b,c,d) = twopal_vector(n-1)

    a %= MODULUS
    b %= MODULUS
    c %= MODULUS
    d %= MODULUS

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

    return res % MODULUS

def pal_twopals_seq():
    k = 20

    even = pal_twopal_fast(2*k)
    odd = pal_twopal_fast(2*k+1)

    while True:
        #print(2*k,": ", even)
        #assert(pal_twopal_fast(2*k) == even)
        #print(2*k+1,": ",odd)
        #assert(pal_twopal_fast(2*k+1) == odd)

        if even % MODULUS == 0:
            print("Found!")
            return 2*k
        if odd % MODULUS == 0:
            print("Found!")
            return 2*k+1

        #input()

        even += twopal_fast(k+1) - twopal_fast(k) + twopal_fast(k-1) + 2**(k-2)
        odd += twopal_fast(k+1)

        even %= MODULUS
        odd %= MODULUS

        k += 1

def pal_twopals_seq_faster():
    k = 20

    even = pal_twopal_fast(2*k)
    odd = pal_twopal_fast(2*k+1)

    vprev = twopal_vector(k-1)
    vcurr = twopal_vector(k)
    vnext = twopal_vector(k+1)

    powtwo = 2**(k-2)

    while True:
        tkprev = vprev[1] + vprev[2]
        tkcurr = vcurr[1] + vcurr[2]
        tknext = vnext[1] + vnext[2]

        even %= MODULUS
        odd %= MODULUS

        even += tknext - tkcurr + tkprev + powtwo
        odd += tknext

        vprev = vcurr
        vcurr = vnext

        (a,b,c,d) = vnext
        vnext = (a+d % MODULUS, a % MODULUS, b+2*c % MODULUS, b+d % MODULUS)

        powtwo = powtwo*2 % MODULUS

        k += 1

        if even % MODULUS == 0:
            print("Found!")
            return 2*k
        if odd % MODULUS == 0:
            print("Found!")
            return 2*k+1

def test():
    for i in range(1,20):
        x1 = timeme(lambda: num_twopals(i))
        x2 = timeme(lambda: twopal_fast(i))

        assert(x1 == x2)

timeme(pal_twopals_seq_faster)

# answer: 1275000