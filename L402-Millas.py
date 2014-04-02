def transpose(F):
    m = len(F); n = len(F[0])
    T = []
    for j in range(n):
        c = []
        for i in range(m):
            c += [F[i][j]]
        T += [c]
    return T
        
# trend(f) computes the trend signal of a discrete signal f
def trend(f):
    r=sqrt(2); J = range(len(f)//2)
    return [(f[2*j]+f[2*j+1])/r for j in J]

# fluct(f) computes the fluctuation 
# (or difference) signal of a discrete signal f    
def fluct(f):
    r=sqrt(2); J = range(len(f)//2)
    return [(f[2*j]-f[2*j+1])/r for j in J]

# haar(f,r) computes the Haar transform of f or order r. 
# haar(f) is equivalent to haar(f,1)
def haar(f,r=1): 
    if r==1: return (trend(f)+fluct(f))
    N=len(f); m=N//2**(r-1)
    a=haar(f,r-1); x=a[:m]
    return trend(x)+fluct(x)+a[m:]

def haar2d_rows(F):
    H = []
    for f in F:
        H += [haar(f)]
    return H
    
def haar2d(F):
    H = haar2d_rows(F)
    H = transpose(H)
    H = haar2d_rows(H)
    return transpose(H)
        
F = [
[10,12,13,14],
[17,16,15,14],
[12,11,10,10],
[7,9,11,12]
]

print(F)
print(round(haar2d(F),1))