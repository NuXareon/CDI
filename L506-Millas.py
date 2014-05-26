## A430 : Daubechies wavelets -- preliminairies
## SXD 506 

import numpy as np

# Synonyms
sqrt = np.sqrt
array  = np.array


r2=sqrt(2); r3=sqrt(3);

''' 
Goal: check relations T6.2
'''

d = 4*r2
a1 = (1+r3)/d; a2 = (3+r3)/d; a3 = (3-r3)/d; a4 = (1-r3)/d
D = [a1,a2,a3,a4]

print('a1,a2,a,3,a4: ')
print(D,'\n')

print('a1**2+a2**2+a3**2+a4**2: ')
print(round(a1**2+a2**2+a3**2+a4**2), '\n')

print('a1+a2+a3+a4-r2: ')
print(round(a1+a2+a3+a4-r2), '\n')

print('a1*a3+a2*a4: ')
print(round(a1*a3+a2*a4), '\n')

B = [b1,b2,b3,b4] = [a4,-a3,a2,-a1]

print('sum(B): ') 
print(round(sum(B)),'\n')

print('0*a4-1*a3+2*a2-3*a1: ')
print(round(0*b1+1*b2+2*b3+3*b4), '\n')