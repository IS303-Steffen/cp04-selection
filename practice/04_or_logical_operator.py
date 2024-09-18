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
# LOGICAL OPERATORS: OR
# ======================

'''
OVERVIEW
--------
    and     every condition must be true
    or      at least one condition must be true 

We'll go over "or" in this file. When using or, as long as at least one of 
the conditions in the if/elif statement is True, then the entire statement
is evaluated as True.

STRUCTURE
---------
and:
    - just put "or" between every logical statement in your if or elif

EXAMPLE
-------
if x == y or y != z:
    print("At least one condition met.")
'''

num_1 = 3
num_2 = 12

# 1. PUT 2 CONDITIONS IN ONE IF STATEMENT
# Print a message if num_1 doesn't equal 2 or if num_2 is above 10



# 2. PUT 2 CONDITIONS IN ONE IF STATEMENT (AGAIN)
# Print a message if iNum doesn't equal 3 or num_2 is above 10



# 3. PUT 2 CONDITIONS IN ONE IF STATEMENT (AGAIN)
# Print message if iNum doesn't equal 3 or num_2 doesn't equal 12



# 4. PUT 3 CONDITIONS IN ONE IF STATEMENT (AGAIN)
# Write any if statement you want, but use 3 "or" operators.
# Print something if at least one is true.




