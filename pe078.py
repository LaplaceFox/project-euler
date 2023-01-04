from timeme import timeme

def penta_low(k):
    return k * (3*k - 1) / 2

def penta_high(k):
    return k * (3*k + 1) / 2

memo = {0:1}

def partition(n):
    if n < 0:
        return 0

    if n in memo:
        return memo[n]

    result = 0

    k = 1

    while True:
        a = penta_low(k)
        b = penta_high(k)
        
        if n-a < 0:
            break

        sign = (-1)**(k%2 + 1)

        result += sign * (partition(n-a) + partition(n-b))

        k += 1
    
    memo[n] = result
    return result

def run():
    n = 1

    while True:
        if partition(n) % 1000000 == 0:
            return n
        n += 1

timeme(run)