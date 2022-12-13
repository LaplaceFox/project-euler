from mylib import digitSum

def dRoot(n):
	while n >= 10:
		n = digitSum(n)
	return n

def dRootSum(n):
	tot = 0
	for i in range(n+1):
		tot += dRoot(i)
	return tot

def dRootSumFast(n):
	return 45*(n//9) + sum(range((n%9+1)))