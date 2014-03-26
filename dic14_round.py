# dic14_round

def is_sequence(arg):
    return (not hasattr(arg, "strip") and
            hasattr(arg, "__getitem__") or
            hasattr(arg, "__iter__"))

def round(f,n):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if is_sequence(f):
        return [round(x,n) for x in f]
