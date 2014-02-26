# Help file for DIC14 Python Programming: lists
 
'''
Lists in Python are sequences of objects delimited by brackets
'''
F=[1,1,2,3,5,8,13,21] # the first 8 Fibonacci numbers

'''
If a list L has n values, they are indexed by k = 0,1,...,n-1
and the k-th value is given by L[k].
If k<0 or k>n-1, L[k] produces an error: "list index out of range".
Extraction can also be done in a range, like 1:7 <-> 1,...,6
'''
print(F[0],F[7])
print(F[1:7])

'''
The list of integers from a to b-1 can be construted
using range(a,b)
'''
R = range(-5,6)
L = list(R)
print(L)

# The values of R can also be extracted
print(R[5])

'''
range(a,b,d) makes a virtual list of the values a, a+d, a+2d, ...
insofar as they in the interval [a,b) 
'''
R=range(5,-6,-3)
L=list(R)
print(L)

# Strings work as lists with respect to extraction
V = "aeiouAEIOU"
print(V[5])


#The operation + concatenates lists
print(F+F)
print(2*F)
print(F*2)
print(F+L+F)

'''
The most powerful list constructors is by using
functions or filters on given lists or ranges.
Some examples should suffice for the moment
'''
L = [x**3 for x in range(101,106)]
print(L)

def odd(n): 
    if n%2: return True 
    else: return False

Lodd = [x for x in L if odd(x)]
print("Lodd =", Lodd)

#Lodd2 = filter(odd,L)
#print("Lodd2 =", Lodd2)

#X = map(odd, L)
#print("X =",X) 

P=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print("P =",P)



'''
If L and M are lists, and x a value, then we have also the following
constructions:
'''
#  L.append(x)       # x is appended at the end of L; same as L+[x]
#  L.extend(M)       # same a L+M
#  L.insert(i, x)    # insert x at position i of L
#  L.remove(x)       # removes the first occurrence of x in L; error if it does not occur
#  L.pop([i])        # removes i-th item from L and returns its value
#  L.index(x)        # index of first occurrence of x in L; error if it does not occur
#  L.count(x)        # number of times x appears in L
#  L.reverse()       # reverses the list L
#  L.sort()          # sorts the elements of L






