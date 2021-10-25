from math import sqrt

def Prime_Factor(num):
    arr = []
    while num % 2 == 0:
        num //= 2
        arr.append(2)
    squre_root = int(sqrt(num))
    print("none",arr,squre_root)
    for i in range(3, squre_root,2):
        while num % i == 0:
            num = num // i
            arr.append(i)
    if num > 1:
        arr.append(num)        
    return arr
if __name__ == "__main__":
    inp = int(input("Enter The number:"))
    PF = Prime_Factor(inp)
    if inp in PF:
        print(PF)
    else:
        print("Its not prime number:")    