## L507x: Kick off for L507
## SXD 507
'''
Daub4 scaling and wavelet arrays
'''

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

# To construct the array of D4 level r scaling vectors
# from the array V of D4 level r-1 scaling vectors
def D4V(V):
    N = len(V)
    V = stack([V, V[0:2]])
    X = a1*V[0,:]+a2*V[1,:]+a3*V[2,:]+a4*V[3,:]
    for j in range(1,N//2):
        x = a1*V[2*j,:]+a2*V[2*j+1,:]+a3*V[2*j+2,:]+a4*V[2*j+3,:]
        X = stack([X,x])
    return X

# To construct the array of D4 level r wavelet vectors
# from the array V of D4 level r-1 scaling vectors
def D4W(V):
    N = len(V)
    V = stack([V, V[0:2]])
    Y = b1*V[0,:]+b2*V[1,:]+b3*V[2,:]+b4*V[3,:]
    for j in range(1,N//2):
        y = b1*V[2*j,:]+b2*V[2*j+1,:]+b3*V[2*j+2,:]+b4*V[2*j+3,:]
        Y = stack([Y,y])
    return Y

# To construct the pair formed with the array V 
# of all D4 scale vectors and the array W of all
# D4 wavelet vectors.
def D4VW(N):
    V = Id(N)
    X = [V]
    Y = []
    while N > 2:
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
    
    
## Applications

    
n=10
N = 2**n

# Duab4 scaling and wavelet vectors
V, W = D4VW(N)


F = lambda t: 1000*t**2*(1-t)**4*((t-0.35)**2+0.01)*np.cos(41*t)
t = ls(0,1,N)

# simple functon with a jump singularity
g1 = [9*(j/N)**2 for j in range(N//3)]
g2 = [4*(j/N-1/3)**2 for j in range(N//3, 2*N//3)]
g3 = list(zeros(1 + N//3))
g = g1 + g2 + g3

eps = 0.01
# oscillating with high frequency singularity
h = [np.sin(1/(eps+j/N)) for j in range(0,N)]

f=[F(t), g, h]


## The Daub4 = D4 Transform using D4V and D4W
def D4T(f,r=1):
    x=proj_coeffs(f,V[r])
    # range should include 0, which is level 1
    for k in range(r-1,-1,-1):
        x = splice([x,proj_coeffs(f,W[k])])
    return x
    
## A and D vectors
def A(f,r): return proj(f,V[r])
def D(f,r): return proj(f,W[r-1])

# Approximations A^r(f)
f = f[0]; lo =-0.75; hi=15; sep=1.4 #smooth oscillating function
#f = f[1]; lo =-0.75; hi=16; sep=1.4 # simple function with a jump
#f = f[2]; lo =-1.2; hi=21; sep=2.0 # oscillating with high frequency singularity

plt.close('all')



plt.figure(1)
plt.axis([0, N, lo, hi])

for r in range(n+1):
    plt.plot(sep*r+A(f,r))
    
plt.figure(2)
plt.axis([0, N, lo, hi])
    
for r in range(1,n+1):
    plt.plot(sep*r+D(f,r))
    
plt.figure(3)
plt.axis([0, N, lo, hi])
    
for r in range(5):
    plt.plot(2.2*sep*r+D4T(f,r))
    
plt.show()
    
    
    
    


# Utility functions
def round(f,n=nd):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if (not hasattr(f, "strip") and hasattr(f, "__getitem__") or hasattr(f, "__iter__")):
        return [round(x,n) for x in f]
        
# Cosmetics
import pprint
_p = pprint.PrettyPrinter()

def disp(f,n=nd): return(_p.pprint(round(f,n)))






