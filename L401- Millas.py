## L401x: Kick off file for L401

'''
Define the following functions:

1. decimate(f), that returns, given a sequence (list, tuple, …), 
the list formed with its odd-numbered indices.


2. average(f), that gives the average value of a numerical sequence f.


3. energy(f), that yields, if f is numerical sequence, the sum of its squares 
(this was already used in the context of computing variances).


4. sample(h,N,a=0,b=1), that returns, given a function h, 
   a positive integer N and real numbers a and b, a < b, 
   the list of values h(a+j*s) for j in range(N+1), where s=(b-a)/N.
   
Add suitable tests and comments.
'''

def decimate(f): return[f[j] for j in range(1,len(f),2)]

def average(f): return sum(f)/len(f)

def energy(f): return sum([x**2 for x in f])

def sample(h,N,a=0,b=1):
    s = (b-a)/N
    return [h(a+j*s) for j in range(N+1)]

def h(t): return t**2 + 2*t -t**3

a = [1,1,2,3,5,8,13]
print("a: ", a)
print("decimate(a): ", decimate(a))
print("average(a): ", average(a))
print("energy(a): ", energy(a))
print("h(t): -t**3 + t**2 + 2*t")
print("sample(h,10,-2,3): ", sample(h,10,-2,3))