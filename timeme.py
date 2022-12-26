from time import time

dbg = False

def dinput():
	if dbg:
		input()

def dprint(x):
	if dbg:
		print(x)

def timeme(fn):
	start = time()

	result = fn()
	print(result)

	print("Finished in", time()-start, "seconds.", chr(7))

	return result