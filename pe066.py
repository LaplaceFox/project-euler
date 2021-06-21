from math import sqrt

def isSquare(n):
    return round(sqrt(n))**2 == n

bestD = 0
bestx = 0

for D in range(1001):
    if not isSquare(D):
        y = 1
        while True:
            xsq = D*(y**2) + 1

            if isSquare(xsq):
                x = round(sqrt(xsq))

                print("%i^2 - %i*%i^2 = 1"%(x, D, y))

                if x > bestx:
                    bestx = x
                    bestD = D

                break
            y += 1
print(bestD)
