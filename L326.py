# L326. Interval encoder

# import header
#pypath = 'D:/Docencia/2014/py'
pypath = '/home/nuxe/pyzo2013c/CDI'

import sys
sys.path.append(pypath)
from L326h import *  # accumulate, IE, 


## Examples IE

# Example 1
P=[('a',0.2), ('b',0.5), ('c',0.3)]
M='babc'
C= IE(M, P)
print(M,'==>', round(C,5))

# Example 2
Q=[('a', 0.25), ('b', 0.4), ('c', 0.15), ('d', 0.1), ('e', 0.1)]
M='badbbdcbabea'
C=IE(M, Q)
print(M,'==>', round(C,10))

## Examples dec2bin and bin2dec

x = 0.5555
xb = dec2bin(x)
xb10 = dec2bin(x,10)
xb20 = dec2bin(x,20)

print("Bit encodings of",x,": ", (xb10,xb20, xb))
print("get back decimal number:",bin2dec(xb10),bin2dec(xb20),bin2dec(xb))

## Examples BE

a=0.5555; b = a + 0.000011
ab = BE(a,b)
print("BE of [",a,',',b,') = ',ab,sep='')

## Examples AE

# Example 1
P=[('a',0.2), ('b',0.5), ('c',0.3)]
M='babc'
x= AE(M, P,15)
print(M,'==>', x)

# Example 2
Q=[('a', 0.25), ('b', 0.4), ('c', 0.15), ('d', 0.1), ('e', 0.1)]
M='badbbdcbabea'
y=AE(M, Q)
print(M,'==>', y)

## Examples AD

# Example 1
print(x,"==>",AD(x,P))

# Example 2
print(y,"==>",AD(y,Q))