# A326x: kick off A326
# A suboptimal encoding based on L325

# import header
pypath = 'D:/Docencia/2014/py'
import sys
sys.path.append(pypath)
from A326h import *
    
T={
'a':  (0.0575, '0000'),
'b':  (0.0128, '001000'),
'c':  (0.0263, '00101'),
'd':  (0.0285, '10000'),
'e':  (0.0913, '1100'),
'f':  (0.0173, '111000'),
'g':  (0.0133, '001001'),
'h':  (0.0313, '10001'),
'i':  (0.0599, '1001'),
'j':  (0.0006, '1101000000'),
'k':  (0.0084, '1010000'),
'l':  (0.0335, '11101'),
'm':  (0.0235, '110101'),
'n':  (0.0596, '0001'),
'o':  (0.0689, '1011'),
'p':  (0.0192, '111001'),
'q':  (0.0008, '110100001'),
'r':  (0.0508, '11011'),
's':  (0.0567, '0011'),
't':  (0.0706, '1111'),
'u':  (0.0334, '10101'),
'v':  (0.0069, '11010001'),
'w':  (0.0119, '1101001'),
'x':  (0.0073, '1010001'),
'y':  (0.0164, '101001'),
'z':  (0.0007, '1101000001'),
'_':  (0.1928, '01')
}

AZ = sorted(list(T.keys()))

P = [T[j][0] for j in AZ]

# P now contains probabilities in decreasing order
P=reverse(sorted(P))

X = make_code_list(P)

'''Now we have to pair characters with probabilities
   in decreasing order with the codes in X, whose lengths
   are non decreading.
   Hint: make a table whose rows have the form (p:c), where
     p is in P and c is the corresponding character
   Compute the mean length ell2 of the resulting encoding.
   Note that it should be <1+H.
   Remember that the mean length of the Huffman encoding
   was found to be 4.146
   '''
   


