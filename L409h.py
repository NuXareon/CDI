## L409h: Utilities for L409x and L409
## SXD 409. 

# Version 409. New high_filter and low_filter
from dic14_haar import *

# Utilities for L409
def A_(f,r=1): return round(high_filter(f,r),2)
def D_(f,r=1): return round(low_filter(f,r),2)

def add(x,y): return [x[j]+y[j] for j in range(min(len(x),len(y)))]