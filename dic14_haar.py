## dic14-haar.py is a tool module for Haar wavelets (T5)
## SXD 408, 409

pypath="D:/Docencia/2014/py"

import sys
sys.path.append(pypath)

# Loads utilities: 
# average(X), energy(X), sample(h, N, a=0, b=1), 
# decimate(f), round(f,n)
from dic14h import *


## Core functions 

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

    
