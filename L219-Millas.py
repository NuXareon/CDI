n=10
U=list(range(1,n+1))
w=[1,3,5,2,7,4,1,3,8,9]
ws=sum(w)
p=[x/ws for x in w]

def P(X):
    s = 0
    for k in X:
        s += p[k-1]
    return s
    
print("p - ", p)
print("P(U) - ", P(U))
print("P([]) - ", P([]))
print("P([2,6,7]) - ", P([2,6,7]))
print("P([3,5,6,9,10]) - ", P([3,5,6,9,10]))