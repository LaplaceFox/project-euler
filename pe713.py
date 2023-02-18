from timeme import timeme

def T(N,m):
    if 2*m > N and m > 2:
        return N-m+1
    
    k = m-1
    q = N//k
    r = N % k

    return k * q * (q-1) // 2 + q * r

def solution():
    N = 10**7
    return sum([T(N,m) for m in range(2,N+1)])

timeme(solution)