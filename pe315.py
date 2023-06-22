from primes import megasieve
from mylib import digitSum
from timeme import timeme

digit_seg = {
    0: 0b1110111,
    1: 0b0010010,
    2: 0b1011101,
    3: 0b1011011,
    4: 0b0111010,
    5: 0b1101011,
    6: 0b1101111,
    7: 0b1110010,
    8: 0b1111111,
    9: 0b1111011
}

# Number of segments on for both digits d1 and d2
def shared_segs(d1,d2):
    # Bitwise AND, then count the 1s
    return "{:b}".format(digit_seg[d1] & digit_seg[d2]).count("1")

def saved_transitions(a,b):
    digitsA = [int(c) for c in str(a)]
    digitsB = [int(c) for c in str(b)]

    numShared = min(len(digitsA),len(digitsB))

    res = 0

    for i in range(1,numShared+1):
        # Read from the end so we only get shared digits
        res += 2 * shared_segs(digitsA[-i],digitsB[-i])
    
    return res

def total_saved(n):
    res = 0
    while n >= 10:
        res += saved_transitions(n, digitSum(n))
        n = digitSum(n)
    
    return res

def solution():
    used_primes = [p for p in megasieve(2*10**7) if p > 10**7]
    
    res = 0
    for p in used_primes:
        res += total_saved(p)

    return res

timeme(solution)