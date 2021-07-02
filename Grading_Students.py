"""
HackerLand University has the following grading policy
1. Every student receives a grades  in the inclusive range from 1 to 100.
2. Any grades  less than 40  is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:
1. If the difference between the  grade and the next multiple of 5 is less than 3 , round  up to the next multiple of 5 .
2. If the value of grade  is less than 38, no rounding occurs as the result will still be a failing grade.

Examples:

 1. grade = 84 round to 85 (85 - 84 is less than 3)
 2. grade= 29  do not round (result is less than 40)
 3. grade = 57 do not round (60 - 57 is 3 or higher)
"""
def MyFunction(grades):
    arr =[40,45,50,55,60,65,70,75,80,85,90,95,100]
    my_arr = []
    for j in range(len(grades)):
        
        for i in range(len(arr)):
            if grades[j] <=37:
                my_arr.append(grades[j])
                break
            val = arr[i]-grades[j]
            if val >= 0 and val <=2:
               my_arr.append(arr[i])
               break
            elif val >=3 and val <=5:
               my_arr.append(grades[j])
               break
            else:
                continue
    return my_arr 
inp = int(input("Enter the number:"))
arr2 =[]
for i in range(inp):
    while True:
        inp2 = int(input("Enter the grade:"))
        if inp2 >=0 and inp2 <=100:
           arr2.append(inp2)
           break
        print("Grade  range 1 to 100.")
print(MyFunction(arr2))
  