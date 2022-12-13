from math import *

def period_len(n):
    # List of seen (k,d) pair
    seen = []

    fsn = floor(sqrt(n))  # precompute

    pair = (0,1)

    while pair not in seen:
        (k,d) = pair
        seen.append(pair)
        m = d*floor((fsn+k)/d)-k  # intermediate value
        pair = (m, (n-m**2)//d)

    return len(seen) - seen.index(pair)

def solution():
    squares = [x**2 for x in range(101)]

    odd_pd = 0

    for i in range(1,10001):
        if i not in squares:
            odd_pd += period_len(i) % 2
    
    return odd_pd