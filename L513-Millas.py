## L513x.py : Kick off for L513.py
## SXD 513

''' 1.
With the same conventions as in L507, 
take N=2**10 and plot the D4 scaling vectors 
v_1^5, v_8^5, v_16^5, 
v_1^6, v_4^6, v_8^6  
and the D4 wavelets 
w_1^5, w_8^5, w_16^5, 
w_1^6, w_4^6, w_8^6.
'''
# We need scaling and wavelet vector
from A507h import *

plt.close('all')

# Plot 3 level 5 and 3 level 6 scaling vectors
plt.figure("3 level 5 and 3 level 6 scaling vectors")
h = 3; d = 0.5
for j in [0,7,15]:
    plt.plot( h + V[5][j] )
    h -= d

for j in [0,3,7]:
    plt.plot( h + V[6][j] )
    h -= d


plt.show()

''' 2.
Check (numerically) the identities 
on pages T6.12 and T.13 for the Daub6
coefficients
'''

a1=0.332670552950083
a2=0.806891509311092
a3=0.459877502118491
a4=-0.135011020010255
a5=-0.0854412738820267
a6=0.0352262918857095

# Define b1, ..., b6
a=[a1,a2,a3,a4,a5,a6]
b=[b1,b2,b3,b4,b5,b6]=[a6,-a5,a4,-a3,a2,-a1]

def Z(x):
    if abs(x) > 1/10**14: x=0.0
    return round(x,10)
    
t1 = Z(sum(s**2 for s in a)-1)
t2 = Z(sum(s for s in a)-sqrt(2))
t3 = Z(sum(s for s in b))
t4 = Z(sum(k*b[k] for k in range(6)))
t5 = Z(sum(k**2 * b[k] for k in range(6)))
t6 = Z(sum(a[k]*b[k] for k in range(6)))
print("square sum of a: ", t1)
print("sum of a -sqrt(2): ", t2)
print("square sum of b: ", t3)
print("k*b[k]: ", t4)
print("k**2*b[k]: ", t5)
print("a*b: ", t6)

if (t1 == t2 == t3 == t4 == t5 == t6 == 0): print("tots els resultats son 0, correcte!")








