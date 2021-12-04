from timeme import timeme

def hasSquareSum(t):
	lo = 1
	hi = 2
	tot = 5 #1^2  + 2^2

	while lo != hi:
		if tot == t:
			return True
		elif tot < t:
			hi += 1
			tot += hi**2
		else:
			tot -= lo**2
			lo += 1
	return False

def run():
	tot = 0

	for i in range(1,10000): #all 4-digit numbers:
		n1 = int(str(i) + str(i)[::-1])
		n2 = int(str(i)[:-1] + str(i)[::-1])

		if hasSquareSum(n1):
			tot += n1
		if hasSquareSum(n2):
			tot += n2

	return tot

if __name__ == "__main__":
	timeme(run)