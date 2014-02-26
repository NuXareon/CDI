'''
DIC14 utilities
'''

# Checks 
def weight_list(W):
    if len(W)<2: return False
    for w in W:
        if w <= 0: return False
    return True

# intersection of two lists, ranges or tuples
def intersect(X,Y): return set(X) & set(Y)

#A=range(5); B=list(range(7,2,-1)); C={3,4,7,11,15}

# checks whether X is a subset of U
def subset(X,U): 
    if intersect(X,U)==set(X): return True
    else: return False

# probability of X with respect to list of weights
# X has to be a subset of range(1,len(w)+1).
def probability(X,w):
    if not weight_list(w): return 'dic14/probability: Wrong weight list'
    U = range(1,len(w)+1)
    if not subset(X,U): return 'dic14/probability: Wrong event data'
    p = 0
    for k in X:
        p += w[k-1]
    return p/sum(w)

# interaction index of X and Y for probabilities defined by w.
def interaction(X,Y,w):
    if list(X) == [] or list(Y) == []: 
        return 'dic14/interaction: events have to be non empty'
    return probability(intersect(X,Y),w)/probability(X,w)/probability(Y,w)
 
# Independence of X and Y for probabilities defined by w.   
def independent(X,Y,w): 
    x = probability(X,w)
    y = probability(Y,w)
    xy = probability(intersect(X,Y),w)
    if xy == x*y: return True
    else: return False

# Probability of Y conditioned to the occurrence of of X, 
# with with respect to w.
def conditional_probability(Y,X,w): 
    if list(X) == []: 
        return 'dic14/conditional_probability: Wrong data for conditioning event'
    return probability(intersect(X,Y),w)/probability(X,w)
  
def at_least_once_in(N,p): return 1-(1-p)**N

def weighted_average(E,w):
    if not weight_list(w): 
        return 'dic14/weighted_average: Wrong weight list'
    if len(E) != len(w): 
        return 'dic14/weighted_average: lengths unequal'
    a = 0
    for k in range(0,len(E)):
        a += w[k]*E[k]
    return a/sum(w)

def average(E): 
    if len(E)==0: 
        return 'dic14/average: E has to be non-empty'
    return sum(E)/len(E) 
    
