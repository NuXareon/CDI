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

plt.close()
plt.close()

x = np.arange(0.0,1.0,0.0001)

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

fig = plt.figure(figsize=(10,10))

plt.xlim(-0.1,1.2)
plt.ylim(-0.1,1.2)

plt.plot(x ,-x*log2(x)-(1-x)*log2(1-x), lw=3, color='black')

hline(0,1.05,0)
vline(0,1.05,0)

p = 0.5

hline(0,p,-p*log2(p)-(1-p)*log2(1-p))
vline(0,-p*log2(p)-(1-p)*log2(1-p),p,dash='k--')

plt.show()