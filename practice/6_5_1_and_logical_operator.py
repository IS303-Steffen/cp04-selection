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

# So far with if statements, we've just checked if one logical statement is true
    # e.g. iNum1 >= iNum2

# However, we often want to check for multiple conditions simultaneously
# or only need one of several statements to be true
# logical operators and / or help with this
# not reverses false or true
'''
    and     every statement must be true
    or      at least one statement must be true
    not     changes true to false and false to true
'''

######
## and
######
iNum1 = 3
iNum2 = 12

# Print message if iNum1 doesn't equal 1 and if iNum2 is above 10


# Print message if iNum1 doesn't equal 3 and if iNum2 is above 10


# try writing something with 3 ands.
