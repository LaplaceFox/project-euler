from timeme import *
from math import sqrt

dbg = True

def slow_pfactsum(n):
	acc = 0 # Total of the factors we pull out
	k = 2

	while n > 1 and k <= sqrt(n):
		while n % k == 0:
			acc += k
			n //= k
		k += 1

	if n > 1:
		# Alternate break condition, where n has a large prime factor
		acc += n

	return acc

def run():
	pass

timeme(run)