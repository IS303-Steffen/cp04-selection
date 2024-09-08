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

# by combining comparisons with the if statement,
# you control what code gets executed

#structure of if statement:
'''
    must start with lowercase if
    then you must have a conditional statement
        (something that results in TRUE or FALSE). Usually a comparison
    a colon : following the conditional statement
    Then indent in (press tab) on the next line.
    Anything indented from the "if" will be part of the if statement
    Outdent to exit the "if" statement.

'''

# Write a program that prints "congrats!"
# but only if num1 is not equal to num2

num1 = 10
num2 = 20




# Note, you can also do a shorthand version.
# put a colon after the conditional statement, then the code you want. You can add commas to put more lines.
# I don't recommend this, especially for longer if statements (which we'll get into soon)



# PRACTICE:
'''
    Check if a number stored in a variable is equal to 5.
    If it is, say "Wow it is equal to 5". No matter what the number
    is, print out the value of the number afterwards.
'''




# note, when working with booleans, you can just put the variable name with nothing else.
# if it is True, it will run, if False it will skip it:

example_boolean = True

