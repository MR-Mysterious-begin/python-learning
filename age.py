""" Write a program in python to input age. Thereafter check if he is less than 18, then not eligible for driving license, if age is more than 18, then eligible for driving license
and if age is equal to 18, then the person needs to visit the office for a test """

a=int(input("Please enter your age"))
if a>18: 
    print("Hurray! You are eligible for a driving license")
elif a<18:
    print("Sorry! You are not eligible for a driving license")
else:
    print("We can't determine currently. Please visit the office for a test")
