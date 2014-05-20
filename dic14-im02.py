## dic14-im04 : Other tricks for image generation and saving.
from numpy import random
import matplotlib.pyplot as plt
import numpy as np


# data
pngpath = '/home/nuxe/pyzo2013c/CDI/png'
color='hot'
color='gray'
s = (14,14)

# Get a random array of shape s
def rand(s): return random.random(s)
def view(A): return plt.imshow(A,interpolation='nearest')
def save(f): return plt.savefig(pngpath + f + '.png', bbox_inches='tight')

I = rand(s)
plt.figure('rand'+str(s[0])+color)
plt.axes([0,0,1,1])
plt.axis('off')
F = view(I)
F.set_cmap(color)
save('rand'+str(s[0])+color)



n=16
data = np.arange(n**2).reshape((n, n))
fig = plt.figure('64 gray levels in a row')
fig.set_size_inches(3, 3)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
plt.set_cmap('gray')
#ax.imshow(data, aspect = 'normal')
ax.imshow(data, interpolation='nearest')
plt.savefig(pngpath+color+'squares.png', dpi = 80)

