w = [15,15,11,11,6,11,11,15]
ws = sum(w)
p = [x/ws for x in w]

B = [1,2,8]
N = [1,2,3,7,8]
C = [1,3,5,7]

def P(X):
    s = 0
    for k in X:
        s += p[k-1]
    return s
    
def independents(X,Y):
    XY = [x for x in X for y in Y if x == y]
    pxy = P(XY)
    px = P(X)
    py = P(Y)
    return(pxy != px*py)
    print(pxy, " - ", px*py)
    
def I(X,Y):
    XY = [x for x in X for y in Y if x == y]
    pxy = P(XY)
    px = P(X)
    py = P(Y)
    return(pxy/(px*py))
    
def Bayes(X,Y):
    return(P(X)*I(X,N))


print("Independent pairs of events: ")
if (independents(B,N)): 
    print("(B,N)")
if (independents(B,C)): 
    print("(B,C)")
if (independents(N,C)): 
    print("(N,C)")
    
print("I(B,N) = ",I(B,N))
print("I(B,C) = ",I(B,C))
print("I(N,C) = ",I(N,C))

print("Bayes rule for P(B|N)",Bayes(B,N))
print("Bayes rule for P(N|B)",Bayes(N,B))
print("Bayes rule for P(B|C)",Bayes(B,C))
print("Bayes rule for P(C|B)",Bayes(C,B))
print("Bayes rule for P(N|C)",Bayes(N,C))
print("Bayes rule for P(C|N)",Bayes(C,N))

print("Probability of at least one period of B-wind in 5 periods: ",P(B)+P(B)**2+P(B)**3+P(B)**4+P(B)**5)
