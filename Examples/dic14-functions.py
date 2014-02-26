# Help file for DIC14 Python Programming: functions
 
'''
We want to convert angle values in degrees to angle values
in radians, and conversely. For example, 90º -> pi/2.
This can be done by defining suitable functions
'''
from math import pi
def deg2rad(d): return(d*pi/180)
def rad2deg(r): return(r*180/pi)

print(deg2rad(90), pi/2)
print(rad2deg(0.7853981633974483), 45)

'''
Functions can have any number of parameters. 
Here is, for example, a function that computes
the probability that in N runs of a random
experiment an event with probability p occurs
at least once:
'''
def at_least_once_in(N,p): return(1-(1-p)**N)

f = at_least_once_in

print(f(4,1/6), f(24,1/36), f(25,1/36))


#Anonymous functions can be defined as lambda expressions
g = lambda N, p: 1-(1-p)**N

p=1/36
print(g(24,p), g(25,p), g(26,p))
