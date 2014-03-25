# L325h: head file for L325

# cartesian(X,Y)
# def cartesian(X,Y):
#    return sorted({str(x)+str(y) for x in X for y in Y})

def cartesian(X,C):
    if not C:
        return sorted({str(x) for x in X})
    if not X:
        return sorted({str(c) for c in C})
    return sorted({str(x)+str(c) for x in X for c in C})

# Define a function ells2ens(L) that transforms a list of lenghts 
# to a table with their frequencies

def ells2ens(L): return {l : L.count(l) for l in range(1,1+max(L))}