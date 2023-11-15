from primes import megasieve
from timeme import timeme

class FactorizationGen:
    def __init__(self,n):
        self.n = n
        self.primes = megasieve(n)
        self.exps = [0]

    def __iter__(self):
        return self

    def __eval_factorization(self):
        acc = 1
        for i in range(len(self.exps)):
            acc *= self.primes[i]**self.exps[i]
        return acc
    
    def __increase(self):
        self.exps[0] += 1

    def __rollover(self):
        i = 0
        while self.exps[i] == 0:
            i += 1
        # i is now index of first nonzero exponent
        self.exps[i] = 0

        if i+1 >= len(self.exps):
            self.exps.append(1)
        else:
            self.exps[i+1] += 1 # could be out of bounds, but should never actually happen
    
    def __next__(self):
        if len(self.exps) > len(self.primes):
            raise StopIteration

        res = (self.__eval_factorization(), [self.primes[i]**self.exps[i] for i in range(len(self.exps))])

        self.__increase()
        
        while self.__eval_factorization() > self.n:
                self.__rollover()

                if len(self.exps) > len(self.primes):
                    return res
        return res


def naive_idempotents(n):
    return max([a for a in range(n) if (a**2 - a)%n == 0])

def naive_solution(n):
    acc = 0
    for i in range(1, n+1):
        acc += naive_idempotents(i)

    return acc

def inv_euclid(a,b):
    modulus = a
    # a > b

    coeff = []

    while b > 0:
        coeff.append(a // b)
        a, b = b, a%b

    # Now inverse

    m, n = (0,1)

    # Skip last coefficient
    for c in coeff[:-1]:
        m, n = n, m - c*n

    return n % modulus

# Assume all moduli are pairwise coprime
# Every residue is 1
def chinese_remainder_terms(moduli):
    N = 1
    for ni in moduli:
        N *= ni

    terms = []

    for i in range(len(moduli)):
        ni = moduli[i]
        m = N // ni
        inv = inv_euclid(ni, m)

        terms.append(m * inv)
    
    return terms

def all_subset_sums(L):
    if L == []:
        return [0]
    else:
        subcase = all_subset_sums(L[1:])
        return subcase + [L[0] + x for x in subcase]
    
# `factorization` is prime power factorization of n
def idempotents(n, factorization):
    factorization = [f for f in factorization if f != 1]
    res = all_subset_sums(chinese_remainder_terms(factorization))
    return sorted([x % n for x in res])

def solution(n):
    gen = FactorizationGen(n)

    acc = 0

    for (x,facts) in gen:
        if x in gen.primes and x*2 > n:
            break

        #print(x,facts)
        acc += max(idempotents(x,facts))
    
    acc += len([p for p in gen.primes if p >= x])

    return acc

timeme(lambda: solution(10**3))
timeme(lambda: solution(10**4))
timeme(lambda: solution(10**5))
timeme(lambda: solution(10**6))
timeme(lambda: solution(10**7))