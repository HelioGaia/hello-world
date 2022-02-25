## README
## hello-world
Version-control lab for CMPINF 0010
Asks for name & Fav color

## What It Is

This program generates a pseudo random password based on a few inputs from the user.
The user is prompted for their first name and their favorite color, and in the 
computer then outputs a password that contains letters, numbers, and special characters.

## How To Use It

This program requires no installation. It can be run from the command line, as long as the
user has access to the .py file.

1. User Enters Information:
      ```python
        name = input("What is your name? ")
        color = input("What is your favorite Colour?")
        ```
2. Prints the Completed Password
      ```python     
          mixed += name[nC]
          num += int(ord(color[i]))
          spec += random.choice(specList1)
          print(mixed + str(num) + spec)
          ```
          
## How To Contribute

Since this is an open source project, any contributions to the program would be apprecieated.
Creating a fully random generation of the program based on the user inputs is something
that is not included in the original publication of the program. If there are any bugs in 
the code, feel free to submit a pull request explaining what the error was, and what was 
changed in order to fix the problem. For all changes, we ask that you fork the repository 
and make any changes to the file locally, and submit a pull request, so the main contributor
can accept the changes.
