#Default: binary.

def kraft_sum(L,r=2):
    return sum([1/r**l for l in L])
    
def kraft_defect(L, r=2):
    return 1-kraft_sum(L, r)
    
def kraft(L, r=2):
    return kraft_sum(L,r)<=1
    
def K(L, l, r=2):
    n = len(L)
    while kraft(L,r): L += [l]
    return len(L)-1-n
    
def M(L, r=2):
    l = 1
    while (l <= max(L)):
        if kraft(L+[l],r): return l
        else: l += 1
    return 0