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

# ====
# ELSE
# ====

'''
OVERVIEW
--------
You can extend an if statement with "else". Code under "else" will run when
the condition in the if statement is False.

If the original statement is True, the code under "else" will not run.

STRUCTURE
---------
else:
    - Can only exist after an if statement. Needs to be at the same indentation
      level as the if statement. Has a colon immediately after "else"

EXAMPLE
-------
if x == y:
    print("They are equal")
else:
    print("They are not equal")
'''


# 1. WRITE IF, ELSE:
# If num_1 and num_2 are the same, print out "They are the same". Otherwise,
# print out "They are different". No matter what, print out
# "This message will always print."

num_1 = 10
num_2 = 20

if num_1 == num_2:
    print("They are the same")
else:
    print("They are different")

print("This message will always print.")

# ====
# ELIF
# ====

'''
OVERVIEW
--------
"elif" lets you check multiple statements. The first statement that is True
will have its code executed, and then exit the if statement. You can use as
many elifs as you want. You can optionally add an else statement at the very
end.


STRUCTURE
---------
elif:
    - can only exist if there is an if statement first. Structured exactly
      the same as an if statement.

EXAMPLE
-------
if x == y:
    print("They are equal")
elif x > y:
    print("x is bigger")
else:
    print("x must be smaller")

'''

# 2. WRITE CODE FOR MULTIPLE CONDITIONS:
# if num_starbursts_eaten is less than 10 then print "Live a little."
# if num_starbursts_eaten is less than 50 then print "Nice."
# if num_starbursts_eaten is less than 100 then print "Are u full yet?"
# if num_starbursts_eaten is any thing else, print "Woah! Amazing!"

num_starbursts_eaten = 128

if num_starbursts_eaten < 10:
    print("live a little")
elif num_starbursts_eaten < 50:
    print("nice.")
elif num_starbursts_eaten < 150:
    print("Are u full yet?")
else:
    print("Woah! Amazing!")

