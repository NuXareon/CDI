## L423y : examples of projections for A423
from L423h import *

# orthogonal with vectors of dimension 3
# projeccion sobre una dimesion (recta)
U = [array([4,3,2])] #np.array te operacions sobre arrays (dot prod, ...)

x = array([1,1,-2]) #vector a proyectar

u = U[0]

# x1 = t * u
# (x-x1)·u = 0
# x·u -t u·u = 0
# t = (x·u)/(u·u)

t = dot(x,u)/dot(u,u)
x1 = t*u
print(x1)
print(dot(x-x1,u)) # this must be 0!

# projeccion sobre 2 dimensiones (plano)
V = array([[4,3,2],[7,-3,-8]])
v1 = V[0]
v2 = V[1]

w = array([dot(x,v1), dot(x,v2)])

G=[
[dot(v1,v1),dot(v1,v2)],
[dot(v2,v1),dot(v2,v2)]
]
G=np.matrix(G)
H = G.I

t=w*H
t1=t[0,0]
t2=t[0,1]

x1 = t1*v1 + t2*v2 # projeccio del vector sobre el pla
print(x1)
print(dot(x-x1,v1)) # ha de ser 0
print(dot(x-x1,v2)) # ha de ser 0

