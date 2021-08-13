# write a program that keeps taking input from user until the user enters a number greater than 100.Print "Congrats! you have printed a number greater than 100" after the process finishes

while True:
    n = int(input("Enter input"))
    if n>100:
        print("Congrats! You have printed a number greater than 100")
        break
    else:
        print("Try Again")
        continue
