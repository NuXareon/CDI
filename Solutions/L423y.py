## L423y : examples of projections
## SXD 423
import numpy as np

# Synonyms
array  = np.array
matrix = np.matrix
dot    = np.dot

# Example: vector projected on 
# a line (in dim 3)
U =array([[4,3,2]]) # this represents the line

x = array([1,1,-2]) # this is the vector

u = U[0]

# x1 = t * u
# (x-x1)·u = 0
# x·u - t u·u = 0
# t = (x·u)/(u·u)

t=dot(x,u)/dot(u,u)
x1 = t*u
print("x1 =",x1)

# test
print("test (x-x1)·u = 0? ",dot(x-x1,u))

# Example: vector projected on 
# a plane (in dim 3)

V =array([[4,3,2],[7,-3,-8]]) # This represents the plane V
v1 = V[0]; v2 = V[1]  # basis of V

w=array([dot(x,v1), dot(x,v2)])

G=[
[dot(v1,v1),dot(v1,v2)],
[dot(v2,v1),dot(v2,v2)]
]
# To obtain the inverse of G
G = matrix(G)
H = G.I   # this is the inverse

t = w*H

x1 = t * V  # the solution in matrix form
x1=array(x1)[0]  # the solution as a vector

# test
print("test (x-x1)·v1 = 0 & (x-x1)·v2 = 0? ", round(dot(x-x1,v1),10), round(dot(x-x1,v2),10))


# Example parallel projection
v = array([1,1,-1])
w = array([3,-5,7])

t = -dot(w,x)/dot(w,v)
x1 = x+t*v

# test
print("x1·w = 0? ", round(dot(x1,w),10))

# Exaple Q projection
q = array([9,6,5])

t = -dot(w,q)/dot(w,x-q)
x1 = q + t * (x-q)

# test
print("x1·w = 0? ", round(dot(x1,w),10))



