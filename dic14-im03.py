## dic14-im02.py : importing and displaying py predefined images
## SXD 520
import pylab
from scipy import misc

# Synonyms
show = pylab.show()
load = pylab.imshow
Ascent = misc.ascent()
Lena = misc.lena()
Face = misc.face('L')
gray = pylab.gray()  

im = Ascent


load(im,cmap=gray)

show
