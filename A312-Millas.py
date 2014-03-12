# A312x: kick off file for A312

#pypath="d:/Docencia/2014/py/"
pypath="/home/nuxe/pyzo2013c/CDI"

# Add pypath to path
import sys
sys.path.append(pypath)

# Data from the Morse code, and utilities
from A312h import *

# Compute the weighted average (mean) length of the Morse codes (without space)
# Write expressiona that yield the list of those lengths in the alphabetical order

AZ = sorted(M.keys())
L = [sum(M[x]) for x in AZ]

# Write expressions that yield the probabilities of charaters from the frequencies

W = [F[x] for x in AZ]
S = sum(W)
P = [w/S for w in W]
print(round(P,3))

R = range(len(P))

# Write an expression that yields the weighted average (mean) length

ell = sum([P[j] * L[j] for j in R])
print(round(ell,3))

# Write an expression that yields the variance

sigma2 = sum([P[j] * (L[j]-ell)**2 for j in R])
print(round(sigma2,3))