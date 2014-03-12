# L312x
pypath="d:/Docencia/2014/py/"
#pypath="/home/nuxe/pyzo2013c/CDI"

# Add pypath to path
import sys
sys.path.append(pypath)

# Import suitable utilities 
from L312h import *

# Morse frequencies
w1, w2, w3 = MF
w = sum(MF)

# Tests on Morse entropies
print('Probabilities increase, when we drop the space,')
print('and they are in the DECREASING part of h(p):')

print(round([w1/w,w2/w],3))
print(round([w1/(w-w3),w2/(w-w3)],3))

print(round([h(w1/w),h(w2/w)],3))
print(round([h(w1/(w-w3)),h(w2/(w-w3))],3))

print('Conclude: entropy is higher if we include space\n')


# Test on EN and EN_ entropies

print('Probabilities increase, when we drop the space,')
print('but they are in the INCREASING part of h(p):')

print(round(W_,3))
print(round(W,3))

HW_ = [h(p) for p in W_[:len(W_)-1]]
HW = [h(p) for p in W[:len(W_)-1]]
print(round(HW_,3))
print(round(HW,3))

print('\nEntropy terms h(p) are higher without space:\n')

print('Difference of the sums of the h(p) terms for non-space characters')
print('without space and with space, respectively:')

print(round(sum(HW)-sum(HW_),3))

print('\nh(p) term in entropy with space of the space charater:')

print('Therefore, the entropy when we include space remains lower than without space')

print(round(entropy(W)-entropy(W_),3))
print(round(h(w_),3))
