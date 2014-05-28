## L528 : RGB images
import matplotlib.pyplot as plt
import matplotlib.image as Im
import numpy as np

# Synonyms
load = Im.imread
view = plt.imshow
canvas = plt.figure
array = np.array
matrix= np.matrix
cp = np.copy

pngpath = '/home/nuxe/pyzo2013c/CDI/png/'

def load(f): return Im.imread(pngpath + f + '.png')


x=load('lena') # load your favorite color image 

## 1. Extract the red, green and blue components
# red component
xr = cp(x); xr[:,:,[1,2]]=0

# green component
xg = cp(x); xg[:,:,[0,2]]=0

# blue component
xb = cp(x); xb[:,:,[0,1]]=0

plt.close('all')

Original = 'Original color image'
Red = 'Red component'
Green = 'Green component'
Blue = 'Blue component'
Figure='RGB resolution of color'

## 2. View the original image 
##    and the R, G, B components
F=plt.figure(Figure, figsize=(14,6))
c11 = F.add_subplot(2,4,1)
plt.axis('off')
c11.set_title(Original)
view(x)

## 3. Find expressions for the C, M, Y components 
##    and view them
c12 = F.add_subplot(2,4,2)
plt.axis('off')
c12.set_title(Red)
view(xr)

c13 = F.add_subplot(2,4,3)
plt.axis('off')
c13.set_title(Green)
view(xg)

c14 = F.add_subplot(2,4,4)
plt.axis('off')
c14.set_title(Blue)
view(xb)

c21 = F.add_subplot(2,4,5)
plt.axis('off')
c21.set_title('R+G+B')
view(xr+xg+xb)

c22 = F.add_subplot(2,4,6)
plt.axis('off')
c22.set_title('B+G')
view(xb+xg)

c23 = F.add_subplot(2,4,7)
plt.axis('off')
c23.set_title('R+B')
view(xr+xb)

c24 = F.add_subplot(2,4,8)
plt.axis('off')
c24.set_title('R+G')
view(xr+xg)


# To round a float to n decimal places. It also works
# for a list or a matrix of floats.
def roundfloat(f,nd=4): return float("%.*f" % (nd,f))
def roundmatrix(f,nd=4): 
    r,c = f.shape
    return matrix( [[roundfloat(f[i,j],nd) for j in range(c)] for i in range(r)] )
def round(f,nd=4):
    if isinstance(f,int): return float(f)
    if isinstance(f,float): return roundfloat(f,nd)
    if isinstance(f,list) and not isinstance(f[0],list): return [roundfloat(t,nd) for t in f]
    if isinstance(f,matrix): return roundmatrix(f,nd)
    #if (not hasattr(f, "strip") and hasattr(f, "__getitem__") or hasattr(f, "__iter__")):
    #    return [round(x,nd) for x in f]
    return 'round: unknown type for rounding'