########  secection sort

def Selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                x = arr[i]
                arr[i]= arr[j]
                arr[j] = x
    return arr

 ######### insertion sort 
def  Insertion_sort(arr):
    for i in range(1,len(arr)):
        item = arr[i]
        j = i-1
        while  j>= 0  and arr[j] >item :
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = item    
    return arr    

my_arr =[2,8,1,6,8,10,11,23,55,75,99,42]

print( "This is  Selection sort result",Selection_sort(my_arr))
print("This is insertion sort result", Insertion_sort(my_arr))