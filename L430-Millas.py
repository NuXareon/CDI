## L430x : kickoff file for L430
## SXD 430
from A423h import *

# Synonyms
array  = np.array
matrix = np.matrix
dot    = np.dot
det    = np.linalg.det
inv    = np.linalg.inv
rint=np.random.randint


## PP(x,v,w)
'''
If the vectors v and w are not orthogonal, 
this function yields the projection of x
on the space perp(w) in the direction
parallel to v.  
'''
def PP(x,v,w):
    d = dot(v,w)
    if d == 0: return "PP: vector v is orthogonal to w"
    t = -dot(x,w)/d
    print("t =",t)
    x = array(x)
    v = array(v)
    return x + t*v

## OP(x,U) Orthogonal projection
'''
Computes the orthogonal projection of a vector x
on the linear space spanned by the rows of the matrix U,
provided that these rows are linearly independent.
The dimensions of x and of the rows of U have to be the same
'''
def gram(x,U): return [dot(x,u)for u in U]
def Gram(U): return [gram(v,U) for v in U]
#
def OP(x,U):
    if U == []: return np.zeros(len(x))
    w = gram(x,U)
    G = Gram(U)
    d = det(G)
    if d == 0: return "OP: the rows of U are not lineraly independent"
    G = matrix(G)
    t = w*(inv(G))
    y = t*matrix(U)
    return y.A1

## GPP(x,v,U)
'''
Returns the pair of points x+sv, OP(x+sv,U)
such that the distance between them is minimum
'''
def GPP(x,v,U): 
    y = OP(x,U); z = OP(v,U); a = x-y; b = v-z
    b2 = dot(b,b)
    if b2 == 0: return "GPP: v lies in <U>"
    s = -dot(a,b)/b2
    x = array(x); v = array(v)
    return (y+s*z, x+s*v)
    

## GQP(x,q,w)

def GQP(x,q,U): return GPP(x,array(x)-array(q),U)
    

## Examples 2D
x = [0,1]; v1 = [1,0]; v2 = [1,-0.5]; q =[-2,2]
U1 = []; U2 = [v1]
e1 = GPP(x,v1,U1)
e2 = GPP(x,v1,U2)
e3 = GPP(x,v2,U2)
e4 = GQP(x,q,U2)


## Examples 3D
x = [0,0,1]; v1 = [1,0,0]; v2 = [1,0,-0.5]; v3 = [1,1,0]; v4 = [1,1,2]; q = [-2,0,2]; q1 = [12,10,-17]
U1 = []; U2 = [v1]; U3 = [[1,0,0],[0,1,0]]
E1 = GPP(x,v1,U1)
E2 = GPP(x,v1,U2)
E3 = GPP(x,v2,U2)
E4 = GQP(x,q,U2)
E5 = GPP(x,v3,U2)
E6 = GPP(x,v4,U2)
E7 = GPP(x,q1,U2)
E8 = GPP(x,v1,U3)
E9 = GPP(x,v3,U3)
E10 = GPP(x,v4,U3)

## Example in 5D
x = 3-array(range(5))
v = list(rint(-10,10,5))
U = [list(rint(5,15,5)), list(rint(-4,14,5)), list(rint(-20,20,5))]

y = OP(x,U)

y1,x1 = GPP(x,v,U)

