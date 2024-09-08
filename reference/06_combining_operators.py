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

# or, and, & not aren't too complicated when used by themselves, but it can get a little trickier when combined together.

# something to keep in mind is that without parentheses, python has an order that it evaluates the operators:

'''
    First:      not
    Second:     and
    Third:      or
'''

a = True
b = True
c = False
d = True

# this is confusing. Stare at it. it evaluates the ands before the ors
# what will print out?
if a == True and b == True or c == True and d == True:
    print("ex1: Condition met")
else:
    print("ex1: Condition not met")

# I recommend using parentheses ALWAYS when mixing ands and ors
# the below example is identical to the first one
if (a == True and b == True) or (c == True and d == True):
    print("ex2: Condition met")
else:
    print("ex2: Condition not met")


# what about this one?
if (a == True or b == True) and (c == True and d == True):
    print("ex3: Condition met")
else:
    print("ex3: Condition not met")


# practice:
# if a, b, or c are False AND d is not False print ("this worked") otherwise, print "didn't work"
if (a == False or b == False or c == False) and (not d == False):
    print("this worked")
else:
    print("didn't work")
