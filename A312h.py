# A312h: data and utilities for A312

from math import log

# Frequencies of characters
F={'a': 651738, 'b': 124248, 'c': 217339, 'd': 349835, 'e':1041442, 'f': 197881, 'g': 158610, 
   'h': 492888, 'i': 558094, 'j':   9033, 'k':  50529, 'l': 331490, 'm': 202124, 'n': 564513, 
   'o': 596302, 'p': 137645, 'q':   8606, 'r': 497563, 's': 515760, 't': 729357, 'u': 225134, 
   'v':  82903, 'w': 171272, 'x':  13692, 'y': 145984, 'z':   7836, '_': 1918182}
   

# MorseCode (dot,dash) denotes number of dots and number of dashes in each character
M = {
'a':(1,1), 'b':(3,1), 'c':(2,2), 'd':(2,1), 'e':(1,0), 'f':(3,1), 
'g':(1,2), 'h':(4,0), 'i':(2,0), 'j':(1,3), 'k':(1,2), 'l':(3,1), 
'm':(0,2), 'n':(1,1), 'o':(0,3), 'p':(2,2), 'q':(1,3), 'r':(2,1), 
's':(3,0), 't':(0,1), 'u':(2,1), 'v':(3,1), 'w':(1,2), 'x':(2,2), 
'y':(1,3), 'z':(2,2)
}

ME_ = {
'a':(0.0545,4), 'b':(0.0128,6), 'c':(0.0263,5), 'd':(0.0285,5), 
'e':(0.0913,4), 'f':(0.0173,6), 'g':(0.0133,5), 'h':(0.0313,5),
'i':(0.0599,4), 'j':(0.0006,10), 'k':(0.0084,7), 'l':(0.0335,5),
'm':(0.0235,6), 'n':(0.0596,4), 'o':(0.0689,4), 'p':(0.0192,6),
'q':(0.0008,9), 'r':(0.0508,5), 's':(0.0567,4), 't':(0.0706,4),
'u':(0.0334,5), 'v':(0.0069,8), 'w':(0.0119,7), 'x':(0.0073,7),
'y':(0.0164,6), 'z':(0.0007,10), '_':(0.1928,2)
}


def is_sequence(arg):
    return (not hasattr(arg, "strip") and
            hasattr(arg, "__getitem__") or
            hasattr(arg, "__iter__"))

def round(f,n):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if is_sequence(f):
        return [round(x,n) for x in f]

def log2(x): return log(x)/log(2)

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