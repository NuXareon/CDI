<<<<<<< HEAD
## A507x: kick of for A507
## SXD 507

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

def D4trend(f):
    N = len(f)
    f = list(f)
    f = f + f[:2]
    return \
       array([a1*f[2*j]+a2*f[2*j+1]+a3*f[2*j+2]+a4*f[2*j+3] \
              for j in range(N//2)])

def D4fluct(f):
    N = len(f)
    f = list(f)
    f = f + f[:2]
    return \
       array([b1*f[2*j]+b2*f[2*j+1]+b3*f[2*j+2]+b4*f[2*j+3] \
       for j in range(N//2)])

def D4(f,r=1):
    if r<1: return "D4: r must be a positive"
    N = len(f)
    f = list(f)
    if N % 2**r: return "D4: 2**r does not divide N"
    if r == 1: return np.hstack([D4trend(f), D4fluct(f)])
    m = N//2**(r-1)
    x = D4(f,r-1)
    a = x[:m]
    return np.hstack([D4(a), x[-(N-m):]]) 



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
    return X, Y

# Orthogonal projection in orthonormal basis
def proj(f,V):
    x = zeros(len(V[0]))
    for v in V:
        x = x + dot(f,v)*v
    return x  

# Projection coefficients
def proj_coeffs(f,V):
    return array([dot(f,v) for v in V])



n=10
N = 2**n

## Daub4 scaling and wavelet vectors
V, W = D4VW(N)
## The Daub4 = D4 Transform using D4V and D4W
def D4T(f,r=1):
    x=proj_coeffs(f,V[r])
    # range should include 0, which is level 1
    for k in range(r-1,-1,-1):
        x = splice([x,proj_coeffs(f,W[k])])
    return x

## A and D vectors using D4V and D4W
def A(f,r): return proj(f,V[r])
def D(f,r): return proj(f,W[r-1])


## Examples
    
F = lambda t: 1000*t**2*(1-t)**4*((t-0.35)**2+0.01)*np.cos(41*t)
t = ls(0,1,N)

# simple functon with a jump singularity
g1 = [9*(j/N)**2 for j in range(N//3)]
g2 = [4*(j/N-1/3)**2 for j in range(N//3, 2*N//3)]
g3 = list(zeros(1 + N//3))
g = g1 + g2 + g3

# oscillating with high frequency singularity
h = [np.sin(1/(j/N)) for j in range(1,N+1)]

f=[F(t), g, h]




# Approximations A^r(f)
f1 = f[0]; lo =-0.75; hi=15; sep=1.4 #smooth oscillating function
#f = f[1]; lo =-0.75; hi=16; sep=1.4 # simple function with a jump
#f = f[2]; lo =-1.2; hi=21; sep=2.0 # oscillating with high frequency singularity


plt.close('all')

plt.figure(1)
plt.axis([0, N, lo, hi])

for r in range(n+1):
    plt.plot(sep*r+A(f1,r))
    
plt.figure(2)
plt.axis([0, N, lo, hi])

for r in range(1,n+1):
    plt.plot(sep*r+D(f1,r))

plt.figure(3)
plt.axis([0, N, lo, hi])

for r in range(5):
    plt.plot(2*sep*r**1.1+D4T(f1,r))
    
plt.show()

    
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

## Possible answers to assignment

plt.figure(4)
plt.plot(2*sep*r**1.1+D4(f1,2))
    
f2 = f[1]; lo =-0.75; hi=16; sep=1.4 # simple function with a jump

plt.figure(5)
plt.axis([0, N, lo, hi])
for r in range(5):
    plt.plot(2*sep*r**1.1+D4T(f2,r))

plt.figure(6)
plt.plot(2*sep*r**1.1+D4(f2,2))

## A507-Millas
'''
D4trend, D4fluct, D4, D4high, D4low
'''

import numpy as np
import matplotlib.pyplot as plt
from math import *

r2=sqrt(2.0); r3=sqrt(3.0)
a1=(1+r3)/(4*r2); a2=(3+r3)/(4*r2)
a3=(3-r3)/(4*r2); a4=(1-r3)/(4*r2)
[b1,b2,b3,b4] = [a4,-a3,a2,-a1]


def D4trend(f):
    N = len(f)
    f = f + f[:2]
    return [a1*f[2*j]+a2*f[2*j+1]+a3*f[2*j+2]+a4*f[2*j+3] for j in range(N//2)]
    
def D4fluct(f):
    N = len(f)
    f = f + f[:2]
    return [b1*f[2*j]+b2*f[2*j+1]+b3*f[2*j+2]+b4*f[2*j+3] for j in range(N//2)]   
 
def D4fluct_recur(f, r = 1):
    if r == 1: return D4fluct(f)
    else:
        f = D4fluct_recur(f,r-1)
        return f + D4fluct_recur(f,r1)

def average(f): return sum(f)/len(f)

def D4(f,r=1):
    return 0
  
def D4low(f,r = 1):
    N = len(f)
    m = 2**r
    A = []
    while N >= m:
        x = average(f[:m//2])
        N -= m//2
        f1 = f[-N]
        x -= average(f1[:m//2])
        x /= 2
        A += (m//2)*[x]+(m//2)*[-x]
        N -= m//2
        f = f[:-N]
    return 0

def D4high(f,r = 1):
    N = len(f)
    m = 2**r
    A = []
    while N >= m:
        x = average(f[:m])
        A = A + m*[x]
        N -= m
        f = f[-N]
    return A
