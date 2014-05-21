##  dic14_wavelets_x 
##  SXD 521 
''' 
    Kick off for the constrution of dic14_wavelets,
    a module of haar, daub4 and daub6 functions suitable for
    compression and decompression
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
matrix=np.matrix
transpose=np.transpose

# Basic constants
nd = 4  # default number of decimal places in rounding
r2=sqrt(2); r3=sqrt(3);


## 0. General functions

# Utility functions
# average(X): X can be a numerical list, tuple or set.
def average(X): return(sum(X)/len(X))

# energy(X): X can be a numerical list, tuple or set.
def energy(X): 
    return sum(x*x for x in X)

# sample(h,N, a=0, b=1): if h is a function defined on [a,b] 
# and N is a positive integer, it returns the list of 
# samples h(a+j*s) of h for j = 0,...,N, s = (b-a)/N
def sample(h, N, a=0, b=1):
    s = (b-a)/N
    return [h(a+j*s) for j in range(N+1)]
    
# If f is a sequence, # decimate(f) 
# returns [f[1],f[3],...]
def decimate(f): 
    return [f[j] for j in range(1,len(f),2)]
    
# Orthogonal projection in orthonormal basis
def proj(f,V):
    x = zeros(len(V[0]))
    for v in V:
        x = x + dot(f,v)*v
    return x  

# Projection coefficients
def proj_coeffs(f,V):
    return array([dot(f,v) for v in V])

def dual(a):
    s = (-1)**(len(a)-1); b=[]
    for t in a:
        b = [s*t]+b 
        s *= -1
    return b

# Cosmetics

# To round a float to n decimal places. It also works
# for a list or a matrix of floats.
def roundfloat(f,nd=3): return float("%.*f" % (nd,f))
def roundmatrix(f,nd=3): 
    r,c = f.shape
    return matrix( [[roundfloat(f[i,j],nd) for j in range(c)] for i in range(r)] )
def round(f,nd=3):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return roundfloat(f,nd)
    if isinstance(f,list) and not isinstance(f[0],list): return [roundfloat(t,nd) for t in f]
    if isinstance(f,matrix): return roundmatrix(f,nd)
    #if (not hasattr(f, "strip") and hasattr(f, "__getitem__") or hasattr(f, "__iter__")):
    #    return [round(x,nd) for x in f]
    return 'round: unknown type for rounding'

import pprint
_p = pprint.PrettyPrinter()

def disp(f,n=5): return(_p.pprint(round(f,n)))



## 1. Haar wavelets

# trend(f) computes the trend signal of a discrete signal f
def trend(f):
    r=sqrt(2); J = range(len(f)//2)
    return [(f[2*j]+f[2*j+1])/r for j in J]

# fluct(f) computes the fluctuation 
# (or difference) signal of a discrete signal f    
def fluct(f):
    r=sqrt(2); J = range(len(f)//2)
    return [(f[2*j]-f[2*j+1])/r for j in J]

# haar(f,r) computes the Haar transform of f or order r. 
# haar(f) is equivalent to haar(f,1)
def haar(f,r=1): 
    if r==1: return (trend(f)+fluct(f))
    N=len(f); m=N//2**(r-1)
    a=haar(f,r-1); x=a[:m]
    return trend(x)+fluct(x)+a[m:]

# To comput A^r(f) -- T5.13 to T5.16
def high_filter(f,r=1):
    N=len(f); m=2**r; A=[]; 
    while N>=m:
        x=sum(f[:m])      
        A += m*[x]
        N -= m
        f = f[m:]
    r2 = 1.4142135623730951
    k = r//2; K = 2**k
    if r%2: K *= 2 
    else: K *= r2
    return [a/K for a in A]

# To comput D^r(f) -- T5.13 to T5.16
def low_filter(f,r=1):
    N=len(f); m=2**(r-1); D=[]; 
    while N>=2*m:
        x=sum(f[:m])
        N -= m
        f = f[m:]
        x -= sum(f[:m])
        D += m*[x]+ m*[-x]
        N -= m
        f = f[m:]
    r2 = 1.4142135623730951
    k = r//2; K = 2**k
    if r%2: K *= 2 
    else: K *= r2
    return [d/K for d in D]


''' L521.1a

    Define a function that constructs the
    haar matrix dim N
