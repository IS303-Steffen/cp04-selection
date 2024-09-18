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
# LOGICAL OPERATORS: NOT
# ======================

'''
OVERVIEW
--------
Adding "not" to any condition just reverses it. Note that this is most
commonly added to conditions that use "in" which is described later in this
file.

EXAMPLE
-------
if not x == y:
    print("x does not equal y.")
'''

num_1 = 3
num_2 = 12

# 1. REVERSE A CONDITION
# Check if num_1 is equal to num_2 but put "not" before the condition.
if not num_1 == num_2:
    print("First: condition was correct")

'''
Note, # 1. isn't very common to do, since you can just replace not == with !=
It is more common to pair it with "in" as shown below
'''

# =======================
# MEMBERSHIP OPERATOR: IN
# =======================

'''
OVERVIEW
--------
Use "in" to check whether one variable is a part of something else.
It will be most useful for when we talk about lists, but for now you can
use it to check if something is part of a string.

EXAMPLE
-------
if "A" in english_alphabet:
    print("A was found")
'''

# 2. CHECK IF STRING IS IN OTHER STRING
# Check if "secret" is in example_string. Print "found it" if it is there.
example_string = "This is a secret message"

if "sec" in example_string:
    print("found it")

# 3. CHECK IF STRING IS NOT IN OTHER STRING
# Check if "crypto" is not in example string.
# Print "not there" if it isn't there.
if "crypto" not in example_string:
    print("not there")

