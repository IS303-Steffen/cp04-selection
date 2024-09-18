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

# ===========================
# IF, ELIF, AND ELSE PRACTICE
# ===========================

# 1. USE IF, ELIF, AND ELSE WITH INPUT():
# Ask the user to enter their favorite day of the week.
# If it is Monday, print "wow, early weekday"
# If it is Wednesday print "wow, midweek!"
# If it is Saturday print "weekend, woo!"
# If it is any other day, print "that day's pretty good too"

# CHALLENGE: Try and make it so your code works no matter how the
#            the day of the week is capitalized.


