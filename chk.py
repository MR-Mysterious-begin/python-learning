#Write a program to create a list in python and print only numbers which are greater that 6

l = [1,7,8,"s","a","z",9,10,"d",4,"n"]
for item in l:
    if str(item).isnumeric():
        if item > 6:
            print(item)