from timeme import *

def dijkstra(grid):
	width = len(grid[0])
	height = len(grid)

	# Coordinates of current location, then sum
	queue = [ ((0,0),grid[0][0]) ]

	# Dictionary mapping coordinate to best path total 
	# Init with "inf" for unreached coordinates
	best = {k:v for (k,v) in [((r,c),float('inf')) for r in range(height) for c in range(width)]}

	best[(0,0)] = grid[0][0]

	while queue != []:
		#input(queue)
		current = queue.pop(0)
		(r,c) = current[0] # Extract coordinates
		dist = current[1]  # Extract path length

		if dist > best[(r,c)]:
			continue # Not best, can be skipped

		nexts = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]

		for (nr,nc) in nexts:
			if 0 <= nc < width and 0 <= nr < height:
				# In range

				ndist = dist + grid[nr][nc]

				if ndist < best[(nr,nc)]:
					best[(nr,nc)] = ndist # Update distance
					queue.append(((nr,nc),ndist)) # Put back in queue
					queue.sort()
	
	return best[(height-1, width-1)]

test = [
[131, 673, 234, 103,  18],
[201,  96, 342, 965, 150],
[630, 803, 746, 422, 111],
[537, 699, 497, 121, 956],
[805, 732, 524,  37, 331]
]

test2 = [
[ 1,  1, 99,  1,  1,  1],
[99,  1, 99,  1, 99,  1],
[ 1,  1, 99,  1, 99,  1],
[ 1, 99, 99,  1,  1,  1],
[ 1, 99, 99,  1, 99,  1],
[ 1,  1,  1,  1, 99,  1]
]

def run():
	f = open("p083_matrix.txt")

	grid = [[int(x) for x in line.split(",")] for line in f.readlines()]
	print("Loaded grid.")

	return dijkstra(grid)

print(timeme(run))