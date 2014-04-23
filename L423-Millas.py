## L423 Scaling and wavelet vectors (continuation of L422)
## SXD 423 (santjòrdii !!)
from L423h import *  



# To construct the array of level r scaling vectors
# from the array V of level r-1 scaling vectors
def HaarV(V):
    N = len(V)
    X = a1*V[0,:] + a2*V[1,:]
    for j in range(1, N//2):
        x = a1 * V[2*j,:] + a2 * V[2*j+1,:]
        X = stack([X,x])
    return X

# To construct the array of level r wavelet vectors
# from the array V of level r-1 scaling vectors
def HaarW(V):
    N = len(V)
    X = a1*V[0,:] - a2*V[1,:]
    for j in range(1, N//2):
        x = a1 * V[2*j,:] - a2 * V[2*j+1,:]
        X = stack([X,x])
    return X

# To construct the array of all scale vectors.
# The r-th component of the output is
# the matrix of level r scale vectors.
def VA(N):
    V = Id(N)
    X = [V]
    while N>2:
        V = HaarV(V)
        X = X + [V]
        N = len(V)
    V = HaarV(V)
    X = X + [[V]]
    return X
    
# To construct the pair formed with the array 
# of all scale vectors and the array of all
# wavelet vectors.
def VWA(N):
    V = Id(N)
    X = [V]
    Y = []
    while N>2:
        W = HaarW(V)
        V = HaarV(V)
        X = X + [V]
        Y = Y + [W]
        N = len(V)
    W = HaarW(V)
    V = HaarV(V)
    X = X + [[V]]
    Y = Y + [[W]]
    return X, Y


# Show examples

'''

# close all graphics
plt.close()
n=8; N=2**n
V,W = VWA(N)
    

plt.figure("Some scaling vectors")
plot(V[3][1])
plot(V[3][15])
plot(V[3][31])

plt.figure("Some wavelets")
plot(W[2][1])
plot(W[2][15])
plot(W[2][31])

'''

# close all graphics
plt.close()
n=10; N=2**n
V,W = VWA(N)

# some scaling vectors of level 5 and 6 
plt.figure(1)
plot(2.5+V[5][1])
plot(2+V[5][8])
plot(1.5+V[5][20])

plot(1+V[6][1])
plot(0.5+V[6][4])
plot(V[6][15])

# some wavelet vectors of level 5 and 6 
plt.figure(2)
plot(2.5+W[4][1])
plot(2+W[4][8])
plot(1.5+W[4][20])

plot(1+W[5][1])
plot(0.5+W[5][4])
plot(W[5][15])

show