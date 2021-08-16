from timeme import timeme
from factors import *

def test():	
	for i in range(2,10**5):
		x = Factorization(i).getDivisorSum()

timeme(test)

# This is going to be too slow. We need to be more clever with how we find divisors.