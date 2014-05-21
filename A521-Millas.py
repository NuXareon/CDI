## A521x.py : Kick of for A521.py

from dic14_wavelets_x import *


''' A521.1
    WT of images/matrices
'''
# Generic WT of a matrix/image X
def WT(X,w='haar'):
    if w == 'haar': return WThaar(X)
    elif w == 'duab4': return WTdaub4(X)
    elif w == 'daub6': return WTdaub6(X)
    else: return 'WT : unknown wavelet system'

# Haar specific functions
def WThaar(X): return WThaarcol(WThaarrow(X))

def WThaarrow(X):
    r, c = X, shape
    X = list(X)
    Y = []
    for x in X:
        Y += [haar(x)]
    return array(Y)
#
def WThaarcol(X): return transpose(WThaarrow(transpose(X)))   


# Daub4 specific functions
def WTdaub4(X): return WTdaub4col(WTdaub4row(X))

def WTdaub4row(X):
    #...
    return X #array(Y)
#
def WTdaub4col(X): return transpose(WTdaub4row(transpose(X)))   

# Daub6 specific functions
def WTdaub6(X): return WTdaub6col(WTdaub6row(X))

def WTdaub6row(X):
    #...
    return X #array(Y)
#
def WTdaub6col(X): return transpose(WTdaub6row(transpose(X))) 
   
   
''' A521.2
    i_WT of images/matrices
'''
   
   
''' A521.3
    Examples
'''   
 
# First examples

from pylab import *

# Image size
m=16; n=24
X = zeros([m,n])

# Some pixel functions
def f(i,j): return (i+j)%2
def g(i,j): return (10+i**3+j**2)%256
def h(i,j): return 255-127*(sin(i/2)**3+cos(j/5)**2)

im = h

R = range(m); S = range(n)

# construct a mxn image (gray)
for i in R:
    for j in S:
        X[i,j] = im(i,j)

def draw(m,n,h):
    X = zeros([m,n])
    for i in range(m):
        for j in range(n):
            X[i,j] = h(i,j)
    return X

plt.close('all')


imshow(draw(8,12,lambda i,j: (i+j)%2))

plt.figure(str(m)+'x'+str(n)+' gray image')
plt.gray()
plt.axis('off')
imshow(X, interpolation='nearest')

Yrow = WThaarrow(X)
plt.figure('WThaarrow of '+str(m)+'x'+str(n)+' gray image')
plt.gray()
plt.axis('off')
imshow(Yrow, interpolation='nearest')

Ycol = WThaarcol(X)
plt.figure('WThaarcol of '+str(m)+'x'+str(n)+' gray image')
plt.gray()
plt.axis('off')
imshow(Ycol, interpolation='nearest')

Y = WT(X)
plt.figure('WT of '+str(m)+'x'+str(n)+' gray image')
plt.gray()
plt.axis('off')
imshow(Y, interpolation='nearest')