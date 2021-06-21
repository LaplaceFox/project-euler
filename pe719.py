from time import time

def splitsum(n, tgt):
    #print((n,tgt))
    if n == tgt:
        return True

    # But otherwise, if we're out of digits...
    if n == 0:
        return False

    for i in range(1,len(str(n))):
        left = int(str(n)[:i])
        right = int(str(n)[i:])

        #print("Split:", (left,right))
        #input()

        if left > tgt: # Already got too big
            return False

        if right < tgt-left:
            return False

        if splitsum(right, tgt-left):
            return True

    return False

begin = time()

total = 0

for i in range(2,10**6 + 1):
    if i % 10000 == 0:
        print("->" + str(i//10000))

    if splitsum(i**2, i):
        #print(True)
        total += i**2

    #print("------")

print(total)
print("Time taken:", time()-begin, chr(7))