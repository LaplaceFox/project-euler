from math import floor
from timeme import timeme

# k digits of 1/d starting from nth digit
def nth_digit(n,d,k):
    return floor(pow(10,n-1,d)*10**k/d)

def solution():
    acc = 0
    i = 1
    while 10**16 - 3**i > 0:
        # 12 digits found to allow for error accumulation (since less than 100 terms will be added)
        acc += nth_digit(10**16 - 3**i, 3**i, 12)
        i += 1

    # drop last 2 digits, then take the remaining final 10
    return (acc // 100) % 10**10

timeme(solution)