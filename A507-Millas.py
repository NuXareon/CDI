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
