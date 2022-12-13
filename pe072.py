from factors import totient
from timeme import timeme

def run():
	total = 0
	for i in range(2,10**6+1):
		#print(f"{i} has totient {totient(i)}")
		total += totient(i)

	return total


if __name__=="__main__":
	timeme(run)