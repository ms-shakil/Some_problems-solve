"""
The factorial of the integer n , written n! , is defined as:
n! = n * (n-1)*(n-2)*... *2*1
Calculate and print the factorial of a given integer.

For example Inp =25 we calculate 25* 24* 23*....*2*1 and we get 15511210043330985984000000 .


"""
def Factorial(inp):
    val = 1
    for i in range(1,inp):
       val += val*i
    print(val)    
inp = int(input("Enter the value:"))
Factorial(inp)   