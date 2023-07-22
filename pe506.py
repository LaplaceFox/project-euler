from mylib import digitSum
from pe700 import invEuclid
from timeme import timeme

def clock():
    while True:
        for c in "123432":
            yield int(c)

def clock_substrings():
    c = clock()
    i = 1
    while True:
        ss = 0
        while digitSum(ss) < i:
            ss = ss * 10 + next(c)

        yield ss
        i += 1

def test(n):
    return 1234320 * sum([10**(6*i) for i in range(n)]) + 1

# Sum b^0 to b^n mod m
def power_sum_mod(b,n,m):
    return ((pow(b,n+1,m)-1) * invEuclid(m, b-1)) % m

def testsum(n):
    c = clock_substrings()
    return sum([next(c) for i in range(n)]) % 123454321

# ACTUAL SOLUTION

# Sum up to xth term with index with given residue mod 15
def termsum(x,residue):
    transients = [0,1,2,3,4,32,123,43,2123,432,1234,32123,43212,34321,23432]
    
    # Determine repeating segments
    repeat = [123432, 123432]
    for i in range(1,len(transients)-1):
        k = len(str(transients[i])) # Transient length
        last_rep = str(repeat[-1])
        repeat.append(int(last_rep[k:] + last_rep[:k])) # Cycle characters around

    return termsum_helper(repeat[residue], transients[residue], x)

def termsum_helper(rep,trans,x):
    m = 123454321

    if trans == 0:
        k = 0
    else:
        k = len(str(trans))
    d = invEuclid(m,999999)

    return (pow(10,k,m)*d*d*rep*(pow(10,6*(x+1),m)-1) + (x+1)*(-pow(10,k,m)*d*rep + trans)) % m

def solution():
    res = 0
    for i in range(15):
        res += termsum((10**14 - i)//15, i)
    return res % 123454321

timeme(solution)