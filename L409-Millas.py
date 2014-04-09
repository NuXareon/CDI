## L409x: kick off for L409
## SXD 409

pypath="D:/Docencia/2014/py"
#pypath="/home/nuxe/pyzo2013c/CDI"
import sys
sys.path.append(pypath)

# Version 409 of dic14_haar, 
# with new versions of high_filter and low_filter
# and a couple of utilities
from L409h import *
import matplotlib.pyplot as plt
import numpy as np

## 0
'''
Study carefully the new versions of 
high_filter(f,r=1) and low_filter(f,r=1) 
in dic14_haar.py.
'''
# Tests for high_filter and low_filter
f = [2,1]
print('A(f) =',A_(f))
print('D(f) =',D_(f))
print("",add(A_(f),D_(f)))
print()

f = [10,11,15,22,17, 14, 11, 9]

print('A(f) =',A_(f))
print('D(f) =',D_(f))
print("",add(A_(f),D_(f)))
print()



## 1.
'''
1. Consider a function such as
   h(x)=20*(sin(⁡x))**2*(1-x**4)*cos(11 π x)
and sample it N = 2**n times (say n=10) on [0,1] (cf L408x). 
'''
n = 10
N = 2**n
def h(x): return 20*(sin(x))**2*2*(1-x**4)*cos(11*pi*x)
f = sample(h, N, 0, 1)
f = f[:N]
t = np.arange(0.0, 1.0, 1/N)


## 2.
'''
Let f be the discrete signal obtained in 1. 
Compute high_filter(f,r=1) for a r=1,…,n. 
The results can be arranged in an n×N matrix. 
Draw the corresponding graphs.
'''
plt.close('all')

hf = [high_filter(f,x) for x in range(1,n+1)]

print("Printing High Filter Function Plot")

plt.figure("High Filter Function Plot")
for i in range(0,len(hf)):
    plt.subplot(2,n//2,i+1)
    plt.plot(t, hf[i])

plt.show()

print("Printing High Filter Function Plot 2")

plt.figure("High Filter Function Plot 2")
for i in range(0,len(hf)):
    plt.plot(t, hf[i])

plt.show()
    
## 3.
'''
Ditto for low_filter(f,r=1).
'''
lf = [low_filter(f,x) for x in range(1,n+1)]
print("Printing Low Filter Function Plot")

plt.figure("Low Filter Function Plot")
for i in range(0,len(lf)):
    plt.subplot(2,n//2,i+1)
    plt.plot(t, lf[i])

plt.show()

print("Printing Low Filter Function Plot 2")

plt.figure("Low Filter Function Plot 2")
for i in range(0,len(lf)):
    plt.plot(t, lf[i])