'''
def haar_matrix(N):  # for vectors of length N
    r = 1/r2
    H = zeros([N,N])
    for i in range(N//2):
        H[2*i,2*i] = H[2*i,2*i+1] = H[2*i+1,2*i] = r
        H[2*i+1,2*i+1] = -r
    return matrix(H) 

''' L521.1b
    Define a function that is inverse of haar (for one step)
'''
def i_haar(y):
    x = []
    N = len(y)
    r = N//2
    for j in range(r):
        x += [y[j], y[r+j]]
    return x * haar_matrix(N)

## 2. Daub4

'''
I) D4trend, D4fluct, D4
'''

def D4trend(f, r=1):
    a1=(1+r3)/(4*r2); a2=(3+r3)/(4*r2); a3=(3-r3)/(4*r2); a4=(1-r3)/(4*r2);
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
    a1=(1+r3)/(4*r2); a2=(3+r3)/(4*r2); a3=(3-r3)/(4*r2); a4=(1-r3)/(4*r2);
    [b1,b2,b3,b4] = dual([a1,a2,a3,a4])
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
    a1=(1+r3)/(4*r2); a2=(3+r3)/(4*r2); a3=(3-r3)/(4*r2); a4=(1-r3)/(4*r2);
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
    a1=(1+r3)/(4*r2); a2=(3+r3)/(4*r2); a3=(3-r3)/(4*r2); a4=(1-r3)/(4*r2);
    [b1,b2,b3,b4] = dual([a1,a2,a3,a4])
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

''' L521.2a

    Define a function that constructs the daub4 matrix of dim N
'''
def daub4_matrix(N):  # for vectors of length N
    a1=(1+r3)/(4*r2); a2=(3+r3)/(4*r2); a3=(3-r3)/(4*r2); a4=(1-r3)/(4*r2);
    [b1,b2,b3,b4] = dual([a1,a2,a3,a4])
    D = zeros([N,N])
    for i in range(N//2):
        D[2*i,2*i] = a1
        D[2*i,2*i+1] = a2
        D[2*i,(2*i+2)%N] = a3
        D[2*i,(2*i+3)%N] = a4
        
        D[2*i+1,2*i] = b1
        D[2*i+1,2*i+1] = b2
        D[2*i+1,(2*i+2)%N] = b3
        D[2*i+1,(2*i+3)%N] = b4
    return matrix(D)

''' L521.2b
    Define a function that yields the inverse of D4
