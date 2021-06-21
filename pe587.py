from math import sqrt, asin, pi

# Gross inside part of the integral
def mess(x):
    return 1/4 * (-2*x *sqrt(x-x**2) + sqrt(x-x**2) + 2*x + asin(sqrt(1-x)))

# Area of curvy part given left bound
def area(a):
    return mess(1/2) - mess(a)

# Left bound of the integral, given number of circles
def bound(n):
    return n*(n+1-sqrt(2*n))/(2*n**2+2)

# Area of the triangle part, given n
def triangle(n):
    ystar = (n+1-sqrt(2*n))/(2*n**2+2)
    return n*ystar**2 / 2

# Area of curvy part, given n
def curvy(n):
    return area(bound(n))

# Fraction of total corner area
def ratio(n):
    entire = 1/4 - pi/16
    partial = triangle(n) + curvy(n)
    return partial/entire