from itertools import *
from timeme import timeme

# All binary partitions of list
def all_splits(L):
    if L == []:
        return [([],[])]
    left  = [([L[0]]+l,r) for (l,r) in all_splits(L[1:])]
    right = [(l,[L[0]]+r) for (l,r) in all_splits(L[1:])]

    return left + right

# All possible values of arithmetic expressions using elements of L
def arith_exp_values(L):
    # Empty has no valid results, one element has exactly that result
    if len(L) <= 1:
        return L

    vals = []
    for (l,r) in all_splits(L):
        if l == [] or r == []:
            continue

        l_vals = arith_exp_values(l)
        r_vals = arith_exp_values(r)

        for lv in l_vals:
            for rv in r_vals:
                vals += [lv+rv, lv-rv, lv*rv]
                if rv != 0:
                    vals.append(lv/rv)
        
    return list(set(vals))

def is_int(x):
    return abs(x - int(x)) <= 1/10**10

def only_pos_ints(L):
    return [x for x in L if is_int(x) and x >= 1]

def consecutives_from_one(L):
    L = sorted(only_pos_ints(L))

    if L == []:
        return 0

    i = 1
    for x in L:
        if x == i:
            i += 1
        else:
            return i-1

    return max(L)

def solution():
    best = 0

    for digits in combinations(range(10),4):
        digits = list(digits)
        
        res = consecutives_from_one(arith_exp_values(digits))

        if res > best:
            best = res
            bestdigs = digits

    return bestdigs

timeme(solution)