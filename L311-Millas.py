# L311: Entropy of Morse coding

import sys
sys.path.append("d:/Docencia/2014/py/")
sys.path.append("C:/Users/nuXe/Documents/GitHub/CDI")
sys.path.append("/home/nuxe/pyzo2013c/CDI")
from A305h import *

# Frequencies of characters
F={'a': 651738, 'b': 124248, 'c': 217339, 'd': 349835, 'e':1041442, 'f': 197881, 'g': 158610, 
   'h': 492888, 'i': 558094, 'j':   9033, 'k':  50529, 'l': 331490, 'm': 202124, 'n': 564513, 
   'o': 596302, 'p': 137645, 'q':   8606, 'r': 497563, 's': 515760, 't': 729357, 'u': 225134, 
   'v':  82903, 'w': 171272, 'x':  13692, 'y': 145984, 'z':   7836, '_': 1918182}

# MorseCode (dot,dash) denotes number of dots and number of dashes in each character
M = {
'a':(1,1), 'b':(3,1), 'c':(2,2), 'd':(2,1), 'e':(1,0), 'f':(3,1), 
'g':(1,2), 'h':(4,0), 'i':(2,0), 'j':(1,3), 'k':(1,2), 'l':(3,1), 
'm':(0,2), 'n':(1,1), 'o':(0,3), 'p':(2,2), 'q':(1,3), 'r':(2,1), 
's':(3,0), 't':(0,1), 'u':(2,1), 'v':(3,1), 'w':(1,2), 'x':(2,2), 
'y':(1,3), 'z':(2,2)
}

f_space = F['_']

f_dot = sum([F[x]*M[x][0] for x in M])

f_dash = sum([F[x]*M[x][1] for x in M])

MF = [f_dash,f_dot,f_space]

entropy1 = entropy(MF)

entropy2 = entropy(MF[:2])

print("Frequency of dot = ", f_dot)
print("Frequency of dash = ", f_dash)
print("Entropy of [f_space,f_dot,f_dash] = ", entropy1)
print("Entropy of [f_dot,f_dash] = ", entropy2)