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

def addtwomethod1(A,tot):
    A=sorted(A)
    n = len(A)
    L = 0
    R = n-1
    a1 = []
    a2 = []
    newlist = []
    while L < R:
        if (A[L]+A[R] == tot):
            a1.append(A[L])
            a2.append(A[R])
            L=L+1
            R=R-1
        elif (A[L]+A[R] < tot):
            L=L+1  
        elif (A[L]+A[R] > tot):
            R=R-1  
    print("# The pairs that add up to",tot,":")    
    for x,y in zip(a1,a2):
        print("# (",x,",",y,")")
    if len(a1) == 0:
        print("# None")    
                
def addtwomethod2(A,tot):
    hset = set()
    for i in range(0, len(A)):
        test = tot-A[i]
        if test in hset:
            print("# Pair is",A[i],test,"for sum:",tot)
            return
        hset.add(A[i])    
    print("# No pairs that add up to",tot)          
                
#a few examples:
thelist = [4,2,8,0,1,-2,9,13445,1,4,3,6,6];
#thelist = random.sample(range(0, 1000000), 1000000)
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
