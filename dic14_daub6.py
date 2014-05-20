## dic14_daub6x: Kick off for dic14_daub6
## SXD 514

import numpy as np
import matplotlib.pyplot as plt

# Synonyms
Id = np.eye
sqrt = np.sqrt
array = np.array
stack = np.vstack
splice= np.hstack
dot = np.dot
ls  = np.linspace
zeros=np.zeros


# Basic constants
nd = 4
a1=0.332670552950083
a2=0.806891509311092
a3=0.459877502118491
a4=-0.135011020010255
a5=-0.0854412738820267
a6=0.0352262918857095

a=[a1,a2,a3,a4,a5,a6]

b=[b1,b2,b3,b4,b5,b6]=[a6,-a5,a4,-a3,a2,-a1]

'''
I) D6trend, D6fluct, D6 
(adapt D4trend, D4fluct, D4 from dic14_daub4.py)
'''




'''
II) Daub6 scaling and wavelet arrays
(adapt D4V, D4W, D4VW from dic14_daub4.py)
'''



'''
Auxiliary functions work the same way
'''

# Orthogonal projection in orthonormal basis
def proj(f,V):
    x = zeros(len(V[0]))
    for v in V:
        x = x + dot(f,v)*v
    return x  

# Projection coefficients
def proj_coeffs(f,V):
    return array([dot(f,v) for v in V])


# Annex: Utility functions
def round(f,n=nd):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if (not hasattr(f, "strip") and hasattr(f, "__getitem__") or hasattr(f, "__iter__")):
        return [round(x,n) for x in f]
        
# Cosmetics
import pprint
_p = pprint.PrettyPrinter()

def disp(f,n=nd): return(_p.pprint(round(f,n)))