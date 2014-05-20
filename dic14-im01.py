## dic14-im01.py : basic constructing of images
## SXD 520

import numpy as np
import matplotlib.pyplot as plt
from pylab import *

# Image size
m=16; n=24
X = zeros([m,n])
X2 = zeros([m,n])


# Some pixel functions
def f(i,j): return (i+j)%2
def g(i,j): return (10+i**3+j**2)%256
def h(x,y): return 255-127*(sin(i/2)**3+cos(j/5)**2)

im = f
im2 = h

R = range(m); S = range(n)

# construct a mxn image (gray)
for i in R:
    for j in S:
        X[i,j] = im(i,j)


plt.close('all')

for i in R:
    for j in S:
        X2[i,j] = im2(i,j)

plt.figure(str(m)+'x'+str(n)+' color image')
plt.axis('off')
imshow(X2, interpolation='nearest')


plt.figure(str(m)+'x'+str(n)+' gray image bilinear')
plt.gray()
plt.axis('off')
imshow(X)

'''
X[0,1]=2
plt.figure('16x16 chequer board (2)')
plt.gray()
plt.axis('off')

imshow(X, interpolation='nearest')
X[0,1]=1.5
plt.figure('16x16 chequer board (1.5)')
plt.gray()
plt.axis('off')
imshow(X, interpolation='nearest')

X[0,1]=1.1
plt.figure('16x16 chequer board (1.1)')
plt.gray()
plt.axis('off')
imshow(X, interpolation='nearest')
'''