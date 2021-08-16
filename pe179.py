from time import time
from math import sqrt

def divCount(n):
	# Count # of divisors
	numDiv = 1
	k = 2
	while n > 1:
		if k > sqrt(n):
			return numDiv * 2 #last prime factor
		ct = 0
		while n % k == 0:
			n //= k
			ct += 1
		if ct > 0:
			numDiv *= (ct+1)
		k += 1
	return numDiv

start = time()

for i in range(2,10**7):
	divCount(i)

print("Finished in", time()-start, "seconds.", chr(7))