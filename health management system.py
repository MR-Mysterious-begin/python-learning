"""
In this program create 2 text files for each user to store the food taken and exercise done at a specific time
Also the user must be able to access these text files for just seeing
No. of users = 3

NOTE- I am not going to upload the text files since I will be using those for personal use also. You can create your own files and
change the name accordingly in the program

"""

def getdate():
    """This function will return date and time"""
    import datetime
    return datetime.datetime.now()

n=int(input("Enter 1 to access 1st user's database, 2 to access 2nd user's database and 3 to access 3rd user's database"))
n1=int(input("Do you want to lock data or retrieve data (1/2)"))
n2=int(input("Exercise or Food? (1/2)"))
dt=str(getdate()) + ": /n"
if n2 == 1:
    if n == 1: f=open('e1', 'r+')
    elif n == 2: f=open('e2', 'r+')
    elif n == 3: f=open('e3', 'r+')
elif n2 == 2:
    if n == 1: f=open('f1', 'r+')
    elif n == 2: f=open('f2', 'r+')
    elif n == 3: f=open('f3', 'r+')
if n1 == 2:
    print(f.read())
elif n1 == 1:
    e=input("Enter the name of the exercise/food .")
    f.write(dt)
    f.write(e)
    print("This is stored as", dt, e)
f.close()