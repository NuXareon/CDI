# A312h: data and utilities for A312


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


# Table constructed with the data on page 2 of A312.pdf
# To .eEach character, including '_' (space), we associate
# the pair (p,c), where p is its probability and c its binary code string
# The name T for the table is chosen for simplicity and following
# a similar criterion than for the two preceding tables
T={
'a':  (0.0575, '0000'),
'b':  (0.0128, '001000'),
'c':  (0.0263, '00101'),
'd':  (0.0285, '10000'),
'e':  (0.0913, '1100'),
'f':  (0.0173, '111000'),
'g':  (0.0133, '001001'),
'h':  (0.0313, '10001'),
'i':  (0.0599, '1001'),
'j':  (0.0006, '1101000000'),
'k':  (0.0084, '1010000'),
'l':  (0.0335, '11101'),
'm':  (0.0235, '110101'),
'n':  (0.0596, '0001'),
'o':  (0.0689, '1011'),
'p':  (0.0192, '111001'),
'q':  (0.0008, '110100001'),
'r':  (0.0508, '11011'),
's':  (0.0567, '0011'),
't':  (0.0706, '1111'),
'u':  (0.0334, '10101'),
'v':  (0.0069, '11010001'),
'w':  (0.0119, '1101001'),
'x':  (0.0073, '1010001'),
'y':  (0.0164, '101001'),
'z':  (0.0007, '1101000001'),
'_':  (0.1928, '01')
}


from numpy import *
from math import log

def log2(x): return log(x)/log(2)


def is_sequence(arg):
    return (not hasattr(arg, "strip") and
            hasattr(arg, "__getitem__") or
            hasattr(arg, "__iter__"))

def round(f,n):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if is_sequence(f):
        return [round(x,n) for x in f]

