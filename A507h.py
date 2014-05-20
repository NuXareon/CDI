## A507h : header for A507.py
## SXD 512

from dic14_daub4 import *

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



