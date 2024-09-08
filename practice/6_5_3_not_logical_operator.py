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
## not
######
iNum1 = 3
iNum2 = 12

# not reverses True and False.

# check if iNum equals 2 is not true


# note, in examples where you're just comparing a variable to a value, not is basically the same as !=
# for example:

if iNum1 != 2:
    print("Second: this is similar to the first example")


#### Membership operator: in

# not is most useful when combined with "in"
# we'll use "in" more when we get to the chapter on data structures.
# but we can start testing it on strings.
    
example_string = "This is a secret message"

# check if "sec" in in example_string. Print "found it" if it is there.



# check if "crypto" is not in example string. Print "not there" if it isn't there.









