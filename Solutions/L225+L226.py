#L225+L226
 
# Generic encoding

def E(m,e):
    M = ''
    for t in m:
        M += e[t]
    return M


# Utility function
def invert(e): return {e[t]:t for t in e}

# Generic decoding
def D(M,e):
    d = invert(e)
    keys = d.keys()
    l = max([len(k) for k in keys])
    m = ''
    while M != '':
        for j in range(1,l+1):
            x = M[:j]
            if x not in keys: continue
            else: 
                m += d[x]
                M = M[len(x):]
                break
        if not x in keys: 
            print('L255+L256/D: wrong residual data:', x)
            print('L255+L256/D: decoded message so far:', m)
            return m
    return m

#--------------------------------------------------------
# Fixed length encoding
efix={'a':'000','b':'001', 'c':'010','d':'011','e':'100'}
# Variable length encoding
evar={'a':'00','b':'01', 'c':'10','d':'110','e':'111'}

m = 'aaabccedabdb'

Mfix = E(m,efix)
Mvar = E(m,evar)

print("Mfix has length", len(Mfix))
print("Mvar has length", len(Mvar))

mfix = D(Mfix,efix)
print("Fixed length coding/decoding:", m, mfix)

mvar = D(Mvar,evar)
print("Variable length coding/decoding:", m, mvar)