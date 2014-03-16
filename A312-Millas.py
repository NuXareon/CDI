# A312x: kick off file for A312

pypath="d:/Docencia/2014/py/"
#pypath="/home/nuxe/pyzo2013c/CDI"
#pypath="C:/Users/nuXe/Documents/GitHub/CDI"

# Add pypath to path
import sys
sys.path.append(pypath)

# Data from the Morse code, and utilities
from A312h import *
from A305_EN1 import *

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

ell_2 = sum(ME_[x][0]*ME_[x][1] for x in AZ)
sigma2_2 = sum(ME_[x][0]*(ME_[x][1]-ell_2)**2 for x in AZ)

e1_=entropy(EN_.values())

print("Mean lenght l =",ell_2)
print("Entropy of EN_ =",e1_)
print("By coding each letter of the english alphabet with a diferent number of bits depending of their probability we have reduced the entropy, that means that we need a lower amount of bits to codify an english text thanks to the new codifycation.")
print("Comparing morse and the new encoding:")
print("Mean lenght: morse = ", ell, ", codification = ", ell_2)
print("Variance: morse = ",sigma2, ", codification = ",sigma2_2)
print("We can see from this values that the morse code uses less bits to codify an english text. However, we have to take into acount that the morse code is more time consuming since it uses \"silences\" to represent the end of a character or the space")