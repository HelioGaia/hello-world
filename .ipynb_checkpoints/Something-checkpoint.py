<<<<<<< HEAD
name = input("What is your name? ")
favColor = input("What is your favorite Color?")

=======
# import random
import random
name = input("What is your name? ")
color = input("What is your favorite Colour?")


##Creates a "Random" String
nC = 0
cC = 0

mixed = ""

while nC < len(name) or cC < len(color):
    try:
        if nC * len(color) < cC * len(name):
            mixed += name[nC]
            nC += 1
        else:
            mixed += color[cC]
            cC += 1
    except:
        break
        
        
>>>>>>> 6e929184decacdaa8ad8f342136ecf02e37448d7
#Creates a value stored in num from ascii values that is to be added to the end of the password
num = 0
for i in range(len(name)):
    num += int(ord(name[i]))
<<<<<<< HEAD
for i in range(len(favColor)):
    num += int(or(favColor[i]))
=======
for i in range(len(color)):
    num += int(ord(color[i]))

    
##Creates Special charecters
specList1 = ['!', '@,', '#', '$'] 
specList2 = ['%', '^', '&', '*']
spec = ""

if len(name) < len(color):
    spec += random.choice(specList1)
    spec += random.choice(specList1)
elif len(name) > len(color):
    spec += random.choice(specList2)
    spec += random.choice(specList2)
else:
    spec += random.choice(specList1)
    spec += random.choice(specList2)
   
##prints the completed password
print(mixed + str(num) + spec)
>>>>>>> 6e929184decacdaa8ad8f342136ecf02e37448d7
