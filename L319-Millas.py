L = [1,1,1,1,2,2,2,3,3,4]
A = ['a','b','c']
B = [1,2,3]

print("L = ",L)

def ells2ens(L):
    B = list(set(L))
    return {l : L.count(l) for l in B}

N = ells2ens(L)
print("N = ells2ens(L) = ",N)
    
def ens2ells(N):
    B = []
    B += [i for i in N for j in range(1,N[i]+1)]
    return B
    
L2 = ens2ells(N)
print("ens2ells(N) = ",L2)
    
def cart(X,Y):
    if not X:
        return sorted({str(x) for y in Y})
    if not Y:
        return sorted({str(y) for x in X})
    return sorted({str(x)+str(y) for x in X for y in Y})
    
print("A = ",A)
print("B = ",B)
print("cart(A,B) = ",cart(A,B))