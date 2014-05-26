## L521x.py : Kick off for L521.py 

from dic14_wavelets_x import *

## 1.
''' L521.1a
    Include examples of haar_matrix 
    (should be an orthogonal)
'''

H4 = haar_matrix(4)
print("haar matrix of size 4: \n", H4)
print("H4*transpose(H4) must be the identity matrix:\n", round(H4*transpose(H4)))

''' L521.1b
    Include examples illustrating that
    i_haar works properly 
'''

y = [1,4.3,10,-3]
Hy = haar(y)
iHy = i_haar(Hy)
print("initial array:", y)
print("haar:", Hy)
print("i_haar: ", iHy)


## 2.
''' L521.2a
    Include examples of daub4_matrix, 
    (should be an orthogonal)
'''

D4M = daub4_matrix(4)
print("daub4 matrix of size 4: \n", D4M)
print("D4*transpose(D4) must be the identity matrix:\n", round(D4M*transpose(D4M)))

''' L521.2b
    Include examples illustrating that
    i_daub4 works properly 
'''

y = [1,4.3,10,-3]
D4y = D4(y)
iD4y = i_daub4(D4y)
print("initial array:", y)
print("haar:", D4y)
print("i_haar: ", iD4y)

## 3.
''' L521.3a
    Include examples of daub6_matrix, 
    (should be an orthogonal)
'''

D6M = daub6_matrix(8)
print("daub6 matrix of size 8: \n", D6M)
print("D6*transpose(D6) must be the identity matrix:\n", round(D6M*transpose(D6M)))

''' L521.3b
    Include examples illustrating that
    i_daub6 works properly 
'''

y = [1,4.3,10,-3,5,6.43,-3.4,9]
D6y = D6(y)
iD6y = i_daub6(D6y)
print("initial array:", y)
print("haar:", D6y)
print("i_haar: ", round(iD6y))
