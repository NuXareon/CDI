# A226-h: overhead file for A226

# load numpy and pyplot
import numpy as np
import matplotlib.pyplot as plt

# Key functions
def log2(x): return np.log(x)/np.log(2)

e_ = np.e

def h_(p): return -p * log2(p) 

def c_(p): return h_(p)+h_(1-p)


# utilities for graphing vertical and horizontal lines
def hline(a,b,h,lw=1,dash='k-'):
    x = np.arange(a,b+0.0001,b-a)
    return plt.plot(x,h+0*x,dash, lw=lw)
    
def vline(a,b,d,lw=1, dash='k-'):
    y = np.arange(a,b+0.0001,b-a)
    return plt.plot(d+0*y,y,dash, lw=lw )



