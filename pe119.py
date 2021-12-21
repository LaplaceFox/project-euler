from timeme import timeme

def digitSum(n):
	tot = 0
	while n >= 10:
		tot += n % 10
		n //= 10
	return tot + n

def isPowerOf(n,k):
	# Is n a power of k?
	pw = 1

	if k in [0,1]:
		return n == k

	while pw <= n:
		if pw == n:
			return True
		pw *= k
	return False

def smallestWithDS(n):
	# Return smallest integer with digit sum n
	if n < 10:
		return 9 + n
	else:
		dv = n // 9 # number of 9s to put at the end
		md = n % 9  # number to put at the front

		return md * (10**dv) + 10**dv - 1


def run():
	found = []
	
	k = 2 # Power to test
	while True:
		n = 2 # Digit sum to test
		while True:
			if n > 9 and n**k < smallestWithDS(n):
				break

			if digitSum(n**k) == n:
				found.append(n**k)
				#print(f"Found {n}^{k} = {n**k}")

				if len(list(filter(lambda x: x < 2**k, found))) >= 30: # If we found 30 that are smaller than any possible future result:
					return sorted(found)[29] # Return the 30th thing

			n += 1

		k += 1

if __name__ == "__main__":
	timeme(run)