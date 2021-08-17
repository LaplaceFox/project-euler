from timeme import timeme
from factors import *

def run():
	ds = divisorSum # alias

	bestlen = 1
	bestmin = 0

	found = set([1])

	for i in range(2,10**6):
		if i in found:
			continue

		chain = [i]

		while True:
			i = ds(i)

			if i in chain:
				size = len(chain) - chain.index(i)
				minimum = min(chain[chain.index(i):])

				if size > bestlen:
					bestlen = size
					bestmin = minimum

				chain.append("...")
				break

			if i > 10**6:
				chain.append("OVERFLOW")
				break

			chain.append(i)

			if i in found:
				break

		# print current chain
		#print(" -> ".join(map(str,chain)))

		found |= set(chain)

	return bestmin

timeme(run)