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

# =========================
# IF STATEMENTS (SELECTION)
# =========================

'''
OVERVIEW
--------
By default, code runs in "sequence", meaning it runs line by line from the top
down. When using if statements, you are using "selection". This means you make 
decisions or choices about which lines of code to run based on conditions.

By combining comparisons (<, ==, etc.) with operators in if statements
your code can become much more dynamic and respond to different situations.

STRUCTURE
---------
if statements:
    - Start with a lowercase if.
    - Follow with a conditional statement
      (something that results in True or False) and then a colon.
    - Anything indented on the line after the colon will be part
      of the if statement. Outdent to exit the if statement.

EXAMPLE
-------
if x == y:
    print("Example text")
    print("This is also part of the if statement")

print("This is outdented. Therefore, not part of the if statement")
'''

# 1. COMPARE 2 NUMBERS:
# Write an if statement that prints "They are the same!" if num_1 and num_2
# are equivalent. Feel free to mess with the values and see what happens.

num_1 = 10
num_2 = 10


# 2. COMPARE 2 NUMBERS (AGAIN):
# Write an if statement that prints "They are different!" if num_3 and num_4
# are different. Feel free to mess with the values and see what happens.
# print out a message saying "This will always print." whether or not num_3
# and num_4 are different.

num_3 = 10
num_4 = 20



'''
TIP
---
When using booleans with if statements, you can just put the variable name
without any other comparison operators. Because booleans already represent
either True or False there's no need to add anything else. 
'''

# 3. USE A BOOLEAN:
# If example_boolean is True, write out
# "the boolean must have been True."

example_boolean = True



'''
IF STATEMENT ON SINGLE LINE
---------------------------
You can write an if statement on one line to save space.
This might be convenient for a very short if statement, but I generally
don't recommend for anything longer than very simple lines of code because
it can become harder to read.

EXAMPLE
-------
if num_1 == num_2: print("Example first line"), print("Example last line")

'''

# 4. WRITE IF STATEMENT ON A SINGLE LINE:
# If num_5 is greater than num_6, print out "num_5 is bigger"
# put the print statement on the same line as the if statement.

num_5 = 2
num_6 = 1

