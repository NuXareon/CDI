#Variable lenght encoding
eOld = {'a' : '000', 'b' : '001', 'c' : '010', 'd' : '011', 'e' : '100'}
e = {'a' : '00', 'b' : '01', 'c' : '10', 'd' : '110', 'e' : '111'}

#Coding function
def E(m,e):
    M = ''
    for t in m:
        M += e[t]
    return M
    
#Utility function
def invert(e): return {e[t]: t for t in e}

#Decoding function
def D(m,e):
    d = invert(e)
    keys = d.keys()
    M=''
    lMax = max([len(k) for k in keys])
    lMin = min([len(k) for k in keys])
    while len(m) >= 2:
        for i in range(lMin,lMax+1):
            x = m[:i] #extrea les i primeros bits de M
            if x not in keys: continue
            else:
                M += d[x]
                m = m[i:] #quita los i primeros bits
                break
        if (x not in keys): 
            print("WARNING: Invalid codification: ",x)
            break
    if(len(m) > 0): print("WARNING: Message partially decoded, missing decoding string: ",m)
    return(M)
    
m1 = 'aaabccedabdb'
m2 = 'bbdaceed'
me1 = E(m1,e)
me2 = E(m2,e)
    
print(m1,' encoded: ',E(m1,e),' lenght = ',len(E(m1,e)))
print(m1,' encoded w\ old encoding: ',E(m1,eOld),' lenght = ',len(E(m1,eOld)))
print(me1,' decoded: ',D(me1,e))
print(m2,' encoded: ',E(m2,e),' lenght = ',len(E(m2,e)))
print(m2,' encoded: w\ old encoding: ',E(m2,eOld),' lenght = ',len(E(m2,eOld)))
print(me2,' decoded: ',D(me2,e))
print('0111111 decoded: ',D('0111111',eOld))