'''
def i_daub4(y):
    x = []
    N = len(y)
    r = N//2
    for j in range(r):
        x += [y[j], y[r+j]]
    return x * daub4_matrix(N)

## 3. Daub6

'''
I) D6trend, D6fluct, D6
'''

def D6trend(f, r=1):
    a1= 0.332670552950083; a2= 0.806891509311092;  a3=0.459877502118491
    a4=-0.135011020010255; a5=-0.0854412738820267; a6=0.0352262918857095
    N = len(f)
    f = list(f)
    if r == 0: return array(f)
    if N % 2**r: return "D6trend: "+str(N)+" is not divisible by "+str(2**r)
    if r == 1:
        f = f + f[:4]
        return \
            array([a1*f[2*j]+a2*f[2*j+1]+a3*f[2*j+2]+a4*f[2*j+3]+a5*f[2*j+4]+a6*f[2*j+5] \
            for j in range(N//2)])
    else: return D6trend(D6trend(f),r-1)
        
def D6fluct(f,r=1):
    a1= 0.332670552950083; a2= 0.806891509311092;  a3=0.459877502118491
    a4=-0.135011020010255; a5=-0.0854412738820267; a6=0.0352262918857095
    [b1,b2,b3,b4,b5,b6] = dual([a1,a2,a3,a4,a5,a6])
    N = len(f)
    f = list(f)
    if N % 2**r: return "D6fluct: "+str(N)+" is not divisible by "+str(2**r)
    if r == 1:
        f = f + f[:4]
        return \
            array([b1*f[2*j]+b2*f[2*j+1]+b3*f[2*j+2]+b4*f[2*j+3]+b5*f[2*j+4]+b6*f[2*j+5] \
            for j in range(N//2)])
    else: return D6fluct(D6trend(f,r-1))

def D6(f,r=1):
    N = len(f)
    f = list(f)
    if r == 0: return array(f)
    if N % 2**r: return "D6: "+str(N)+" is not divisible by "+str(2**r)
    d = []
    while r>= 1:
        a = D6trend(f)
        d = np.hstack([D6fluct(f),d])
        f = a
        r -=1
    return np.hstack([f,d])

'''
II) Daub6 scaling and wavelet arrays
'''

# To construct the array of D6 level r scaling vectors
# from the array V of D6 level r-1 scaling vectors
def D6V(V):
    a1= 0.332670552950083; a2= 0.806891509311092;  a3=0.459877502118491
    a4=-0.135011020010255; a5=-0.0854412738820267; a6=0.0352262918857095
    N = len(V)
    X = a1*V[(0 % N),:]+a2*V[(1 % N),:]+a3*V[(2 % N),:]\
       +a4*V[(3 % N),:]+a5*V[(4 % N),:]+a6*V[(5 % N),:]
    for j in range(1,N//2):
        x = a1*V[(2*j)% N,:]+a2*V[(2*j+1)% N,:]+a3*V[(2*j+2) % N,:] \
           +a4*V[(2*j+3)% N,:]+a5*V[(2*j+4)% N,:]+a6*V[(2*j+5)% N,:]
        X = stack([X,x])
    return X

# To construct the array of D6 level r wavelet vectors
# from the array V of D6 level r-1 scaling vectors
def D6W(V):
    a1= 0.332670552950083; a2= 0.806891509311092;  a3=0.459877502118491
    a4=-0.135011020010255; a5=-0.0854412738820267; a6=0.0352262918857095
    [b1,b2,b3,b4,b5,b6] = dual([a1,a2,a3,a4,a5,a6])
    N = len(V)
    Y = b1*V[0 % N,:]+b2*V[1 % N,:]+b3*V[2 % N,:]\
       +b4*V[3 % N,:]+b5*V[4 % N,:]+b6*V[5 % N,:]
    for j in range(1,N//2):
        y = b1*V[(2*j)% N,:]+b2*V[(2*j+1)% N,:]+b3*V[(2*j+2)% N,:] \
          +b4*V[(2*j+3)% N,:]+b5*V[(2*j+4)% N,:]+b6*V[(2*j+5)% N,:]
        Y = stack([Y,y])
    return Y

# To construct the pair formed with the array V 
# of all D6 scale vectors and the array W of all
# D6 wavelet vectors.
def D6VW(N):
    V = Id(N)
    X = [V] 
    Y = []
    while N>2:
        W = D6W(V)
        V = D6V(V)
        X = X + [V]
        Y = Y + [W]
        N = len(V)
    W = D6W(V)
    V = D6V(V)
    X = X + [[V]]
    Y = Y + [[W]]
    return (X, Y)


''' L521.3a
    Define a function that constructs the daub6 matrix of dim N
'''
def daub6_matrix(N):  # for vectors of length N
    a1= 0.332670552950083; a2= 0.806891509311092;  a3=0.459877502118491
    a4=-0.135011020010255; a5=-0.0854412738820267; a6=0.0352262918857095
    [b1,b2,b3,b4,b5,b6] = dual([a1,a2,a3,a4,a5,a6])
    D = zeros([N,N])
    for i in range(N//2):
        D[2*i,2*i] = a1
        D[2*i,2*i+1] = a2
        D[2*i,(2*i+2)%N] = a3
        D[2*i,(2*i+3)%N] = a4
        D[2*i,(2*i+4)%N] = a5
        D[2*i,(2*i+5)%N] = a6
        
        D[2*i+1,2*i] = b1
        D[2*i+1,2*i+1] = b2
        D[2*i+1,(2*i+2)%N] = b3
        D[2*i+1,(2*i+3)%N] = b4
        D[2*i+1,(2*i+4)%N] = b5
        D[2*i+1,(2*i+5)%N] = b6
    return matrix(D)

''' L521.3b
    Define a function that yields the inverse of D6
'''
def i_daub6(y):
    N = len(y)
    r = N//2
    x = []
    for j in range(r):
        x+=[y[j],y[j+r]]
    return x * daub6_matrix(N)