from time import time

start = time()

big = 100_000_000
base = 1777

def modcheck():
	acc = base
	exp = 1
	lowest = big
	low_exp = 0

	for i in range(10_000_000):
		exp += 1
		acc = (acc * base) % big

		if acc < lowest and exp >= 3:
			low_exp = exp
			lowest = acc
			print("Exp:", exp, "Rem:", acc)

def bigpow(b,e):
	pattern = "{0:b}".format(e)
	acc = 1

	for char in pattern:
		acc *= acc
		acc %= modulus**2
		if char == '1':
			acc *= b
	return acc

# We can cheat by doing exponents mod 1_250_000... cool!

modulus = big

acc = 1777

for i in range(1855):
	print("acc is", acc)
	input()
	acc = bigpow(base, acc) % modulus

print(acc % big)

print("Finished in", time()-start, "seconds.", chr(7))