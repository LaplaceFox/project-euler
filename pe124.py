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

def genFromRad(pf, hi, output = False):
	fact = [[x,1] for x in pf]

	out = []

	# Special case for only one prime factor
	if len(fact) == 1:
		return floor(log(hi, fact[0][0]))

	smallest = fact[-1][0] # Smallest prime in factorization
	fact = fact[:-1] # The larger primes to increment individually

	ct = 0

	while True:
		unf = unfactor(fact)

		toAdd = floor(log(hi/unf, smallest))
		
		if output:
			out += [unf * smallest**i for i in range(1, toAdd + 1)]

		ct += toAdd

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
						return (ct,out) if output else ct # Done!

					fact[i][1] = 1 
					fact[i+1][1] += 1 # Increment immediately after first non-one exponent, then break
					break
				else:
					fact[i][1] = 1 # Reset


goal = 10000
seen = 1

radical = 2

while True:
	#print("radical=%s, seen=%s"%(radical,seen))

	if potentialRad(radical):
		new = genFromRad(pFacts(radical),100000)

		if seen+new < goal:
			seen += new
		else:
			idx = goal - seen
			print("Answer:", sorted(genFromRad(pFacts(radical),100000,True)[1])[idx-1])
			break
	
	radical += 1


print("Finished in", time()-start, "seconds.", chr(7))