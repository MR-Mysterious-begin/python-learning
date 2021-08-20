n = int(input("Enter the number of terms"))
a=0
b=1
c=0
print(a)
print(b)

def fibonacci(n):
    for i in range(n-2):
        global a
        global b
        global c
        c=a+b
        print(c)
        a=b
        b=c


fibonacci(n)
