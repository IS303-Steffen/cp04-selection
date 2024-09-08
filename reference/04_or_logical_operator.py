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

'''
    and     every statement must be true
    or      at least one statement must be true
    not     changes true to false and false to true
'''
######
## or
######

iNum1 = 3
iNum2 = 12

# print something if iNum doesn't equal 2 or iNum2 is above 10
if iNum1 != 2 or iNum2 > 10:
    print("First: both conditions were correct")

# print message if iNum doeesn't equal 3 or iNum2 is above 10
if iNum1 != 3 or iNum2 > 10:
    print("Second: one condition was correct")

# print message if iNum doeesn't equal 3 or iNum2 doesn't equal 12
if iNum1 != 3 or iNum2 != 12:
    print("third: you shouldn't be seeing this")

# like and, you can do as many ors as you want.
if iNum1 != 3 or iNum2 > 10 or iNum1 < iNum2 or iNum2 == 12:
    print("Fourth: at least one condition is correct")



