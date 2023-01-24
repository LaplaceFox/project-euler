from copy import *

def from_profile(profile):
    if profile == len(profile)*[0]:
        return [[]]
    
    res = []
    for i in range(len(profile)):
        if profile[i] > 0:
            new_profile = copy(profile)
            new_profile[i] -= 1

            res += [[i] + L for L in from_profile(new_profile)]
    
    return res

def sum_of_profile(P):
    return sum([i * P[i] for i in range(len(P))])

def valid_perms(profile):
    perms = from_profile(profile)
    return [P for P in perms if sum_of_profile(P) in [23, 34, 45, 56, 67]]

memo = {0:1}

def fact(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = n * fact(n-1)
        return n * fact(n-1)

def profile_perms(profile):
    res = fact(sum(profile))

    for x in profile:
        res //= fact(x)
    
    return res

def solution():
    valids = []
    for i in range(6):
        profile = [i, 10-2*i, i]
        valids += valid_perms(profile)

    # Don't care about the sums anymore, since a profile of one half induces its pair!
    tot = 0

    for v in valids:
        fewer_zero = copy(v)
        invalid = 0 # Number of arrangements with a leading zero we have to rule out

        # If a zero is one of the digits, make sure we can't put it first
        if fewer_zero[0] > 0:
            fewer_zero[0] -= 1
            invalid = profile_perms(fewer_zero)

        perms = profile_perms(v)
        tot += perms * (perms - invalid)
    return tot