from timeme import timeme

def testPerm(s):
	# Test permutation string of digits for product

	found = []

	asz = 1

	while asz <= 3:
		bsz = asz  # b is at least as big as a

		a = int(s[:asz])
		b = int(s[asz:asz+bsz])
		c = int(s[asz+bsz:])

		while a * b <= c:
			if a * b == c:
				found.append(c)

			bsz += 1

			a = int(s[:asz])
			b = int(s[asz:asz+bsz])
			c = int(s[asz+bsz:])

		asz += 1

	return found

def allPerms(s):
	if len(s) == 1:
		return [s]

	perms = []

	for i in range(len(s)):
		newstr = s[:i] + s[i+1:]

		perms.extend(map(lambda x: s[i]+x, allPerms(newstr)))

	return perms

def run():
	found = []

	L = allPerms("123456789")

	for p in L:
		for x in testPerm(p):
			if x not in found:
				found.append(x)

	return sum(found)

if __name__ == "__main__":
	timeme(run)