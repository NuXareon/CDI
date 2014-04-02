## dic14-haar.py is a tool module for Haar wavelet (T5)

pypath="D:/Docencia/2014/py"
pypath="/home/nuxe/pyzo2013c/CDI"

import sys
sys.path.append(pypath)

from dic14h import *


## Core functions 

def transpose(F):
    m = len(F); n = len(F[0])
    T = []
    for j in range(n):
        c = []
        for i in range(m):
            c += [F[i][j]]
        T += [c]
    return T
        
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

def haar2d_rows(F):
    H = []
    for f in F:
        H += [haar(f)]
    return H
    
def haar2d(F):
    H = haar2d_rows(F)
    H = transpose(H)
    H = haar2d_rows(H)
    return H
        
F = [
[10,12,13,14],
[17,16,15,14],
[12,11,10,10],
[7,9,11,12]
]

'''
def high_filter(f,r=1):
    N=len(f); m=2**r; A=[]; K=sqrt(2)**(m/2)
    while N>=m:
        x=average(f[:m])*K        
        A += m*[x]
        N -= m
        f = f[m:]
    return A

def low_filter(f,r=1):
    N=len(f); m=2**r; D=[]; K=sqrt(2)**(m/2)
    while N>=m:
        x=average(f[:(m/2)])*K    
        N -= m/2
        f = f[(m/2):]
        x -= average(f[:(m/2)])*K
        x = x/2
        D += (m/2)*[-x] + (m/2)*[x]
        N -= m/2
        f = f[m:]
    return D


def low_filter_alternative(f,r=1):
    N=len(f); m=2**r; D=[]; K=sqrt(2)**(m/2)
    while N>=m:
        x=average(f[:int(m/2)])*K    
        N -= m/2
        f1 = f[int(m/2):] 
        x -= average(f1[:int(m/2)])*K
        x = x/2
        x = float(trunc(x,3))
        D += int(m/2)*[x] + int(m/2)*[-x]
        N -= m/2
        f = f[m:]
    return D
  '''  

def round(f,n):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if (not hasattr(f, "strip") and hasattr(f, "__getitem__") or hasattr(f, "__iter__")):
        return [round(x,n) for x in f]
    
    
