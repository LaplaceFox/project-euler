# Commonly used functions

def digitSum(n):
	tot = 0
	while n > 10:
		tot += n % 10
		n //= 10
	return tot + n