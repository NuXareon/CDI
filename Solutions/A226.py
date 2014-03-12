# A226

# load A226-h: it enables numpy, pyplot, and utility functions

import sys
sys.path.append("d:/Docencia/2014/py/")
from A226h import *

#  Close all plt windows
plt.close("all")


#---------------
# Graphing h_(p)
#---------------
# Define graphical window
plt.figure("h_(p)", figsize=(6,4))

x = np.arange(0.0001, 1.0, 0.001)
y = h_(x)

plt.plot(x, y,'r-', lw=2)

# range of axis
xmin = -0.1; xmax = 1.1
ymin = -0.1; ymax = 0.6

plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)

# drawing axis through (0,0)
h_max = log2(e_)/e_

hline(0,(1+xmax)/2,0)
vline(0,(h_max+ymax)/2,0)

# Drawing reference elements for maximum
vline(0,h_max,1/e_,dash='g--') 
hline(0,1/e_,h_max,dash='g--') 
plt.plot([1/e_],[0],'go')
plt.plot([1/e_],[h_max],'go')

#Inserting formulas

h_formula = '$-p\,\log_2(p)$'

xh, yh = (1+1/e_)/2, h_max*0.8
plt.text(xh,yh, h_formula, fontsize=16, color='r')

h_max_value = '$\,\log_2(e)/e \simeq 0.53$'
plt.text(1/e_,0.45*h_max, h_max_value, fontsize=16, color='g')
plt.text(1/e_,ymin/2,'$1/e$',fontsize=16, color='g')


#---------------
# Graphing c_(p)
#---------------
# Define graphical window
plt.figure("c_(p)", figsize=(6,6))

x = np.arange(0.0001, 1.0, 0.0001)
y = c_(x)

plt.plot(x, y,'r-', lw=2)

# range of axis
xmin = -0.1; xmax = 1.1
ymin = -0.1; ymax = 1.15

plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)

# drawing axis through (0,0)
c_max = c_(0.5)
hline(xmin,xmax,0)
vline(ymin,ymax,0)

# Drawing reference elements for maximum
vline(0,c_max,0.5,dash='g--') 
hline(0,0.5,c_max,dash='g--') 
plt.plot([0.5],[0],'go')
plt.plot([0.5],[c_max],'go')

#Inserting formulas

c_formula = '$-p\,\log_2(p)-(1-p)\log_2(1-p)$'
xc, yc = 0.15, (c_max+ymax)/2
#plt.text(xc,yc, c_formula, fontsize=16, color='r')

plt.xlabel(c_formula, fontsize=18, color='r')


# show both figures
plt.show()


