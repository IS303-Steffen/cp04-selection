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
# MULTIPLE IFS VS ELIFS
# ====================

'''
COMPARE THE TWO EXAMPLES
--------------------------
When you use elifs (or else) it is connected to the original if statement.

You could also just use multilple if statements, but the behavior is different

Look at the 2 examples below. Why do they print out different results?
'''

example_number = 100

# EXAMPLE 1:
# A single if statement that has multiple elifs
if example_number < 150:
    print("less than 150")

elif example_number < 200:
    print("less than 200")

elif example_number < 300:
    print("less than 300")


# EXAMPLE 2:
# 3 separate if statements.
if example_number < 150:
    print("less than 150")

if example_number < 200:
    print("less than 200")

if example_number < 300:
    print("less than 300")


'''
KEY POINT
---------
For a single if statement, only the first section found to be true is
entered, even if multiple if or elif conditions would be true.

If you use multiple if statements, if will check each individual
condition, because each if statement is independent of the others.
'''