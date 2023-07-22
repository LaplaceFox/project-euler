from copy import deepcopy as copy
import numpy
from timeme import timeme

def matrix_mod(M,md):
    M = copy(M)
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] %= md
    return M

def matrix_power_mod(M,e,md):
    M = copy(M)
    acc = numpy.eye(len(M),dtype=int)

    while e > 0:
        if e % 2 == 0:
            M = matrix_mod(numpy.matmul(M,M),md)
            e //= 2
        else:
            acc = matrix_mod(numpy.matmul(acc,M),md)
            e -= 1
    return acc

def solution():
    modulus = 10**9

    M = numpy.array(
        [[1, 6, 0, 0, 0, 0],
         [1, 1, 5, 0, 0, 0],
         [1, 1, 1, 4, 0, 0],
         [1, 1, 1, 1, 3, 0],
         [1, 1, 1, 1, 1, 2],
         [1, 1, 1, 1, 1, 1]])
    
    bigpow = matrix_power_mod(M,10**12-1,modulus)

    print(bigpow)

    start = numpy.array([[7,0,0,0,0,0]])
    vsum = numpy.array([[1]]*6)

    return matrix_mod(numpy.matmul(numpy.matmul(start,bigpow),vsum),modulus)

timeme(solution)