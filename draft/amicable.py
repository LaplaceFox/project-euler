from math import sqrt

# Sum of proper factors of n
def factorSum(n):
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