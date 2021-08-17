from functools import reduce
from math import sqrt

# Sum of proper divisors of n
def divisorSum(n):
	old_n = n
	total = 1

	assert(n > 0)

	k = 2
	while (n > 1):
		acc = 1

		if k > sqrt(n): # large prime factor
			total *= (n+1)
			break

		acc = 1

		while n % k == 0:
			n //= k
			acc = acc * k + 1 # sum of powers of k

		total *= acc
		k += 1

	return total - old_n

# deprecated

class Factorization:
	def __init__(self, n):
		assert(n > 0)

		self.n = n
		self.pfacts   = []
		self.pfcounts = []

		k = 2
		while (n > 1):

			if k > sqrt(n): # large prime factor
				self.pfacts.append(n)
				self.pfcounts.append(1)
				break

			ct = 0

			while n % k == 0:
				n //= k
				ct += 1

			if ct > 0:
				self.pfacts.append(k)
				self.pfcounts.append(ct)

			k += 1

	def unfactor(self, pfcounts):
		return reduce(lambda a,b: a*b, [self.pfacts[i]**pfcounts[i] for i in range(len(self.pfacts))],1)

	def getDivisorSum(self):
		divsum = 0
		powers = [0]*len(self.pfacts)

		while True:
			k = self.unfactor(powers)
			
			if self.n % k == 0:
				divsum += k
				powers[0] += 1
			else: # "rollover" the power list	
				for i in range(len(powers)): #zero out until we hit first nonzero
					if powers[i] > self.pfcounts[i]:
						powers[i] = 0
					else:
						powers[i] += 1
						break

			if max(powers) == 0: # overflow
				return divsum

	def getDivisors(self):
		divisorlist = []
		powers = [0]*len(self.pfacts)

		while True:
			k = self.unfactor(powers)
			
			if self.n % k == 0:
				divisorlist.append(k)
				powers[0] += 1
			else: # "rollover" the power list	
				for i in range(len(powers)): #zero out until we hit first nonzero
					if powers[i] > self.pfcounts[i]:
						powers[i] = 0
					else:
						powers[i] += 1
						break

			if max(powers) == 0: # overflow
				return sorted(divisorlist)