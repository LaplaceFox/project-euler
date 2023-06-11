from math import *
from timeme import timeme

# Generates continued fraction for sqrt(n)
def rootn_cfgen(n):
    fsn = floor(sqrt(n))  # precompute

    pair = (0,1)

    while True:
        # Represents (sqrt(n)+k)/d
        (k,d) = pair

        a = (fsn+k)//d  # coefficient 
        yield a

        m = d*a-k  # intermediate value
        pair = (m, (n-m**2)//d)

def is_square(n):
    return round(sqrt(n))**2 == n

# Minimal solution for x^2 - Dy^2 = 1
def solve_pell(n):
    if is_square(n):
        return None

    hs = (0,1) # numerators of convergents
    ks = (1,0) # denominators of convergents

    for a in rootn_cfgen(n):
        # Recurrence to make next convergent
        h = a*hs[1] + hs[0]
        k = a*ks[1] + ks[0]

        # check for solution
        if h**2 - n*(k**2) == 1:
            return (h,k)
    
        # record found convergent
        hs = (hs[1],h)
        ks = (ks[1],k)

def solution():
    bestD = 0
    bestx = 0

    for D in range(1001):
        if is_square(D): # not valid for pell equation
            continue
        (x,_) = solve_pell(D)

        if x > bestx:
            bestx = x
            bestD = D
        
    return bestD

timeme(solution)