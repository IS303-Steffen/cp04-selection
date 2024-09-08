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

# PRACTICE:
'''
    Ask the user to enter their favorite day of the week.
        If it is Monday, print "wow, early weekday"
        If it is Wednesday print "wow, midweek!"
        if it is Saturday print "weekend, woo!"
        if it is any other day, print "that day's pretty good too"
'''
sInput = input("What is your favorite day of the week? ")

if sInput == "Monday":
    print('wow, early weekday!')
elif sInput == "Wednesday":
    print("wow midweek")
elif sInput == "Saturday":
    print("weekend woo!")
else:
    print("That's pretty good too")
