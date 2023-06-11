from math import sqrt
from timeme import timeme

def isValid(b,t):
    if t != round(t): # t is not an integer
        return False
    
    t = int(t)

    return t**2 - t == 2*(b**2 - b)

def solution():
    b = 707106781187 # Starting test value for blue disks

    while True: # Keep looking for valid number of blue disks
        t = (1 + sqrt(1 + 8*(b**2-b))) / 2

        print(b, t, (t**2-t)/(b**2-b))
        input()

        if isValid(b,t):
            print(b, int(t))
            return b
        
        b += 1

timeme(solution)