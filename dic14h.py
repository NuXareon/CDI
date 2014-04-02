## dic14h.py General header file

# Get basic math functions
from math import *
'''
 pi, e, sqrt, hypot, exp, log, log10,floor, ceil
 sin, cos, tan, asin, acos, atan, atan2, 
 sinh, cosh, tanh, acosh, asinh, atanh,   
 fabs, fmod, ldexp, modf, pow(x,y)=x**y 
'''

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
