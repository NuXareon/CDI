# A319x

pypath = 'D:/Docencia/2014/py'
import sys
sys.path.append(pypath)

#TODO
# 2. Which of the following ...
print('kraft(L1) =',kraft(L1))

# 3. If we want to add binary words of length 5 to {0,10,110}, 
# what is the max-imum number if it is required that the final 
# list is a prefix code?
L = [1,2,3]
while kraft(L): L += [5]
print('L =',L) #[1,2,3,5,5,5,5,5]
print('The number is:',len(L)-1-3) #4

# 4. Write a function K(L,r) ...
print('K([1,2,3],5) =', K([1,2,3],5)) #4

# 5. Find the values ...
L5 = [1,1,2,2,3,3,3]
print('kraft(L5, 3) =', kraft(L5,3)) #true


# 6. . Construct a 5-ary prefix code with lengths ...
L7 = [1,1,1,1,2,2,2,3,3,4]

# 7. Write a function M(L,r) ...

print('M(L7,5) =', M(L7,5)) #2



