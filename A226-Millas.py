# dic14 help: plots
import numpy as np
import matplotlib.pyplot as plt
from math import e

def log2(x): return np.log(x)/np.log(2)

def hline(a,b,h,lw=1,dash='k-'):
    x = np.arange(a,b+0.0001,b-a)
    return plt.plot(x,h+0*x,dash, lw=lw)
    
def vline(a,b,d,lw=1, dash='k-'):
    y = np.arange(a,b+0.0001,b-a)
    return plt.plot(d+0*y,y,dash, lw=lw )

x = np.arange(0.12,1.01,0.01)

    
plt.close()

fig=plt.figure(figsize=(3.5,7))

#plt.figure(1)
plt.xlim(-1,1.2)
plt.ylim(-0.2,3.5)

plt.plot(x, -log2(x), lw=2)

hline(0,1.05,0)
vline(0,3.1,0)

hline(0,0.5,1)
vline(0,1,0.5)

p=0.35; q=-log2(p)
hline(0,p,q,dash='g:')
vline(0,q,p,dash='g:')
plt.annotate('$-\log_2(p)$',xy=(p,-log2(p)), xytext=(-0.75,q-0.05), fontsize=16)

#axes.get_xaxis().set_ticks([])
#axes.get_yaxis().set_ticks([])

plt.show()

##############

x = np.arange(0.001,1.001,0.01)

fig = plt.figure(figsize=(10,6))

plt.xlim(-0.1,1.2)
plt.ylim(-0.1,0.7)

plt.plot(x, -x*log2(x), lw=3, color='black')

hline(0,1.05,0)
vline(0,0.65,0)

p = 1/e

vline(0,-p*log2(p),p,dash='k--')
hline(0,0.5,-p*log2(p),dash='k--')

plt.annotate('$-p*\log_2(p)$',xy=(0.8,0.4), xytext=(0.8,0.4), fontsize=16)
plt.annotate('$\log_2(e)/e$ =~ $0.53$',xy=(0.4,0.2), xytext=(0.4,0.2), fontsize=16)
plt.annotate('$1/e$',xy=(p,0), xytext=(0.34,-0.05), fontsize=16)

plt.show()