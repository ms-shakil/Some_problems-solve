"""
|0|1|2|
|3|4|5|
|6|7|8|

"""
value = [[str(i)for i in range(j*3,(j+1)*3)]for j in range(3)]
print(value)
for i in value:
    print("| "+" |".join(i)+" |")

