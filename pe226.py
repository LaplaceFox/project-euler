from math import *

# Distance from x to nearest integer
def intdist(x):
    return min(x-floor(x), ceil(x)-x)

def blancmange(x, depth=50):
    res = 0
    for i in range(depth):
        res += intdist(2**i * x) / 2**i
    return res

def intersection(f,g,lo,hi, depth=50):
    for i in range(depth):
        mid = (lo+hi)/2

        if mid == 0:
            return mid

        lo_val  = g(lo) - f(lo)
        mid_val = g(mid) - f(mid)
        hi_val  = g(hi) - f(hi)

        # print("lo ({:.3f}, {:.3f}) | hi ({:.3f}, {:.3f})".format(lo, lo_val, hi, hi_val))

        if (lo_val < 0 < mid_val) or (mid_val < 0 < lo_val):
            hi = mid
        elif (mid_val < 0 < hi_val) or (hi_val < 0 < mid_val):
            lo = mid
        else:
            return None 
        

    return (lo+hi)/2

def bm_circ_inter():
    circ = lambda x: -sqrt(1/2 * x - x*x) + 1/2

    return intersection(blancmange,circ,0,.25)

# Sum of intdist(i * 2**n)/(2**n) from i=0 to x
def intdistsum(x, n):
    res = 0

    # each triangle has base 1 / 2**n, with area 1/2**(2*n + 2)
    full_tri = x // (1/2**n)
    res += 1/2**(2*n+2) * full_tri

    part_tri = x % (1/2**n)

    if part_tri <= 1/2**(n+1):
        res += 1/2 * part_tri**2
    else:
        res += 1/2**(2*n+2) - 1/2 * (1/2**n - part_tri)**2

    return res

def blancmangesum(x, depth=None):
    res = float(0)
    n = 0

    fmt = lambda f: "{:.12f}".format(f)

    prev = fmt(res)

    while True:
        if n == depth:
            break

        # print(prev)
        res += intdistsum(x, n)

        if prev == fmt(res):
            break

        prev = fmt(res)
        n += 1

    return res

# Overall solution to the problem
def solution():
    p = bm_circ_inter()
    q = blancmange(p)

    # Rectangular area
    rect = 1/4 - p/2

    # Trianglular area
    tx = 1/4 - p
    ty = 1/2 - q
    tri = 1/2 * tx * ty

    # Circle section
    theta = pi - acos(4*tx)
    section = 1/32 * theta

    under_circ = rect - tri - section

    half_bm = 1/4

    return half_bm - blancmangesum(p) - under_circ

print(solution())