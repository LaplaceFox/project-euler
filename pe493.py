from math import comb, factorial, prod
from timeme import timeme
from pe710 import ord_partitions

def unordered_partitions(n):
    # Sort all partitions, make hashable, then deduplicate
    return list(set([tuple(sorted(P)) for P in ord_partitions(20)]))

def solution():
    color_profiles = [profile for profile in unordered_partitions(20) if len(profile) <= 7 and max(profile) <= 10]

    # Number of ways a given number of colors can occur
    freq_table = {k:0 for k in range(1,8)}

    for prof in color_profiles:
        # Assuming fixed colors, number of ways profile can occur
        ways = prod([comb(10,x) for x in prof])

        # Find number of ways to allocate colors to indices of the profile
        partcounts = [prof.count(x) for x in set(prof)] # deduplicate, count occurences of each quantity
        partcounts.append(7 - sum(partcounts)) # add number of "empty" groups

        color_alloc = factorial(7)
        for pc in partcounts:
            color_alloc //= factorial(pc)

        ways *= color_alloc

        freq_table[len(prof)] += ways

    total = sum(freq_table.values())

    return sum([k*freq_table[k] for k in freq_table])/total

timeme(solution)