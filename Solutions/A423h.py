## A423h : headar for A423
## 428 SXD

import numpy as np

# Cosmetic functions
def round(f,n=5):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if (not hasattr(f, "strip") and hasattr(f, "__getitem__") or hasattr(f, "__iter__")):
        return [round(x,n) for x in f]

import pprint
_p = pprint.PrettyPrinter()

def disp(f,n=5): return(_p.pprint(round(f,n)))

def precision(k=5): return np.set_printoptions(precision=k)
precision()