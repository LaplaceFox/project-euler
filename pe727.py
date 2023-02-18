from math import *
from itertools import combinations
from timeme import *

# Angle and two sides, find side opposite to angle
def loc_side(gamma,a,b):
    return sqrt(a**2 + b**2 - 2*a*b*cos(gamma))

# Three sides, find angle opposite to a
def loc_angle(a,b,c):
    return acos((b**2 + c**2 - a**2)/(2*b*c))

# Radius of circle externally tangent to circles of three given radii
def descartes(ra,rb,rc):
    ka, kb, kc = 1/ra, 1/rb, 1/rc
    ke = ka + kb + kc + 2*sqrt(ka*kb + ka*kc + kb*kc)
    return 1/ke

# Distance from incenter to center of circle externally tangent to circles of three given radii
def incenter_dist(ra,rb,rc):
    x, y, z = rb+rc, ra+rc, ra+rb

    # Angle A is 2*alpha, angle B is 2*beta
    alpha = loc_angle(x,y,z)/2
    beta =  loc_angle(y,x,z)/2

    re = descartes(ra,rb,rc)

    ABE = loc_angle(ra+re, z, rb+re)

    BD = z * sin(alpha) / sin(pi-alpha-beta)
    BE = rb + re
    DBE = abs(ABE - beta)

    return loc_side(DBE, BD, BE)

def gcd(a,b):
    if a > b:
        a, b = b, a

    # a <= b
    while a > 0:
        a, b = b%a, a

    return b

def gcd3(a,b,c):
    return gcd(gcd(a,b),c)

def solution():
    # All triples such that 1 <= ra < rb < rc <= 100
    triples = combinations(range(1,101), 3)
    
    # apply function where there's a collective gcd of 1
    triples = [incenter_dist(ra,rb,rc) for (ra,rb,rc) in triples if gcd3(ra,rb,rc) == 1]

    return sum(triples)/len(triples)

timeme(solution)