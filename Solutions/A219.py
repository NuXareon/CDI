# A219

# load dic14 in order to be able to use 
# intersect(X,Y), probability(X,w), independent(X,Y,w), interacton(X,Y,w), ...
import sys
sys.path.append("d:/Docencia/2014/py/")
from dic14 import *


# Wind rose
w = [15,15,11,11,6,11,11,8]
U = range(1,len(w)+1)

# P for the wind rose
def P(X): 
    if not subset(X,U): 
        return 'A219/P: Wrong event data'
    return probability(X,w)
    
# I for the wind rose
def I(X,Y): return interaction(X,Y,w)

# Conditional probability
def CP(Y,X): return conditional_probability(Y,X,w)

# Indepencende
def Indep(X,Y): return independent(X,Y,w)


# Events relevant for A219
B = [1,2,8]         # boreal
N = [1,2,3,7,8]     # northern
C = [1,3,5,7]       # cardinal

# Independence checks
print("B and N independent?:", Indep(B,N))
print("B and C independent?:", Indep(B,C))
print("N and C independent?:", Indep(N,C))

# Bayes' checks
def Bayes_check(X,Y): 
    if CP(Y,X) == P(Y)*I(X,Y): return True
    else: return False

print("Bayes check B, N:", Bayes_check(B,N))
print("Bayes check N, B:", Bayes_check(N,B))

print("Bayes check B, C:", Bayes_check(B,C))
print("Bayes check C, B:", Bayes_check(C,B))

print("Bayes check N, C:", Bayes_check(N,C))
print("Bayes check C, N:", Bayes_check(C,N))



# Probability of B in five periods
p = P(B)
N=5
print('The probability of at least one period of B in 5 periods:',at_least_once_in(N,p))

    