# A309h : header file for A306 

from math import log
import string

def log2(x): return log(x)/log(2)

# entropy function
def entropy(W):
    S = sum(W)
    #assert S != 0
    if S == 0: return 'A305h/entropy(W): W is not a weight distribution' 
    H = 0
    for w in W:
        if w < 0: return 'A305h/entropy(W): W is not a weight distribution'
        if w == 0: continue
        else: H -= w * log2(w)
    H += S * log2(S)
    return H/S

def row_marginal(P): return [sum(p) for p in P]

def col(k,P): return [P[j][k] for j in range(len(P))]

def col_marginal(P): return [sum(col(k,P)) for k in range(len(P[0]))]

def unfold(P):
    X = []
    for p in P:
        X += p
    return X

def joint_entropy(P): return entropy(unfold(P))

def joint_distribution(U,CPM):
    P = []
    n = sum(U.values())
    for j in list(string.ascii_lowercase): 
        c = U[j]
        i = ord(j)-ord('a')
        p = CPM[i]
        p = [(c/n) * p[k] for k in range(len(p))]
        P.append(p)
    return P