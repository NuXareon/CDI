## A430h : header file for A430
import numpy as np
import matplotlib.pyplot as plt

# Basic constants
r2 = np.sqrt(2)
a1=a2 = 1/r2
nd = 4

# Synonyms
Id = np.eye
array = np.array
stack = np.vstack
splice= np.hstack
plot  = plt.plot
show  = plt.show()
dot = np.dot
ls  = np.linspace
zeros=np.zeros



# To construct the array of level r scaling vectors
# from the array V of level r-1 scaling vectors
def HaarV(V):
    N = len(V)
    X = a1*V[0,:] + a2*V[1,:]
    for j in range(1, N//2):
        x = a1 * V[2*j,:] + a2 * V[2*j+1,:]
        X = stack([X,x])
    return X

# To construct the array of level r wavelet vectors
# from the array V of level r-1 scaling vectors
def HaarW(V):
    N = len(V)
    X = a1*V[0,:] - a2*V[1,:]
    for j in range(1, N//2):
        x = a1 * V[2*j,:] - a2 * V[2*j+1,:]
        X = stack([X,x])
    return X

'''
# To construct the array of all scale vectors.
# The r-th component of the output is
# the matrix of level r scale vectors.
def VA(N):
    V = Id(N)
    X = [V]
    while N>2:
        #print("type(X) =", type(X))
        V = HaarV(V)
        X = X + [V]
        N = len(V) 
    V = HaarV(V)
    X = X + [[V]]
    return X
'''
    
# To construct the pair formed with the array 
# of all scale vectors and the array of all
# wavelet vectors.
def VWA(N):
    V = Id(N)
    X = [V]
    Y = []
    while N>2:
        W = HaarW(V)
        V = HaarV(V)
        X = X + [V]
        Y = Y + [W]
        N = len(V) 
    W = HaarW(V)
    V = HaarV(V)
    X = X + [[V]]
    Y = Y + [[W]]
    return X, Y

# Utility functions
def round(f,n=nd):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if (not hasattr(f, "strip") and hasattr(f, "__getitem__") or hasattr(f, "__iter__")):
        return [round(x,n) for x in f]

## OP(x,U)
'''
Computes the orthogonal projection of a vector x
on the linear space spanned by the rows of the matrix U,
provided that these rows are linearly independent.

def gram(x,U): return [dot(x,u)for u in U]
def Gram(U): return [gram(v,U) for v in U]
#
def OP(x,U):
    if U == []: return np.zeros(len(x))
    w = gram(x,U)
    G = Gram(U)
    d = det(G)
    if d == 0: return "OP: the rows of U are not lineraly independent"
    G = matrix(G)
    t = w*(inv(G))
    y = t*matrix(U)
    return y.A1
'''



# Cosmetics
import pprint
_p = pprint.PrettyPrinter()

def disp(f,n=nd): return(_p.pprint(round(f,n)))