# A319

# 1. Define functions
#    kraft_sum(L,r),
#    kraft_deffect(L,r), and
#    kraft(L,r)

'''Note that r=2 allows calls with one parameter, L, 
   in which case the default value of the second paramter is 2, 
   and calls with two parameters, L and r. 
   As said in class, no check is included 
   on the properties of L and r, as the calls will garantee 
   that L is a list of positive integers
   and r and integer >= 2.'''

def kraft_sum(L,r=2): return sum (r**-l for l in L)
#    
def kraft_deffect(L,r=2): return 1-kraft_sum(L,r)
#
def kraft(L,r=2): return kraft_sum(L,r) <= 1
    
    
    
# 2. Which of the following lists can be the lengths 
#    of a prefix binary code?

L1 = [1,2,3,3]
L2 = [1,2,2,3,3]
L3 = [1,3,3,3,4,4]
L4 = [2,2,3,3,4,4,5,5]

# aux function
def check2(L,r=2): 
    if kraft(L,r): return 'Yes'
    else: return 'No'
# aux list   
L=[L1,L2,L3,L4]

print()
for i in range(1,5):
    print('Does L'+str(i)+' satisfy the condition?',check2(L[i-1]))
print()


# 3. If we want to add binary words of length 5 to {0,10,110}, 
#    what is the maximum number if it is required that the final list 
#    is a prefix code?

# Lists of lengths
L = [1,2,3]
L_ = L[:]
while kraft(L_): L_ += [5]

print('The number is:',len(L_)-1-len(L))
print()


# 4. Write a function K(L,l), where 
#    L is a list of lengths of binary strings and 
#    r is a positive integer, that gives 
#    the maximum number of binary strings of length l 
#    that can be added to a code with word-lengths L 
#    with the requirement that the final list is a prefix code.

def K(L,l): 
    if kraft_sum(L) >= 1: return 0
    else: return int( kraft_deffect(L)*2**l )
'''Note: this expresses how many times 1/2**l 
   fits into kraft_deffect(L)'''

# 5. Find the values of
#      kraft (L5, 3), L5={1,1,2,2,3,3,3};
#      kraft (L6, 5), L6={1,1,1,1,1,8,9}.

L5 = [1,1,2,2,3,3,3]
L6 = [1,1,1,1,1,8,9]

print('Value of kraft(L5, 3):',kraft(L5,3))
print('Value of kraft(L6, 5):',kraft(L6,5))
print()


# 6. Construct a 5-ary prefix code with lengths
L7=[1,1,1,1,2,2,2,3,3,4]

''' Since r = 5, we can take C = {0,1,2,3,4}.
    Our goal is to find 10 C-words that form
    a prefix code and so that n1=4 have length 1,
    n2=3 have length 2, n3=2 have length 3 and 
    n4=1 has length 4.
    For the n1=4 words of length 1 we can take
    any 4 of the 5 that there are. The simplest choice is
    0, 1, 2 and 3 (we omit quotes to have less clutter).
    Since the code has to be prefix, all other words
    must start with 4. Clearly, 40, 41, 42 is a good
    choice for the n2=3 words of length 2. After that,
    all other code words have to start with 43 or 44.
    We can stick to 43, as we have to write only three
    more words and there are 5 starting with 43. So
    430 and 431 may be taken as the n3=2 words of
    length 3. As word of length 4 we may take 4320,
    the first that avoids 430 and 431.
    Conclusion:'''
    
print(['0','1','2','3', '40','41','42', '430','431', '4320'])
print()

'''Note: Making this construction generic with a function
   will be the subject of L325''' 

# 7. Write a function M(L,r), where L and r are as in 1, 
#    that supplies the minimum length that can be added 
#    to L such that the elements of the new list 
#    are the lengths of an r-ary prefix code.

from math import log, floor, ceil
def log2(x): return log(x)/log(2)

def M(L,r=2): 
    S = kraft_sum(L,r)
    if S > 1: return('there is no code to enlarge')
    if S == 1: return('the code cannot be enlarged')
    return ceil(- log2(1-S)/log2(r))


# 8. Among the lists L1−L7 for which Kraft returned True, 
#    which can be enlarged? 
#    For each of these, which is the minimum length 
#    that can be added?

D = [(L1,2),(L2,2),(L3,2),(L4,2), (L5,3), (L6,5), (L7,5)] 

for j in range(1,len(D)+1):
    L = D[j-1][0]; r = D[j-1][1]
    if kraft_sum(L,r) > 1: 
        print('L'+str(j)+' is impossible')
    elif kraft_sum(L,r) == 1:
        print('L'+str(j)+' is possible, but cannot be enlarged')
    else:
        print('L'+str(j)+' can be enlarged;')
        print('   the minimum length that can be added is ', M(L,r))
#L = [ in L if ]



