from L423h import *

def OP(x,U):
    G=[]
    for i in range(len(U)):
        g1 = []
        for j in range(len(U)):
            g1.append(dot(U[i],U[j]))
        G.append(g1)
    G=np.matrix(G)
    H=G.I
    
    w = [dot(x,U[i]) for i in range(len(U))]
    w = np.array(w)

    t = w*H
    x1 = t*U
    return x1.A1
        
    
def PP(x,v,w):
    x = np.array(x)
    v = np.array(v)
    w = np.array(w)
    t = -dot(w,x)/dot(w,v)
    x1 = x+t*v
    return x1
    
def QP(x,q,w):
    x = np.array(x)
    q = np.array(q)
    w = np.array(w)
    t = -dot(w,q)/dot(w,x-q)
    x1=q+t*(x-q)
    return x1

#Example for OP
x = [1,1,-2]
u = [[4,3,2],[7,-3,-8]]
xop = OP(x,u)

print("OP([1,1,-2],[[4,3,2],[7,-3,-8]]): ", xop);
for i in range(len(u)):
    print("test (x-xop)·u[",i,"] = 0? ",round(dot(x-xop,u[i]),10))
    
#Example for PP
v = [1,1,-1]
w = [3,-5,7]
xpp = PP(x,v,w)

print("PP([1,1,-2],[1,1,-1],[3,-5,7]): ", xpp);
print("x1·w = 0? ", round(dot(xpp,w),10))
    
#Example for QP
q = [9,6,5]
xqp = QP(x,q,w)

print("QP([1,1,-2],[9,6,5],[3,-5,7]): ", xqp);
print("x1·w = 0? ", round(dot(xqp,w),10))
    
