from time import time

GOAL_SIZE = 5

def digitSort(n):
	return "".join(sorted(list(str(n))))

def run():
	n = 1
	resultLen = 1

	memo = {}

	while True:
		
		cube = n**3
		
		if len(str(cube)) > resultLen:
			# Check for goal condition
			for perm in memo:
				if len(memo[perm]) == GOAL_SIZE:
					return min(memo[perm])**3

			# Rolled over into new number size, reset memo table
			memo = {}
			resultLen = len(str(cube))

		perm = digitSort(cube)

		if perm not in memo:
			memo[perm] = [n]
		else:
			memo[perm] += [n]

		#input()
		#print(memo)

		n += 1

start = time()

print(run())

print("Finished in", time()-start, "seconds.")