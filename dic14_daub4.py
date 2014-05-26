## dic14_daub4: Module for Duab4 wavelets
## SXD 512

import numpy as np
import matplotlib.pyplot as plt

# Synonyms
Id = np.eye
sqrt = np.sqrt
array = np.array
stack = np.vstack
splice= np.hstack
dot = np.dot
ls  = np.linspace
zeros=np.zeros


# Basic constants
nd = 4
r2=sqrt(2); r3=sqrt(3);
a1=(1+r3)/(4*r2); a2=(3+r3)/(4*r2); 
a3=(3-r3)/(4*r2); a4=(1-r3)/(4*r2);
[b1,b2,b3,b4] = [a4,-a3,a2,-a1]

'''
I) D4trend, D4fluct, D4
'''

def D4trend(f, r=1):
    N = len(f)
    f = list(f)
    if r == 0: return array(f)
    if N % 2**r: return "D4trend: "+str(N)+" is not divisible by "+str(2**r)
    if r == 1:
        f = f + f[:2]
        return \
            array([a1*f[2*j]+a2*f[2*j+1]+a3*f[2*j+2]+a4*f[2*j+3] \
            for j in range(N//2)])
    else: return D4trend(D4trend(f),r-1)
        
def D4fluct(f,r=1):
    N = len(f)
    f = list(f)
    if r == 0: return zeros(N)
    if N % 2**r: return "D4fluct: "+str(N)+" is not divisible by "+str(2**r)
    if r == 1:
        f = f + f[:2]
        return \
            array([b1*f[2*j]+b2*f[2*j+1]+b3*f[2*j+2]+b4*f[2*j+3] \
            for j in range(N//2)])
    else: return D4fluct(D4trend(f,r-1))

def D4(f,r=1):
    N = len(f)
    f = list(f)
    if r == 0: return array(f)
    if N % 2**r: return "D4: "+str(N)+" is not divisible by "+str(2**r)
    #if r == 1: return np.hstack(D4trend(f),D4fluct(f))
    d = []
    while r>= 1:
        a = D4trend(f)
        d = np.hstack([D4fluct(f),d])
        f = a
        r -=1
    return np.hstack([f,d])




'''
II) Daub4 scaling and wavelet arrays
'''

# To construct the array of D4 level r scaling vectors
# from the array V of D4 level r-1 scaling vectors
def D4V(V):
    N = len(V)
    V = stack([V, V[0:2]])
    X = a1*V[0,:]+a2*V[1,:]+a3*V[2,:]+a4*V[3,:]
    for j in range(1,N//2):
        x = a1*V[2*j,:]+a2*V[2*j+1,:]+a3*V[2*j+2,:] \
          +a4*V[2*j+3,:]
        X = stack([X,x])
    return X

# To construct the array of D4 level r wavelet vectors
# from the array V of D4 level r-1 scaling vectors
def D4W(V):
    N = len(V)
    V = stack([V, V[0:2]])
    Y = b1*V[0,:]+b2*V[1,:]+b3*V[2,:]+b4*V[3,:]
    for j in range(1,N//2):
        y = b1*V[2*j,:]+b2*V[2*j+1,:]+b3*V[2*j+2,:] \
          +b4*V[2*j+3,:]
        Y = stack([Y,y])
    return Y

# To construct the pair formed with the array V 
# of all D4 scale vectors and the array W of all
# D4 wavelet vectors.
def D4VW(N):
    V = Id(N)
    X = [V] 
    Y = []
    while N>2:
        W = D4W(V)
        V = D4V(V)
        X = X + [V]
        Y = Y + [W]
        N = len(V)
    W = D4W(V)
    V = D4V(V)
    X = X + [[V]]
    Y = Y + [[W]]
    return (X, Y)

# Orthogonal projection in orthonormal basis
def proj(f,V):
    x = zeros(len(V[0]))
    for v in V:
        x = x + dot(f,v)*v
    return x  

# Projection coefficients
def proj_coeffs(f,V):
    return array([dot(f,v) for v in V])


# Annex: Utility functions
def round(f,n=nd):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if (not hasattr(f, "strip") and hasattr(f, "__getitem__") or hasattr(f, "__iter__")):
        return [round(x,n) for x in f]
        
# Cosmetics
import pprint
_p = pprint.PrettyPrinter()

def disp(f,n=nd): return(_p.pprint(round(f,n)))