from timeme import timeme

def numSoln(n):
	ct = 0
	x = n+1 #initial value

	while True:
		if x*n % (x-n) == 0:
			ct += 1
		if x*n / (x-n) < x:
			return ct
		x += 1

def run():
	n = 1

	while numSoln(n) < 1000:
		print(n, numSoln(n))
		n += 1

	return n

if __name__ == "__main__":
	timeme(run)