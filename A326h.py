# A326h : header for A326

# Define a function that constructs, given r and a feasible list
# of lengths, a prefix encoding with those lengths

def ells2code(L,r=2): 
    return( make_code( list(ells2ens(L).values()), r ) )

def make_code(N,r=2):
    n = sum(N)
    l = len(N)
    A = range(n)
    C = range(r) 
    T = []
    X = [] # to hold the current Code_(j-1)
    Y = [] # words eligible for construction Code_j
    sj = 0
    for j in range(l):
        nj = N[j]
        if nj == 0:
            Y = cartesian(Y,C)
            continue
        Y = cartesian(Y,C)
        X = Y[:nj]
        Y = list(set(Y) - set(X))
        T += [(i,X[i-sj]) for i in range(sj,sj+nj)]
        sj += nj
    return T

def p2l(p,r=2):
    l=0; q=1/p
    while r**l<q:
        l += 1
    return l

def make_code_list(P,r=2):
   L = [p2l(p,r) for p in P]
   C = ells2code(L,r)
   R = range(len(P))
   return [C[j][1] for j in R]


def reverse(X): return [X[j] for j in range(len(X)-1,-1,-1)] 