from time import time

start = time()

def step(x):
	if   x % 3 == 0:
		return ("D", x // 3)
	elif x % 3 == 1:
		return ("U", (4*x + 2) // 3)
	else:
		return ("d", (2*x - 1) // 3)

def multistep(x, steps):
	path = ""
	for i in range(steps):
		(char, newx) = step(x)
		x = newx
		path += char
	return path

def inv2(m):
	# Only defined for odd numbers
	return (m+1)//2

def inv4(m):
	# Only defined for odd numbers
	if m % 4 == 3:
		return (m + 1) // 4
	else:
		return (3*m + 1) // 4

def revstep(x,s,m):
	# s is the goal number mod 3
	# m is the modulus
	d = {
		0 : 3*x,
		1 :	((3*x-2) * inv4(m)),
		2 : ((3*x+1) * inv2(m))
	}
	return d[s] % m

seq = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"

def revseq(seq):
	symb = {"D":0, "U":1, "d":2}

	modulus = 3
	acc = symb[seq[-1]]

	for char in seq[::-1][1:]:
		modulus *= 3
		acc = revstep(acc,symb[char],modulus)
	return (acc,modulus)

bound = 10**15

(acc,modulus) = revseq(seq)

mult = bound//modulus * modulus

print(mult+acc if mult+acc > 10**15 else mult+modulus+acc)

print("Finished in", time()-start, "seconds.", chr(7))