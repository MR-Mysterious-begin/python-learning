#A guessing game.

a=18
i=1
n=int(input("Enter a number"))
while(i<=10):
    if n==a:
        print("Congrats! You guessed the number right! You win! :)")
        break
    elif n > a:
        print("The guessed number is greater than the actual number.")
    elif n < a:
        print("The guessed number is lesser than the actual number.")
    print("Number of chances left:",(10-i))
    n=int(input("Try Again"))
    i=i+1
if i>10:
    print("The chances are over. You lose! :(")
