# L312x
pypath="d:/Docencia/2014/py/"

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
# add suitable expressions to check this


print('Conclude: entropy is higher if we include space\n')


# Test on EN and EN_ entropies

print('Probabilities increase, when we drop the space,')
print('but they are in the INCREASING part of h(p):')
# add suitable expressions to check this


print('Entropy terms h(p) are higher without space:')
# add suitable expressions to check this


print('Difference of the sums of the h(p) terms for non-space characters')
print('without space and with space, respectively:')
# add a suitable expression to check this


print('h(p) term in entropy with space of the space charater:')
# add a suitable expression to check this

print('Therefore, the entropy when we include space remains lower than without space')
# add a suitable expression/s to check this
print(entropy(W)-entropy(W_))
