# L318x

# How many ticks does it take, on the average, to transmit one character 
# using the Morse encoding? 

# We can use the table M in A312h, whose rows have the form
# c : (a, b), where c is a character (including space)
# a is the number of dots and b the number of dashes:

M = {
'a':(1,1), 'b':(3,1), 'c':(2,2), 'd':(2,1), 'e':(1,0), 'f':(3,1), 
'g':(1,2), 'h':(4,0), 'i':(2,0), 'j':(1,3), 'k':(1,2), 'l':(3,1), 
'm':(0,2), 'n':(1,1), 'o':(0,3), 'p':(2,2), 'q':(1,3), 'r':(2,1), 
's':(3,0), 't':(0,1), 'u':(2,1), 'v':(3,1), 'w':(1,2), 'x':(2,2), 
'y':(1,3), 'z':(2,2)
}

# How many ticks does (a,b) represent?

Ticks = {c : M[c][0]+M[c][1]*3+(M[c][0]+M[c][1]-1)*3 for c in M.keys()}

# Ticks should also include 4 ticks for the character '_':

Ticks.update({'_':4})

# Now to compute the mean value of the number of ticks,
# we need a table with the probabilities of EN_. We can use
# the table T of A312h:
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

# Since we only need the probabilities, lets
# construct a table P with them:

P = {c:T[c][0] for c in sorted(T.keys())}    

# Now the computation of the mean number of ticks 
# can proceed as follows:

A = sum([P[c] * Ticks[c] for c in P.keys()])

#...

print('\nAverage number of ticks per character in the Morse encoding:', A)


# Let us also see what are the differencies between the values of Ticks
# and the values of the lengths of the binary encodings:

D = dict()
for c in sorted(P.keys()):
    D.update({c : Ticks[c]-len(T[c][1])})

B = sum([T[c][0] * len(T[c][1]) for c in T.keys()])

C = sum([P[c] * D[c] for c in P.keys()])

print('\nAverage length per character in the binary encoding:', B)

print('\nAverage number of extra ticks per character in the Morse encoding compared to the binary encoding:', C,"\n")

'''
The simplicity of the Morse code is overun by the
time needed to transmit: nearly double ticks than the
binary encoding!!
'''


# Check the inequalities [*_j] on page 6 of T3 
# for the binary encoding used in A312.

def n(j):
    nj = 0
    for c in T.keys():
        if len(T[c][1]) == j:
            nj += 1
    return nj
    
N = [n(j) for j in range(1,11)]

for j in range(1,11):
    e = 2**j - sum([n(k)*2**(j-k) for k in range(1,j)])
    if e < n(j): print("Inequalty fails for ", j)
    else: print("n(",j,") = ",n(j)," <= ",e)
    
M = [2**j - sum([n(k)*2**(j-k) for k in range(1,j)]) for j in range(1,11)]