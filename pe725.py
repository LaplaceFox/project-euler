from copy import copy
from math import comb, factorial, prod
from timeme import timeme
from pe710 import ord_partitions

def unordered_partitions(n):
    # Sort all partitions, make hashable, then deduplicate
    return list(set([tuple(sorted(P)) for P in ord_partitions(n)]))

# Computes number of assignments of "color profile" to total # of objects in profile
def multichoice(prof):
    return factorial(sum(prof)) // prod([factorial(x) for x in prof])

def solution():
    n = 2020

    total = 0

    # Each DS-number has a "sum digit" up to 9
    for dsum in range(10):
        # For each partition of dsum, count the digit frequencies
        digit_freqs = [[p.count(i) for i in range(10)] for p in unordered_partitions(dsum)]
        
        for df in digit_freqs:
            df[dsum] += 1 # Record sum digit
            df[0] = 2020 - sum(df) # Add zeroes

            # Test placing each digit
            for d in range(1,10):
                if df[d] >= 1:
                    prof = copy(df)
                    prof[d] -= 1 # fix this digit in place
                    total += d * multichoice(prof)
    
    total *= (10**17 - 1)//9
    return total % (10**16)

timeme(solution)