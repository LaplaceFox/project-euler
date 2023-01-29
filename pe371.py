from timeme import *

def solution():
    memo = {}

    # Base cases
    memo[(998,True)]  = 1000/999
    memo[(998,False)] = 1000/999 + (1/999)*memo[(998,True)]

    for w in range(997,-1,-1):
        memo[(w,True)]  = 1000/(1000-w-1) + (1/(1000-w-1))*(max(0, 998-2*w)*memo[(w+1,True)])
        memo[(w,False)] = 1000/(1000-w-1) + (1/(1000-w-1))*(max(0, 998-2*w)*memo[(w+1,False)] + memo[(w,True)])

    return memo[(0,False)]

timeme(solution)