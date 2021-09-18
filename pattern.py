"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
0 1 0 1 0 1
1 0 1 0 1 0 1
0 1 0 1 0 1 0 1
"""
def Print_squre(hight):
    for i in range(1 ,hight+2):
        arr = []
        for j in range(1,i):
            if j % 2 == 0:
                j = 0
            else:
                j = 1    
            arr.append(str(j))
        bd =[]    
        for i in range(len(arr)-1,-1,-1):
            bd.append(arr[i])  
        print(" ".join(bd))    
     
Print_squre(4)   


