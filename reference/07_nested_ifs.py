import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ====================
# NESTED IF STATEMENTS
# ====================

'''
OVERVIEW
--------
You can put if statements inside of other if statements.
The inner, or "nested" if statements will only be evaluated if the outer
if statements are evaluated as True.

EXAMPLE
-------
if x == y:
    if day == "Tuesday":
        print("Made it here")
    else:
        print("Something else")

TIP
---
You can select entire blocks of code and press tab to indent them.
You can also hold shift + tab to tab backwards.
'''

# 1. USE NESTED IFS FOR CUSTOM MESSAGES
# use the age and favorite_food variables.
# check if they are 10 or under.
#   If so, check if their favorite food is candy:
#       if so, print "you're a kid, makes sense"
#       else, print "wow, such taste for a young child"
# If they are older than 10:
#   if so, check if their favorite food is candy:
#       if so, print "you should eat more broccoli instead"
#       otherwise, print "wow, good choice"

age = 9
favorite_food = 'candy'

# first it checks the age, if they are under 10
if age <= 10:
    # if they are under 10, it has a whole other check here:
    if favorite_food == 'candy':
        print('you\'re a kid, makes sense')
    else:
        print('wow, such taste for a young child')
# now we are back to the original if statement. if they are older than 10, we'll end up here
else:
    # we can have entirely different if statements here, or none at all. Your choice
    if favorite_food == 'candy':
        print ('you should eat more broccoli instead')
    else:
        print('wow, good choice')
