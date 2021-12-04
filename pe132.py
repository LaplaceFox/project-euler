from primes import nextPrime
from timeme import timeme
from math import floor

def bigpowmod(b,e,m):
	acc = 1

	while e > 0:
		if e % 2 == 1:
			acc = (acc * b) % m

		b = b**2 % m
		e = floor(e/2)

	return acc


def run():
	ct = 0
	tot = 0
	p = 7

	while ct < 40:
		if bigpowmod(10,10**9,p) == 1:
			tot += p
			ct += 1
			print("Found", p)
		p = nextPrime(p)

	return tot

if __name__ == "__main__":
	timeme(run)