## L423h : header file for L423
import numpy as np
import matplotlib.pyplot as plt

# Basic constants
r2 = np.sqrt(2)
a1 = a2 = 1/r2
nd = 4

# Synonyms
Id = np.eye
array = np.array
stack = np.vstack
plot  = plt.plot
show  = plt.show()
dot = np.dot


# Utility functions
def round(f,n=nd):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if (not hasattr(f, "strip") and hasattr(f, "__getitem__") or hasattr(f, "__iter__")):
        return [round(x,n) for x in f]

# Cosmetics
import pprint
_p = pprint.PrettyPrinter()

def disp(f,n=nd): return(_p.pprint(round(f,n)))