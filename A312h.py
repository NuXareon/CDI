# A312h: data and utilities for A312


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


def is_sequence(arg):
    return (not hasattr(arg, "strip") and
            hasattr(arg, "__getitem__") or
            hasattr(arg, "__iter__"))

def round(f,n):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return float("%.*f" % (n,f))
    if is_sequence(f):
        return [round(x,n) for x in f]

