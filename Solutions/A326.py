# A326
# A suboptimal encoding based on L325 (now subsumed in A326h
# sxd 31/3/2014

# import header
#pypath = 'D:/Docencia/2014/py'
pypath = '/home/nuxe/pyzo2013c/CDI/Solutions'
import sys
sys.path.append(pypath)
from A326h import *

'''
This is extracted from A326.pdf, which provides the context:

1. Construct this encoding for the binary encoding for EN_ 
   by paring decreasing probabilities with increasing code lengths.
   
2. Calculate the mean length and compare it with the mean length 
   of the Huffman encoding. 
   Are the results consistent with Shannon’s source cod-ing theorem?
'''

# Data for EN_ (already used several times in class)
# T is a table whose rows have the form
#    j : (p, w)
# where j is one of the EN_ symbols, p is its probability
# and w is a binary word that was constructed using the
# Huffman algorithm

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

## Here starts the solution 

# AZ is the source alphabet with the usual order 
# ('_', space, will be its first character.
AZ = sorted(list(T.keys()))

# P contains the probabilities of the symbols in AZ
# in the same order
P = [T[j][0] for j in AZ]

#def reverse(X): return [X[j] for j in range(len(X)-1,-1,-1)] 

# X is the list of the binary code-words with lengths
#      l =  ⌈-log2(p)/log2(r)⌉, p in P
# According to A326h, they are ordered so that
# the lengths are non-decreasing 
X = make_code_list(P)

# We construct an auxiliary table Q whose elements
# have the form 
#      p : j
# where j is a source symbole and p is its probability 
# This table contains len(P) elements because the
# probabilities in P are distinct (this can be checked
# with len(set(P)==len(P))
Q={T[j][0]:j for j in AZ}

# Now we order P in decreasing order
P=reverse(sorted(P))

# Now we can complete the encoding C we were after.
# we run through the probabilities p = P[k] in P, using an 
# index k (they will be in decreasing order),
# and at the same time through the code-words w = X[k] 
# (this ensures the lengths will never decrease),
# and find the symbol s = Q[p] corresponding
# to the probability p and form the element
#      s : w
# of C 
C={Q[P[k]]:X[k] for k in range(len(P))}

print("Encoding C =", C)
print()

# Now we can compute the mean length ell_C of C
ell_C = sum (p*len(C[Q[p]]) for p in P)
print("mean length of C = ell_C =",ell_C)
print()

# To compare with the mean length of the Huffman encoding
# let
ell_T = mean_len(T)
#sum( T[j][0]*len(T[j][1]) for j in AZ)
print("mean length of Huffman encoding H = ell_H =",ell_T)
print()

'''
We remember that the entropy of EN_ was H = 4.10.
We again see that ell_T > H (first part of the source
coding theorem). Now we also see that
# ell_C - H = 0.56 <1
# as it should by the second half of that theorem. 
'''