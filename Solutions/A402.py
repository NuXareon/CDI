#### A402.py  Solution of A402.2 assignement with A402_huffman.py
#pypath = "D:/Docencia/2014/py"
pypath = "C:/Users/nuXe/Documents/GitHub/CDI/Solutions"
import sys
sys.path.append(pypath)

# Import log2 and round
from A402h import *

# Import the file we want to study and test
from A402_huffman import *



## 1.0
HT = make_huffman_tree(EN_)
C = dict()
make_huffman_encoding(HT, C)
#print(C)
#print()


A2P = {a:p for (p,a) in EN_}

T315 = {a:(round(A2P[a],4),round(-log2(A2P[a]),1),len(C[a]), C[a]) for a in C}

# print the table
L = sorted(list(A2P.keys()))
#print(L)
for x in L[1:]: print(tuple(x)+T315[x])
print(tuple(L[0])+T315[L[0]])
print()


## Other examples

L1 = [(1,'A')]
T1=mht(L1)
C1=dict()
mhe(T1,C1)
print(C1)

L2=[(0.4,'A'), (0.6,'B')]
T2 = mht(L2)
C2=dict()
mhe(T2, C2)
print(C2)

L3=[(0.5001,'a'),(0.20,'b'),(0.15,'c'),(0.10,'d'),(0.05,'e')]
T3=mht(L3)
H3 = MHE(T3)
print(H3)

L4=[(0.2,'a'),(0.4,'b'),(0.20001,'c'),(0.100001,'d'),(0.1,'e')]
T4=mht(L4)
H4=MHE(T4)


