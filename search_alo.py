# liner search
def Liner_search(Input_value,My_arr):

    for i in range(len(My_arr)):
        if My_arr[i]== Input_value:
           print(f"This value is >> {My_arr[i]} and valus index is >>{i}")
           break
    else:
        print("We don't find this value in That array !") 

My_arr =[3,4,5,6,7,8,20,40,33]
Input_value = int(input("Enter The value:"))        
Liner_search(Input_value,My_arr)


########### binary search
Arr = [1,3,4,5,6,7,8,9,9,10,11,12,13,14,16]
_input  = int(input("Enter The value:"))

def Birary_search(arr,_input):
    left = 0
    right = len(arr)
    while left <= right:
        mid = (left+right)//2
        if _input == arr[mid]:
            print(f"we find This value. index {mid} ",arr[mid])
            break
        elif arr[mid] < _input:
            left = mid +1
        elif arr[mid] > _input:
            right = mid -1
    else:
            print("We don't find this value in that array.")           

Birary_search(Arr,_input)