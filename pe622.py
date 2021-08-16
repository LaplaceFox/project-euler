from factors import *

total = 0

divisors = Factorization(2**60-1).getDivisors()

divisors.remove(1) # degenerate case

for d in divisors:
	if 2**12 % d != 1 and 2**20 % d != 1 and 2**30 % d != 1:
		total += d+1

print(total)