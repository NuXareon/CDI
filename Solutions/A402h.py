## A402h.py / Header file for A402.py

# log2
from math import log
def log2(x): return log(x)/log(2)

# round(f,n)
def round(f,n):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if (not hasattr(f, "strip") and hasattr(f, "__getitem__") or hasattr(f, "__iter__")):
        return [round(x,n) for x in f]


## Data
EN_ =[(0.0575,'a'),
(0.0128,'b'),
(0.0263,'c'),
(0.0285,'d'),
(0.0913,'e'),
(0.0173,'f'),
(0.0133,'g'),
(0.0313,'h'),
(0.0599,'i'),
(0.0006,'j'),
(0.0084,'k'),
(0.0335,'l'),
(0.0235,'m'),
(0.0596,'n'),
(0.0689,'o'),
(0.0192,'p'),
(0.0008,'q'),
(0.0508,'r'),
(0.0567,'s'),
(0.0706,'t'),
(0.0334,'u'),
(0.0069,'v'),
(0.0119,'w'),
(0.0073,'x'),
(0.0164,'y'),
(0.0007,'z'),
(0.1928,'_')]