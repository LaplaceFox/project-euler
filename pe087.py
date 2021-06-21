from primes import sieve
from math import sqrt, ceil
from time import time

start = time()

big = 50_000_000

ps = sieve(ceil(sqrt(big)+1))

squares = [p**2 for p in ps if p**2 <= big]
cubes   = [p**3 for p in ps if p**3 <= big]
fourth  = [p**4 for p in ps if p**4 <= big]

sums = [s + c + f for s in squares for c in cubes for f in fourth if s + c + f <= big]

print(len(set(sums)))

print("Finished in", time()-start, "seconds.", chr(7))