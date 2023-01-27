from timeme import timeme

# When `a` is even, best remainder is a*(a-2)
# When `a` is odd, best remainder is a*(a-1)
def solution():
    return sum([a*(a-(2-a%2)) for a in range(3,1001)])

timeme(solution)