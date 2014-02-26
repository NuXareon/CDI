# Help file for DIC14 Python Programming: user modules

# biltin module
from math import pi
def deg2rad(d): return(d*pi/180)
def rad2deg(r): return(r*180/pi)


# Updating the path
import sys

#print(sys.path)
sys.path.append("d:/Docencia/2014/py/")
#print(sys.path)

# own module
from dic14 import *

print(subset(range(4),range(5)))



