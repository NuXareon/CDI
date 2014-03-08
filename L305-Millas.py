# L305 / See InClassLab
import sys
sys.path.append("/home/nuxe/pyzo2013c/CDI/Solutions")
from A305h import *

r = 7; g = 5; b = 10; a=32; y=10
U = [r, g, b, a, y]

# Assumption: 1st marble is not returned
def JP2(U): # should yield the joint distribution matrix
    P = []
    n = sum(U)
    for j in range(len(U)):
        c = U[j]
        p = U[:]
        p[j] -= 1
        p = [c/n * k/(n-1) for k in p]
        P.append(p)
    return P

P = JP2(U)

print(P)

A = row_marginal(P)
B = col_marginal(P)

HA = entropy(A)
HB = entropy(B)
HAB = joint_entropy(P)

print('H(A) =', HA)
print('H(B) =', HB)
print('H(A,B) =', HAB)

print ('HA+HB-HAB =', HA+HB-HAB)





