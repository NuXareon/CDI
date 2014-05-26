## A430: Haar MRA & Compression
## SXD 430 
from A430h import *  
import matplotlib.pyplot as plt

n=10
N = 2**n

# Haar scaling and wavelet vectors
V, W = VWA(N)


F = lambda t: 1000*t**2*(1-t)**4*((t-0.35)**2+0.01)*np.cos(41*t)

t = ls(0,1,N)
f = F(t)


def proj(f,V):
    x = zeros(N)
    for v in V:
        x = x + dot(f,v)*v
    return x   

def A(r): return proj(f,V[r])
 
def D(r): return proj(f,W[r])

'''
# Approximations A^r(f)
plt.close()

plt.figure(1)
plt.axis([0, N, -0.75, 15])

for k in range(n+1):
    plt.plot(1.4*k+A(k))
    
plt.figure(2)
plt.axis([0, N, -0.75, 15])
    
for k in range(1,n+1):
    plt.plot(1.4*k+D(k))
    
plt.show()
'''

# Compression
def proj_coeffs(f,V):
    return array([dot(f,v) for v in V])

# The Haar Transform
def HaarT(f,r=1):
    x=proj_coeffs(f,V[r])
    for k in range(r,0,-1):
        x = splice([x,proj_coeffs(f,W[k])])
    return x

plt.close()

for r in range(5):
    plt.plot(2*r**1.3+HaarT(f,r))
plt.axis([0, N, -1, 15])

plt.show()

# energy(X): X can be a numerical list, tuple or set.
def energy(X):
    E=0
    for x in X:
        E += x*x
    return(E)

for r in range(6):
    print(r, energy(proj_coeffs(f,V[r])))

