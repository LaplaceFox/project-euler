from timeme import *
from math import sqrt
from primes import megasieve as sieve

dbg = True

def run():

	pfs = sieve(20_000_000)

	dprint("Primes sieved.")

	def pfactsum_range_factorial(n):
		# Prime factor sum of n!
		acc = 0

		for pf in pfs:
			if pf > n:
				break

			ppow = pf # Prime power
			while ppow <= n:
				acc += n // ppow * pf
				ppow *= pf

		return acc

	prf = pfactsum_range_factorial #alias

	return prf(20_000_000) - prf(15_000_000) - prf(5_000_000)

timeme(run)