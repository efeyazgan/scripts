#python chal3.py 
#gives:
#Result:  8 + 9 = 17
#Result:  3 + 9 = 12
#Result:  4 + 8 = 12
#Result:  2 + 9 = 11
#Result:  3 + 8 = 11
#Result:  -2 + 3 = 1
#Result:  0 + 1 = 1
#No pairs in this list sum up to 19
#Result:  -2 + 1 = -1
#No pairs in this list sum up to 1231233232

def addtwo(A,tot):
        A = set(A)
        A = list(A)
        A.sort()
        n = len(A)
        L = 0
        R = n-1
        sum = tot
        res = 0
        while(L < R):
            while(A[L]+A[R] <= sum):
                if A[L]+A[R] == sum:
                    print("Result: ",A[L],"+",A[R],"=",sum)
                    res=res+1
                if L+1 < n-1:
                    L=L+1
                else:
                    break    
            if R-1 >= 0:
                R=R-1
            else:
                break    
            while(A[L]+A[R] > sum):
                if A[L]+A[R] == sum:
                    print("Result: ",A[L],"+",A[R],"=",sum)  
                    res=res+1 
                if R-1 >= 0:
                    R=R-1
                else:
                    break    
        if res == 0:
            print("No pairs in this list sum up to ",sum)
            
#a few examples:
thelist = [4,2,8,0,1,-2,9,13445,1,4,3];
addtwo(thelist,17)
addtwo(thelist,12)
addtwo(thelist,11)
addtwo(thelist,1)
addtwo(thelist,19)
addtwo(thelist,-1)
addtwo(thelist,1231233232)
