from functools import reduce
from time import time
from math import log, floor

start = time()

def pFacts(n):
	k = 2
	factored = []

	while n > 1:
		ct = 0
		while n % k == 0:
			n //= k
			ct += 1

		if ct > 0:
			factored.append(k)
		k += 1
	return factored[::-1]

def rad(n):
	return reduce(lambda a,b: a*b, pFacts(n))

def potentialRad(n):
	return rad(n) == n

def unfactor(fact):
	# [(5,2), (3,1), (2,2)] -> 5**2 * 3 * 2**2
	return reduce(lambda a,b: a*b, [x[0]**x[1] for x in fact])

def genFromRad(pf, hi):
	fact = [[x,1] for x in pf]

	# Special case for only one prime factor
	if len(fact) == 1:
		return floor(log(hi, fact[0][0]))

	smallest = fact[-1][0] # Smallest prime in factorization
	fact = fact[:-1] # The larger primes to increment individually

	ct = 0

	while True:
		ct += floor(log(hi/unfactor(fact), smallest))

		#print(fact)
		#print("Added", floor(log(hi/unfactor(fact), smallest)))
		#input()

		# "Increment" the factorization
		fact[0][1] += 1

		# Check if bound exceeded
		while unfactor(fact) > hi:
			# "Carry"
			for i in range(len(fact)):
				if fact[i][1] > 1:
					if i+1 >= len(fact):
						return ct # Done!

					fact[i][1] = 1 
					fact[i+1][1] += 1 # Increment immediately after first non-one exponent, then break
					done = True
					break
				else:
					fact[i][1] = 1 # Reset




#print("Finished in", time()-start, "seconds.", chr(7))