#python chal3.py

# Running method 1
# ---------------------
# The pairs that add up to 17 :
# ( 8 , 9 )
# The pairs that add up to 12 :
# ( 3 , 9 )
# ( 4 , 8 )
# ( 6 , 6 )
# The pairs that add up to 11 :
# ( 2 , 9 )
# ( 3 , 8 )
# The pairs that add up to 1 :
# ( -2 , 3 )
# ( 0 , 1 )
# The pairs that add up to 19 :
# None
# The pairs that add up to -1 :
# ( -2 , 1 )
# The pairs that add up to 1231233232 :
# None

# Running method 2
# ---------------------
# Pair is 9 8 for sum: 17
# Pair is 8 4 for sum: 12
# Pair is 9 2 for sum: 11
# Pair is 1 0 for sum: 1
# No pairs that add up to 19
# Pair is -2 1 for sum: -1
# No pairs that add up to 1231233232

# -------------------------------------------------------
# The ratio of time it takes of the first method w.r.t. second method= 2.3181818181818183 (using a list of 12 elements)
# The ratio of time it takes of the first method w.r.t. second method= 3.112964509732737 (using a list of 1 million elements)

import time
import random

#define the function
def addtwomethod1(A,tot):
    A=sorted(A) #sort the list A
    n = len(A) #n = number of elements in A
    L = 0 #index of the first element of A
    R = n-1 #index of the last element of A
    a1 = []
    a2 = []
    while L < R: #scan the elements of A 
        if (A[L]+A[R] == tot): # the condition for the two elements of the list adding up to the desired value (tot)
            a1.append(A[L]) #add one element of the pair that meets the condition to the list a1
            a2.append(A[R]) #add other element of the pair that meets the condition to the list a2
            L=L+1 #to scan the next element
            R=R-1 #to scan the next element
        elif (A[L]+A[R] < tot): #when condition is not satistified like this increment L to scan the next element
            L=L+1  
        elif (A[L]+A[R] > tot): #when condition is not satistified like this decrement R to scan the next element
            R=R-1  
    print("# The pairs that add up to",tot,":")    
    for x,y in zip(a1,a2): # zip pairs the elements in a1 and a2 (this is just for conveniently printing) 
        print("# (",x,",",y,")")
    if len(a1) == 0:
        print("# None")    
                
def addtwomethod2(A,tot):
    #create empty set
    hset = set()
    for i in range(0, len(A)): # loop over elements of the list A
        test = tot-A[i] # candidate number to be tested for existence in A
        if test in hset: 
            print("# Pair is",A[i],test,"for sum:",tot) # resulting pair is {A[i], sum-A[i]}
            return
        hset.add(A[i]) #add the corresponding element A[i] to hset    
    print("# No pairs that add up to",tot)          
                
#a few examples:
thelist = [4,2,8,0,1,-2,9,13445,1,4,3,6,6];
#thelist = random.sample(range(0, 1000000), 1000000) # <--- to get a much larger list quickly
print("# Running method 1")
print("# ---------------------")
start1 = time.time()
addtwomethod1(thelist,17)
addtwomethod1(thelist,12)
addtwomethod1(thelist,11)
addtwomethod1(thelist,1)
addtwomethod1(thelist,19)
addtwomethod1(thelist,-1)
addtwomethod1(thelist,1231233232)
end1 = time.time()
time1 = end1-start1
print()
print("# Running method 2")
print("# ---------------------")
start2 = time.time()
addtwomethod2(thelist,17)
addtwomethod2(thelist,12)
addtwomethod2(thelist,11)
addtwomethod2(thelist,1)
addtwomethod2(thelist,19)
addtwomethod2(thelist,-1)
addtwomethod2(thelist,1231233232)
end2 = time.time()
time2 = end2-start2
print()
print("# -------------------------------------------------------")
print("# The ratio of time it takes of the first method w.r.t. second method=",(time1/time2))
