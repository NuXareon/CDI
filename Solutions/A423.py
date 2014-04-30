## A423 : Solution
## SXD 428

from A423h import *

# Synonyms
array  = np.array
matrix = np.matrix
dot    = np.dot
det    = np.linalg.det
inv    = np.linalg.inv

''' Let us deal with the easiest functions first'''

## PP(x,v,w)
'''
If the vectors v and w are not orthogonal, 
this function yields the projection of x
on the space perp(w) in the direction
parallel to v.  
'''
def PP(x,v,w):
    d = dot(v,w)
    if d == 0: return "PP: vectors v and w are orthogonal"
    t = -dot(x,w)/d
    return x + t*v
    
## QP(x,q,w)
'''
If the vectors v = x - q and w are not orthogonal, 
this function gives the projection of x
on the space perp(w) from the point q.
'''
def QP(x,q,w):     # return PP(x,x-q,w)
    v = x-q
    d = dot(v,w)
    if d == 0: return "QP: vectors x-q and w are orthogonal"
    t = -dot(q,w)/d
    return q + t*(x-q)

## OP(x,U)
'''
Computes the orthogonal projection of a vector x
on the linear space spanned by the rows of the matrix U,
provided that these rows are linearly independent.
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
    
## Examples
#  OP(x,U)
x = array([1,1,-2])           # 3D vector 
U =array([[4,3,2],[7,-3,-8]]) # This represents a plane in 3D
y = OP(x,U)                   # orthogonal projection of x on U 

# test
u1 = U[0]; u2 = U[1]
d1=dot(x,u1)-dot(y,u1)
d2=dot(x,u2)-dot(y,u2)
print("OP: d1 and d2 should vanish:")
disp(d1) 
disp(d2)

#  OP(x,U)
U = [u2]
y = OP(x,U)                   # orthogonal projection of x on u2 
# test
d=dot(x,u2)-dot(y,u2)
print("OP: d should vanish:")
disp(d)

# PP(x,v,w)
v = u1; w = u2
y = PP(x,v,w)
# test
d = dot(y,w)
print("PP: d should vanish:")
disp(d)

# QP(x,q,w)
q = [2,3,7]
y = QP(x,q,w)
# test
d = dot(y,w)
print("QP: d should vanish:")
disp(d)




