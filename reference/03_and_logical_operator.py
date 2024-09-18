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

# ======================
# LOGICAL OPERATORS: AND
# ======================

'''
OVERVIEW
--------
So far, we've just checked if a single condition is True, like:
    x > y

But you can add other logical operators to add multiple conditions:

    and     every condition must be true
    or      at least one condition must be true 

We'll go over and in this file.

STRUCTURE
---------
and:
    - just put "and" between every logical statement in your if or elif

EXAMPLE
-------
if x == y and y != z:
    print("All conditions met.")
'''

num_1 = 3
num_2 = 12
# 1. PUT 2 CONDITIONS IN ONE IF STATEMENT
# Print a message if num_1 doesn't equal 2 and if num_2 is above 10
if num_1 != 2 and num_2 > 10:
    print("First: both conditions were correct")

# 2. PUT 2 CONDITIONS IN ONE IF STATEMENT (AGAIN)
# Print a message if num_1 doesn't equal 3 and if num_2 is above 10
if num_1 != 3 and num_2 > 10:
    print("Second: you shouldn't be seeing this")

# 3. PUT 3 CONDITIONS IN ONE IF STATEMENT
# Write any if statement you want, but use 3 "and" operators.
# Print something if they are all true.
if num_1 != 2 and num_2 > 10 and num_1 < num_2 and num_2 == 12:
    print("Third: all conditions were correct")