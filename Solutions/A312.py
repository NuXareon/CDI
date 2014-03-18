# A312.py : With complete solution.

#pypath="d:/Docencia/2014/py/"
pypath="/home/nuxe/pyzo2013c/CDI/Solutions"

# Add pypath to path
import sys
sys.path.append(pypath)

# Data from the Morse code, and utilities
from A312h import *


# Since the computations for the Morse case were already studied in class,
# let's ignore them for this version. But of course we will follow a
# similar procedure.

'''
# Compute the weighted average length of the Morse codes (without space)
# Write expressiona that yiel the list of those lengths in the alphabetical order

AZ = sorted(M.keys())

L = [sum(M[x]) for x in AZ]

# Write expressions that yield the probabilities of charaters from the frequencies
W = [F[x] for x in AZ]
S = sum(W)
P = [w/S for w in W]

# Write an expression that yields the weighted average length
ell = sum(P[j]*L[j] for j in range(len(P)))

print('\nMean length of  Morse encoding =', round(ell,4))

# Write an expression that yields the variance
sigma2 = sum(P[j]*(L[j]-ell)**2 for j in range(len(P)))
print('\nLength variance of Morse encoding =', round(sigma2,4))
'''




# ----------------------------------------------------
# The binary encoding for the Latin lowercase alphabet 
# with space is captured in table T of A312h.py: the value
# associated to each character is the pair (p,x) formed with
# its probability p and its binary code string x.


#• Compute its mean length ℓ.
'''
For a row c:(p,x) in table T, T[c] yields (p,x)
and hence T[c][0] is the probability of c
and len(T[c][1]) is the length of its binary encoding.
Thus the mean length ℓ is given by
'''
ell = sum( T[c][0] * len(T[c][1]) for c in T)
print('\nMean length of binary encoding =', round(ell,4))

#• Compare ℓ with the entropy of EN_ (use the probabilities 
#  on that same table or the ones used in previous work).
'''
We use the probabilities in the same table, so the p's
appearing in T. We could copy the entropy function in
A312h (from early work) or just go ahead and compute
it using the formula:
'''
H = 0
for c in T:
    p = T[c][0]
    H -= p * log2(p)
    
print('\nThe entropy of EN_ =', round(H,4))



# • Compute the variance σ^2 of the lengths l_j.
'''
No difficulty here, as the formula is analogous
to the formula for the mean length:
'''
sigma2 = sum( T[c][0] * (len(T[c][1]) - ell)**2 for c in T)
print('\nLength variance of binary encoding =', round(sigma2,4))

# • Compare ℓ and σ^2 with the analogous quantities for the Morse code.
'''
Mean length of  Morse encoding = 2.5362
Length variance of Morse encoding = 1.1248
We see that the mean length is nearly one bit smaller.
Does this mean that the Morse encoding is more efficient
than the binary encoding? For the answer, see L318.
As for the variance, we should of course expect to be smaller
than for the binary encoding, as the range of lengths is
1 to 4, instead of 2 to 10.
'''
print()