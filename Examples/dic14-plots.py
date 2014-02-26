# dic14 help: plots
import numpy as np
import matplotlib.pyplot as plt

def log2(x): return np.log(x)/np.log(2)

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
    
t1 = np.arange(0.0, 5.0, 0.2)
t2 = np.arange(0.0, 5.0, 0.02)

plt.close()

plt.figure("1: two graphs")

plt.subplot(2,1,1)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'g-')

plt.subplot(2,1,2)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.show()

plt.figure("2: annotated graph")
#ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

line, = plt.plot(t, s, lw=2)
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5), \
   arrowprops=dict(facecolor='black', shrink=0.))
plt.ylim(-2,2)
plt.show()

# regular polygons

def reg(N):
    return ([np.cos(2*np.pi*j/N) for j in range(N+1)], \
            [np.sin(2*np.pi*j/N) for j in range(N+1)])


plt.figure("3: Polygons")
# Plot regular polygons with 4, 8, 16, 32 sides
for m in range(6):
    P=reg(2**m)
    plt.plot(P[0],P[1])

plt.show()
