name = input("What is your name? ")
favColor = input("What is your favorite Color?")

#Creates a value stored in num from ascii values that is to be added to the end of the password
num = 0
for i in range(len(name)):
    num += int(ord(name[i]))
for i in range(len(favColor)):
    num += int(or(favColor[i]))
