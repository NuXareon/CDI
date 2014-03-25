# L325x: kick off for L325
# construction of prefix r-ary codes with given lengths

# import header
pypath = 'D:/Docencia/2014/py'
import sys
sys.path.append(pypath)
from L325h import *
    
# Define a function that constructs, given r and a feasible list
# of lengths, a prefix encoding with those lengths

def ells2code(L,r=2): 
    return( make_code( list(ells2ens(L).values()), r ) )

def make_code(N,r=2):
    n = sum(N)
    l = len(N)
    A = range(n)
    C = range(r)
    T = dict()
    X = [] # Current code_(j-1)
    Y = [] # Words eligible on code_j
    sj = 0
    for j in range(l):
        nj = N[j]
        if nj == 0:
            Y = cartesian(Y,C)
            continue
        Y = cartesian(Y,C)
        X = Y[:nj]
        Y = list(set(Y) - set(X))
        T.update({i:X[i-sj] for i in range(sj,sj+nj)})
        sj += nj
    return T


print(ells2code([1,2,3,4,4]))

print(ells2code([2,2,2,3,3]))

L = [1,1,1,1,2,2,2,3,3,4]
print(ells2code(L,5))
