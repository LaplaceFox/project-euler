from timeme import timeme

def splitsum(n, tgt):
    if n < tgt:
        return False

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
            continue

        if splitsum(right, tgt-left):
            return True

    return False

def solution():
    total = 0

    for i in range(2,10**6 + 1):
        if i % 10000 == 0:
            print("->" + str(i//10000))

        # Idea from forum: number splitting preserves digit sum, so if a number
        # is an S-number, x = x^2 must be true mod 9 (so x is 0 or 1 mod 9)
        if i % 9 in [0,1] and splitsum(i**2, i):
            #print(True)
            total += i**2

        #print("------")
    return total

timeme(solution)