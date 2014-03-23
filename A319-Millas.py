# A319x

pypath = 'D:/Docencia/2014/py'
#pypath = 'C:/Users/nuXe/Documents/GitHub/CDI'
import sys
sys.path.append(pypath)

from A319h_Millas import *

# 2. Which of the following ...
L1 = [1,2,3,3]
L2 = [1,2,2,3,3]
L3 = [1,3,3,3,4,4]
L4 = [2,2,3,3,4,4,5,5]
print('kraft(L1) =',kraft(L1))
print('kraft(L2) =',kraft(L2))
print('kraft(L3) =',kraft(L3))
print('kraft(L4) =',kraft(L4))

# 3. If we want to add binary words of length 5 to {0,10,110}, 
# what is the max-imum number if it is required that the final 
# list is a prefix code?
L = [1,2,3]
while kraft(L): L += [5]
print('L =',L)
print('The number is:',len(L)-1-3) 

# 4. Write a function K(L,r) ...
print('K([1,2,3],5) =', K([1,2,3],5))

# 5. Find the values ...
L5 = [1,1,2,2,3,3,3]
print('kraft(L5, 3) =', kraft(L5,3))
L6 = [1,1,1,1,1,8,9]
print('kraft(L6, 5) =', kraft(L6,5))


# 6. . Construct a 5-ary prefix code with lengths ...
L7 = [1,1,1,1,2,2,2,3,3,4]
L8 = ['1','2','3','4','01','02','03','041','042','0430']
print (L7, ": ", L8)

# 7. Write a function M(L,r) ...

print('M(L7,5) =', M(L7,5))

# 8.
Ln = [(L1,2),(L2,2),(L3,2),(L4,2),(L5,3),(L6,5),(L7,5)]
i = 0

for L in Ln:
    i += 1
    if kraft(L[0], L[1]):
        if M(L[0],L[1]) > 0: print("L%d" % i,":",M(L[0],L[1]))
        else: print("L%d" % i,": Can not be enlarged.")
    else: print("L%d" % i, ": False")


