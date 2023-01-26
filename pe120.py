from timeme import timeme

def solution():
    tot = 0

    for a in range(3,1001):
        rems = [2 if n%2 == 0 else (2*n*a)%(a**2) for n in range(2*a)]
        tot += max(rems)
    return tot

timeme(solution)