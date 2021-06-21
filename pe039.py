from math import sqrt
bestcount = 0

for p in range(2,1000,2): # Must be even
    count = 0
    for a in range(1,p//4+1): # Bounded by p/4
        k = p - a
        if (p**2 // 2) % k == 0:
            a = p - k
            b = p - (p**2/(2*k))
            count += 1
    if count > bestcount:
        bestcount = count
        bestp = p

print("Best P:", bestp)
print("with", bestcount, "triples")
