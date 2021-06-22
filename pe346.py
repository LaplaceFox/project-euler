from timeme import *

def run():
	bound = 10**12

	# Set of integers that can be represented as a repunit length 3 or greater
	reps = set()

	b = 2 # Starting base

	while True:
		# Start as 111 in given base
		repunit = b**2 + b + 1

		if repunit > bound:
			# No other representation possible
			break

		size = 3

		while repunit < bound:
			dprint("1"*size + " in base" + str(b) + " is " + str(repunit))
			dinput()

			reps.add(repunit)
			repunit = repunit*b + 1
			size += 1

		b += 1		

	return sum(list(reps)) + 1

timeme(run)