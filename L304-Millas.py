from math import log

def log2(x): return np.log(x)/np.log(2)

def entropy(w):
    h = 0
    for t in w:
        h -= t*log2(t)
    s = sum(w)
    h += s*log2(s)
    return h/s    
    

n = 22
r = 7
b = 5
g = 10
bag = [r,g,b]

p = [[p*q for q in bag] for p in bag]

A = bag
B = bag
print('entropy(A): ', entropy(A))
print('entropy(B): ', entropy(B))
print('entropy(A) + entropy(B) = ', entropy(A)+entropy(B))
print('entropy(AB):', entropy([r*r,r*g,r*b,g*r,g*g,g*b,b*r,b*g,b*b]))