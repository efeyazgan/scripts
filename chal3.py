#python chal3.py 
#Running method 1
#---------------------
#The pairs that add up to 17 :
#( 8 , 9 )
#The pairs that add up to 12 :
#( 3 , 9 )
#( 4 , 8 )
#( 4 , 8 )
#( 6 , 6 )
#The pairs that add up to 11 :
#( 2 , 9 )
#( 3 , 8 )
#The pairs that add up to 1 :
#( -2 , 3 )
#( 0 , 1 )
#The pairs that add up to 19 :
#None
#The pairs that add up to -1 :
#( -2 , 1 )
#The pairs that add up to 1231233232 :
#None
#
#Running method 2
#---------------------
#The pairs that add up to 17 are [[9, 8]]
#The pairs that add up to 12 are [[6, 6], [8, 4], [9, 3]]
#The pairs that add up to 11 are [[8, 3], [9, 2]]
#The pairs that add up to 1 are [[1, 0], [1, 0], [3, -2]]
#No pairs that add up to  19
#The pairs that add up to -1 are [[1, -2], [1, -2]]
#No pairs that add up to  1231233232
#
#Running method 3
#---------------------
#The pairs that add up to 17 are {(8, 9)}
#The pairs that add up to 12 are {(6, 6), (3, 9), (4, 8)}
#The pairs that add up to 11 are {(3, 8), (2, 9)}
#The pairs that add up to 1 are {(0, 1), (-2, 3)}
#No pairs that add up to 19
#The pairs that add up to -1 are {(-2, 1)}
#No pairs that add up to 1231233232
#
#Running method 4
#---------------------
#The pairs that add up to 17 are {(8, 9)}
#The pairs that add up to 12 are {(6, 6), (3, 9), (4, 8)}
#The pairs that add up to 11 are {(3, 8), (2, 9)}
#The pairs that add up to 1 are {(0, 1), (-2, 3)}
#No pairs that add up to 19
#The pairs that add up to -1 are {(-2, 1)}
#No pairs that add up to 1231233232
#The ratio of time it takes of the first method w.r.t. second method= 1.3508771929824561
#The ratio of time it takes of the second method w.r.t. third method= 1.056953642384106
#The ratio of time it takes of the third method w.r.t. fourth method= 1.4059590316573556

import time
import random

def addtwo(A,tot):
        A.sort()
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
            elif (A[L]+A[R] < tot):
                L=L+1  
            else:
                R=R-1  
        print("The pairs that add up to",tot,":")        
        for x,y in zip(a1,a2):
            print("(",x,",",y,")")
        if len(a1) == 0:
            print("None")  


def addtwomethod2(A,tot):
    n = len(A) 
    sum = []
    result = []
    table = {}
    for i in range(0, n):
        test = tot - A[i]
        if test in table:
            sum.append([A[i],test])
        table[A[i]] = A[i]
    if len(sum) == 0:
        print("No pairs that add up to ",tot)
    else:
        print("The pairs that add up to",tot,"are",sum) #+str(sum[j][0])+" + "+str(sum[j][1])+" = "+str(tot))    
                
def addtwomethod3(A,tot):
    result = []    
    half=tot//2
    select = {tot-i for i in A if i <= half} & {i for i in A if i>=half}
    result = {(tot-i,i) for i in select}
    if len(result) == 0:
        print("No pairs that add up to",tot)  
    else:    
        print("The pairs that add up to",tot,"are",result)    
                
def addtwomethod4(A,tot):
    result = []    
    half=tot//2
    a1 = []
    a2 = []
    for i in A: 
        if tot-i in A and i <= half:
            a1.append(tot-i)
    a1=set(a1)
    result = {(tot-i,i) for i in a1}
    if len(result) == 0:
        print("No pairs that add up to",tot)  
    else:    
        print("The pairs that add up to",tot,"are",result)
                
#a few examples:
thelist = [4,2,8,0,1,-2,9,13445,1,4,3,6,6];
#thelist = random.sample(range(0, 1000), 1000)
print("Running method 1")
print("---------------------")
start1 = time.time()
addtwo(thelist,17)
addtwo(thelist,12)
addtwo(thelist,11)
addtwo(thelist,1)
addtwo(thelist,19)
addtwo(thelist,-1)
addtwo(thelist,1231233232)
end1 = time.time()
time1 = end1-start1
print()
print("Running method 2")
print("---------------------")
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
print("Running method 3")
print("---------------------")
start3 = time.time()
addtwomethod3(thelist,17)
addtwomethod3(thelist,12)
addtwomethod3(thelist,11)
addtwomethod3(thelist,1)
addtwomethod3(thelist,19)
addtwomethod3(thelist,-1)
addtwomethod3(thelist,1231233232)
end3 = time.time()
time3 = end3-start3
print()
print("Running method 4")
print("---------------------")
start4 = time.time()
addtwomethod4(thelist,17)
addtwomethod4(thelist,12)
addtwomethod4(thelist,11)
addtwomethod4(thelist,1)
addtwomethod4(thelist,19)
addtwomethod4(thelist,-1)
addtwomethod4(thelist,1231233232)
end4 = time.time()
time4 = end4-start4
print("The ratio of time it takes of the first method w.r.t. second method=",(time1/time2))
print("The ratio of time it takes of the second method w.r.t. third method=",(time2/time3))
print("The ratio of time it takes of the third method w.r.t. fourth method=",(time3/time4))
