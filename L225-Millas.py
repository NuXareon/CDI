#Fixed lenght encoding
e = {'a' : '000', 'b' : '001', 'c' : '010', 'd' : '011', 'e' : '100'}

#Coding function
def C(m):
    M = ''
    for t in m:
        M += e[t]
    return M
    
#Utility function
def invert(e): return {e[t]: t for t in e}

#Fixed lenght decoding
d = invert(e)

#Decoding function
def D(m):
    keys = d.keys()
    M=''
    while len(m) > 2:
        x = m[:3] #extrea les 3 primeros bits de M
        M += d[x]
        m = m[3:] #quita los 3 primeros bits
    return(M)
    
m1 = 'aaabccedabdb'
m2 = 'bbdaceed'
me1 = C(m1)
me2 = C(m2)
    
print(m1,' encoded: ',C(m1))
print(me1,' decoded: ',D(me1))
print(m2,' encoded: ',C(m2))
print(me2,' decoded: ',D(me2))