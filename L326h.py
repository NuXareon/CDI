# L326h. Header for L326

# import header
#pypath = 'D:/Docencia/2014/py'
pypath = '/home/nuxe/pyzo2013c/CDI'

import sys
sys.path.append(pypath)
from dic14_round import *

# If P is a probability distribution 
# accumulate(P) returns the accumulated  dstribution
def accumulate(P): 
    S=[]            # for the accumulated distribution
    s=0.0           # the current accumulating value
    for p in P:
        s += p[1]   # x[1] is the probability of the symbol x[0]
        S += [(p[0],s)]  # add the new pair to S.
    return(S)

# M message string 
# P probability distribution: list of pairs (symbol, probability)
# IE(M,P) returns the pair (l_M,h_M)
def IE(M, P):       
    S=accumulate(P)
    P=dict(P); S=dict(S)
    l=0.0; h=1.0; u=h-l
    for x in M:
        h=l+S[x]*u; u=P[x]*u; l=h-u
    return (l,h)
    
    
# If x is in [0,1), it returns nb bits of the binary expansion of x
def dec2bin(x,nb=58):
    if (x<0) | (x>=1): return "dec2bin: was expecting a number in [0,1)"
    xb=""
    for j in range(nb):
        x=2*x
        if x<1:
            xb=xb+'0'
        else:
            xb=xb+'1'
            x -= 1
    return xb

# If xb is a string of bits, it returns the decimal number in [0,1)
# whose binary expansion is xb
def bin2dec(xb):
    x=0.0; j=1
    for b in xb:
        b=int(b)
        if b==0: pass
        else: x=x+b/2**j
        j=j+1
    return x

# Bit encoding of the interval [a,b)
def BE(a,b,nb=58):
    if (a<0) | (a>=b) | (b>1): return "BE: was expecting 0<=a < b<=1"
    l=dec2bin(a,nb)
    h=dec2bin(b,nb)
    r=0
    while l[r]==h[r]:
        r += 1
        if r>=nb: 
            print("BE: The bit precision is too low")
            break  
    h=h[:r]+'1'
    if bin2dec(h)<b: return h
    else: 
        if bin2dec(l[:r])==a: return l[:r]
        x=l[(r+1):]
        if x[0]=='0': return l[:r]+'01'
        j=x.index('0')
        return l[:r+1+j]+'1'

def AE(M, P, nb=58):
    l, h = IE(M, P)
    return([len(M),BE(l,h,nb)])

# C = [N, binary_string] is the arithmetically coded message
# P list of pairs (symbol, probability): [ ..., (s, p), ... ]
def AD(C,P):
    N = C[0]
    x=C[1]
    x=bin2dec(x)
    A=accumulate(P)
    P=dict(P) # S=dict(S)
    l=0; h=1; M=""
    for j in range(N):
        u = h-l
        for (k,q) in A:
            if (l+q*u <= x): continue
            else: break
        M += k
        h = l + q*u; l = h-P[k]*u
    return M

