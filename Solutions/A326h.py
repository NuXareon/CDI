# A326h : header for A326
# sxd 31/3/2014

'''
The functions 
     ells2ens(L)
     cartesian(X,C) 
     ells2code(L,r=2)
     make_code(N,r=2)
defined below were studied previously,
so no further comments will be added here
''' 
##
def ells2ens(L):
    return {l : L.count(l) for l in range(1,1+max(L))}
    
def cartesian(X,C):
    if not C:
        return sorted({str(x) for x in X})
    if not X:
        return sorted({str(c) for c in C})
    return sorted({str(x)+str(c) for x in X for c in C})


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
##


# Given a non-zero probability p, and an integer r ≥ 2,
# the function p2l(p,r) return the minimum integer l
# such that r**l ≥ 1/p. This is equivalent (v. T3) to 
#    l =  ⌈-log2(p)/log2(r)⌉ 
def p2l(p,r=2): 
    l=0; q=1/p
    while r**l<q:
        l += 1
    return l

# Given a probability distribution P and an integer r ≥ 2,
# the function make_code_list(P,r=2) constructs
# a list of code-words whose lengths are 
#     l_i =  ⌈-log2(p_i)/log2(r)⌉ 
# The length of any code-word in the list is
# never less than the length of the previous
# code-word in the list.

def make_code_list(P,r=2):
   L = [p2l(p,r) for p in P]
   C = ells2code(L,r)
   R = range(len(P))
   return [C[j][1] for j in R]

# Given an encoding table E whose elements have the form
#    j : (p,w)
# where j is a source symbol, p its probability and w
# the code-word, the function mean_len(E)
# yields the mean length of the code-words

def mean_len(E): return sum(E[j][0]*len(E[j][1]) for j in E)

# Auxiliary function to reverse a list.
def reverse(X): return [X[j] for j in range(len(X)-1,-1,-1)] 