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

# You can put if statements inside of other if statements.
# just make sure you indent them in again (tab).
# remember you can hold shift + tab to tab backwards.

iAge = 9
sFavoriteFood = 'candy'

'''
check if they are 10 or under.
    If so, check if their favorite food is candy:
        if so, print "you're a kid, makes sense
        else, print "wow, such taste for a young child"
If they are older than 10:
    if so, check if their favorite food is candy:
        if so, print "you should eat more broccoli instead"
        otherwise, print "wow, good choice"

'''

# first it checks the age, if they are under 10
if iAge <= 10:
    # if they are under 10, it has a whole other check here:
    if sFavoriteFood == 'candy':
        print('you\'re a kid, makes sense')
    else:
        print('wow, such taste for a young child')
# now we are back to the original if statement. if they are older than 10, we'll end up here
else:
    # we can have entirely different if statements here, or none at all. Your choice
    if sFavoriteFood == 'candy':
        print ('you should eat more broccoli instead')
    else:
        print('wow, good choice')
