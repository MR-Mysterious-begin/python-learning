""" Exercise 2 - Faulty Calculator
Design a calculator which will correctly solve all the problems except
the following ones:
45 * 3 = 555, 56+9 = 77, 56/6 = 4
Your program should take operator  and the two numbers as input from the user
and then return the result """

n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
o = input("Enter the operator (Eg- +,-,*,/)")
if o == "+":
    if (n1 == 56 and n2 == 9) or (n1 == 9 and n2 == 56):
        print("77")
    else:
        print(n1+n2)
elif o == "*":
    if (n1 == 45 and n2 == 3) or (n2 == 45 and n1 == 3):
        print("555")
    else:
        print(n1*n2)
elif o == "/":
    if n1 == 56 and n2 == 6:
        print("4")
    else:
        print(n1/n2)
else:
    print(n1-n2)
