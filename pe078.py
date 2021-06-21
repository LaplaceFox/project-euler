memo = {}

def partition(n,k):
    if (n,k) in memo:
        return memo[(n,k)]

    # Number of partitions of n object with max group size k
    if n <= 1:
        return 1
    if k == 1:
        return 1
    else:
        # Sum F(n-i, i) from 1 to k
        result = sum([partition(n-i,min(n-i,i)) for i in range(1,k+1)]) % 1000000
        memo[(n,k)] = result
        return result

# Key n is sum of part(1,1) + ... + part(n,n)
partitionsums = {0:1}

def run():
    n = 1
    while True:
        result = partitionsums[n//2] + sum([partition(n-i,i) for i in range(1, (n-1)//2 + 1)])
        partitionsums[n] = (result + partitionsums[n-1]) % 1000000
        #input()

        result %= 1000000

        print("(%i,%i): %i"%(n,n,result))
        if result == 0:
            print(n)
            print(chr(7))
            break
        n += 1
