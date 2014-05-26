## dic14-im03 : loading arbitrary (png) images
import matplotlib.pyplot as plt
import matplotlib.image as Im
import numpy as np

# Synonyms
load = Im.imread
view = plt.imshow
pngpath = 'D:/Docencia/2014/png/'
canvas = plt.figure
array = np.array

def load(f): return Im.imread(pngpath + f + '.png')

mosquito=load('stinkbug')
x=load('X')
y=load('Y')

canvas("Mosquito")
plt.axis('off')
view(mosquito)

canvas("Gray Hecatoicosachoron")
plt.axis('off')
view(x)

canvas("Color Hecatoicosachoron")
plt.axis('off')
view(y)

# dedimante y 
r,c,s = y.shape
yd = np.zeros([r//2,c//2,3])

for i in range(r//2):
    for j in range(c//2):
        for k in range(s-1):
            yd[i,j,k]= y[2*i, 2*j,k]

canvas("Decimated Y")
plt.axis('off')
view(yd)
