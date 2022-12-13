from timeme import timeme
from math import ceil

fibdict = {1:1, 2:1}

def fib(n):
	if n <= 2:
		return 1

	if n not in fibdict.keys():
		fibdict[n] = fib(n-1) + fib(n-2)
	return fibdict[n]


def fibWordLookup(k,i):
	# Look up kth character (1-indexed) of ith Fibonacci word
	if i <= 2:
		return i # Return whether the character is A (1) or B (2)

	if k <= fib(i-2):
		return fibWordLookup(k,i-2)
	else:
		return fibWordLookup(k-fib(i-2),i-1)

def dthDigit(n):
	a = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
	b = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"

	#a = "1415926535"
	#b = "8979323846"

	k = len(a)
	assert(k == len(b)) # Lengths must be the same

	rem = (n-1) % k # digit to look up in strings A or B
	n = (n-1) // k + 1

	i = 1
	while fib(i) < n:
		i += 1

	res = fibWordLookup(n,i)

	if res == 1:
		return a[rem]
	else:
		return b[rem]

def run():
	result = ""
	for i in range(18): # 0 up to 17
		result += dthDigit((127+19*i) * 7**i)

	return result[::-1] # Found digits in reverse order

if __name__ == "__main__":
	timeme(run)