## A514.py : solutions to the assignment A514.pdf 
## SXD 519


## 1.
''' 
Draw, by analogy with L513.py, some Daub6 scaling and wavelet vectors. 
'''

# We need the Daub6 package:
from dic14_daub6 import *

# Let's construct Daub6 scaling and wavelet vectors
n=10; N = 2**n
V, W = D6VW(N)

# A and D vectors using D6V and D6W (we may need them)
def A(f,r): return proj(f,V[r])
def D(f,r): return proj(f,W[r-1])

# We take three scaling vectors of level 5 
# and three of level 6
v5 = V[5][1]+V[5][15]+V[5][27]
v6 = V[6][1]+V[6][7]+V[6][13]
plt.close('all')
plt.figure("Examples of Daub6 scaling vectors of length "+str(N))
plt.axis(xmin=0, xmax=N)
s = 0.3
plt.plot(s+v5)
plt.plot(v6)

# Where do vectors start and end?
def support(x):
    n = len(x)
    l = 0
    h = n-1
    while x[l] == 0 & l<n: l += 1
    if l == n-1: return []
    while x[h] == 0: h -=1
    return (l,h)

for k in 1, 15, 27:
    plt.plot(support(V[5][k]), (s,s),'o')
for k in 1, 7:
    plt.plot(support(V[6][k]), (0,0),'o')
plt.plot(support(V[6][13]), (0,0),'or', markersize=10)

# Similarly for wavelets
# We take three scaling vectors of level 5 
# and three of level 6
w5 = W[4][1]+W[4][15]+W[4][27]
w6 = W[5][1]+W[5][7]+W[5][13]

plt.figure("Examples of Daub6 wavelet vectors of length "+str(N))
plt.axis(xmin=0, xmax=N)
s = 0.3
plt.plot(s+w5)
plt.plot(w6)

for k in 1, 15, 27:
    plt.plot(support(W[4][k]), (s,s),'o')
for k in 1, 7:
    plt.plot(support(W[5][k]), (0,0),'o')
plt.plot(support(W[5][13]), (0,0),'or', markersize=10)

#   Note. Width of a scaling or wavelet vector
def width(x): 
    l, h = support(x)
    return h-l
#   Examples of width
for r in 5,6:
    print("Width scaling vector v^"+str(r)+"_1 =",width(V[r][1]))

##  2.
''' Extend L514.py to include the computation of the % energy of f 
    contained in the a^r(f), for some f of your own choice, 
    and different r. 
    '''
# So we first need an f
F = lambda t: 1000*t**2*(1-t)**4*((t-0.35)**2+0.01)*np.cos(41*t)
t = ls(0,1,N)
f = F(t)   

# energy and percent
def energy(v): return sum(t*t for t in v)
def percent(x,y): return 100 * (x/y)

# Now a^r(f) = D6trend(f,r)
ea=[energy(D6trend(f,r)) for r in range(1,n)]
eA=[energy(A(f,r)) for r in range(1,n)]
e=energy(f)

for k in range(6):
    print("The energy of a(f,"+str(k)+") is ", round(percent(ea[k],e),3), " % of the energy of f")
    print("The energy of A(f,"+str(k)+") is ", round(percent(eA[k],e),3), " % of the energy of f")

# Note:
'''
    We recognize that a^r and A^r have the same energy.
    Is there a simple general explanation?
    Yes, indeed. From the definitions we have
    A^r = Sum a^r_j V^r_j, and we know that the V^r_j
    is an orthonormal system, so 
    energey(A^r) = A^r · A^r = Sum (a^r_j)**2 = energy(a^r).
'''


##  3.
''' Compute and draw the energy profile of the D6(f,r) for different r. 
    Recall that the energy profile of a vector a can be computed as 
    [energy(b[:k]) for k in range(1,len(b)+1)]
    where b is the result of ordering a in non-increasing order.
'''

# energy_profile
def ord(a):return(sorted(a,key=lambda t:-t*t))
#
def energy_profile(a):
    b = ord(a); n = len(a)
    return array([energy(b[:k+1]) for k in range(n)])
    
# 6 energy profiles
plt.figure("Energy profiles of D6(f,r)")
plt.axis(xmin=0, xmax=N)
h=[300,200,120,75,40,15]
v=[62,70,75,79,82,86]
c=['b','g','r','c','m','y']
for k in range(6):
    plt.plot(energy_profile(D6(f,k)))
    plt.text(h[k], v[k],str(k), fontsize='14', color=c[k])



