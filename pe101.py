from timeme import timeme

def polynomial_mult(P,Q):
    R = [0]*(len(P)+len(Q)-1)

    for a in range(len(P)):
        for b in range(len(Q)):
            R[a+b] += P[a]*Q[b]

    return R

def polynomial_eval(P,x):
    acc = 0
    for i in range(len(P)):
        acc += P[i] * x**i
    return acc

# Lagrange basis for nodes X, value 1 for x=X_n
def lagrange_basis(X,n):
    basis = [1]

    for i in range(len(X)):
        if i != n:
            basis = polynomial_mult(basis,[-1*X[i],1])
            basis = polynomial_mult(basis,[1/(X[n]-X[i])])

    return basis

# Lagrange interpolation of (x,y)
def lagrange_inter(X,Y):
    assert(len(X) == len(Y))
    
    n = len(X)
    inter = [0]*n

    for i in range(n):
        basis = lagrange_basis(X,i)
        for j in range(n):
            inter[j] += Y[i]*basis[j]
    
    return inter

def solution():
    gen_poly = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]

    n = len(gen_poly)

    terms = [polynomial_eval(gen_poly,x) for x in range(1,n+1)]

    print(terms)
    
    total = 0

    for i in range(1,n):
        # find BOP
        bop = lagrange_inter(range(1,i+1),terms[:i])

        bop = [round(x) for x in bop]

        print("BOP", i, bop)

        bop_terms = [round(polynomial_eval(bop,x)) for x in range(1,n+1)]

        print("BOP terms", bop_terms)
    
        print("FIT is", bop_terms[i])
        total += bop_terms[i]
    
    return total

timeme(solution)