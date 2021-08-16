def looksay(s):
	concat = lambda l: "".join(l)

	# Digit string as input

	# Put dashes between differing characters
	s = concat([s[i] + "-" * (s[i] != s[i+1]) for i in range(len(s)-1)]) + s[-1]

	# For each block, count the length and what character is used
	return concat([str(len(x)) + x[0] for x in s.split("-")])


def iterate(s):
	while(True):
		print(s)

		if input() == "q":
			return 

		s = looksay(s)