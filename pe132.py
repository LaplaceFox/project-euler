from primes import nextPrime
from timeme import timeme

def repu(k):
	# Return repunit of length k (for testing)
	return int("1" * k)

def repuRes(k,d):
	# Residue of repunit length k divided by d

	if 10 % d == 0:
		return 1

	resloop = [1]
	cur = 1

	while True:
		# Get residue of next place value
		cur = (cur * 10) % d

		if cur == 1: #if already looped
			break
		else:
			resloop.append(cur)

	looplen = len(resloop)

	# Total for all repeated loops
	loops_sum = sum(resloop) * (k // looplen)

	# Get sum of residues in partial loop at high end of repunit
	part_sum = sum(resloop[:(k % looplen)]) % d

	return (part_sum + loops_sum) % d

def run(size,count):
	p = 2 #current prime
	ct = 0 #prime divisors found
	tot = 0 #total of divisors

	while ct < count:
		if repuRes(size, p) == 0:
			ct += 1
			tot += p
			print("Found", p)
		p = nextPrime(p)

	return tot


if __name__ == "__main__":
	def test():
		return run(10**9, 40)

	timeme(test)