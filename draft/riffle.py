from copy import copy

def riffle(L):
	return L[::2] + L[1::2]

def riffCycle(L):
	original = copy(L)

	ct = 1
	L = riffle(L)
	print(L)

	while L != original:
		ct += 1
		L = riffle(L)
		print(L)

	return ct