###  sum function
def Add(n):
    if n < 1:
        return n 
    return n+ Add(n-1)
print(Add(10))
