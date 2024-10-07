from math import floor

def digitSum(n):
	tot = 0
	while n >= 10:
		tot += n % 10
		n //= 10
	return tot + n

# b**e % m, but faster
def bigpowmod(b,e,m):
	acc = 1

	while e > 0:
		if e % 2 == 1:
			acc = (acc * b) % m

		b = b**2 % m
		e = floor(e/2)

	return acc