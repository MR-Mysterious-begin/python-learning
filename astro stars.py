"""
A program to input an integer and 1 or 2. Create a pattern like this

if value is true or 1:

*
**
***
****

if value is false or 2

****
***
**
*

The number of rows will be equal to n
"""
i=1
j=1;
n = int(input("Enter the number of rows"))
b = int(input("Enter 1 for true and 2 for false"))
if b==1:
    while i <= n:
        j=1
        while j <= i:
            print("*",end="")
            j+=1
        print()
        i+=1
elif b==2:
    i=n
    while i >= 1:
        j=1
        while j <= i:
            print("*",end="")
            j+=1
        print()
        i-=1
else:
    print("Invalid input!")
