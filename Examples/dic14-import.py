ç# Help file for DIC14 Python Programming: import 
'''
One way to use math constants and functions 
is to import them from the math module.
'''
import math
print(math.pi)

'''
If you want to use pi instead of math.py
it can be done as follows:
'''
from math import pi
print(pi**2)

'''
To use all the functions and constants in the math module
with the same names declared there, proceed as follows:
'''
from math import *
print(e**5)
print(log(e))
print(tan(pi/4))
print(atan(1))
