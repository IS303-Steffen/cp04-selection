# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

# Else will run the code if the logical statement is not true
# note that once something is found true, the else WILL NOT run.

num1 = 3000
num2 = 20

# check if num1 is equal to num2.
# if it is, print "they are equal"
# if they aren't print "they are not equal"
# after, print "this will print no matter what, it is outside the if statement"

if num1 == num2:
    print('They are equal')
else:
    print('they are not equal')

print("this will print no matter what, it is outside the if statement")

# else if, typed elif allows you to specify multiple conditions

# check if num1 is equal to num2.
# if it is, print "they are equal"
# if num1 is greater, print "num 1 is greater than num2"
# if num 2 is greater, print "num 1 is less than num2"


if num1 == num2:
    print('They are equal')
elif num1 > num2:
    print('num 1 is greater than num2!')
else:
    print('num 1 is less than num2!')



