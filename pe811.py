from math import comb,prod
from timeme import timeme

def b(n):
    i = 0
    while n % 2**i == 0:
        i += 1
    return 2**(i-1)

def A(m):
    if m == 0:
        return 1
    elif m % 2 == 0:
        n = m//2 # let m = 2n
        return 3*A(n) + 5*A(2*n - b(n))
    else:
        n = (m-1)//2
        return A(n)

# Sequence of factors in result
def c(n):
    if n == 0:
        return 1 # implementation detail that makes solution simpler
    else:
        return 3 + 5*c(n-1)
    
# Alternative way of computing A(n)
def alt(n):
    runs = "{0:b}".format(n).split("1")
    return prod([c(i) ** len(runs[i]) for i in range(len(runs))])

##### ACTUAL SOLUTION #####

# b^e mod m
def powmod(b,e,m):
    acc = 1
    while e > 0:
        if e % 2 == 1:
            e -= 1
            acc = (acc * b) % m
        else:
            e //= 2
            b = (b * b) % m
    return acc

# H function with padding P, exponent e, mod m
def H(P,e,m):
    run_lens = []
    tail_len = 0
    # Value of each block size P
    for i in range(1,e+1):
        bin_c = "{0:b}".format(comb(e,i)) # Pascal triangle element

        run_lens.append(P - len(bin_c) + tail_len) # padding length

        new_runs = [len(r) for r in bin_c.split("1")]
        tail_len = new_runs[-1]

        run_lens += new_runs[1:-1]

    res = 1

    f = 8 # factor to build solution
    for r in run_lens:
        res *= powmod(f,r,m) % m
        f = (3 + 5*f) % m
    
    return res % m

def solution():
    return H(10**14 + 31, 62, 1000062031)

timeme(solution)