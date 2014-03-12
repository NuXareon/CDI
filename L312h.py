'''
L312 utilities
'''

from math import log
from math import e as e_

def log2(x): return log(x)/log(2)

def mult(a,X): return [a*x for x in X]

def h(p): return -p * log2(p)

def is_sequence(arg):
    return (not hasattr(arg, "strip") and
            hasattr(arg, "__getitem__") or
            hasattr(arg, "__iter__"))

def round(f,n):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if is_sequence(f):
        return [round(x,n) for x in f]

# Morse frequencies
MF=[12544401, 7952531, 1918182]

# 1-character Englich frequencies
W_=[0.0651738, 0.0124248, 0.0217339, 0.0349835, 0.1041442, 0.0197881, 0.0158610, 
    0.0492888, 0.0558094, 0.0009033, 0.0050529, 0.0331490, 0.0202124, 0.0564513, 
    0.0596302, 0.0137645, 0.0008606, 0.0497563, 0.0515760, 0.0729357, 0.0225134, 
    0.0082903, 0.0171272, 0.0013692, 0.0145984, 0.0007836, 0.1918182]
    
W = W_[:len(W_)-1]
w_ = W_[len(W_)-1]

W = mult(1/(1-w_),W)

# A309h : header file for A306 

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
