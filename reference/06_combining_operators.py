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

'''

The scenario:
A student can win a prize based on a few different combinations of conditions.
We have 4 conditions we will evaluate:
1. grades_above_90: Did the student score above 90 on average in their classes?
2. attendance_above_90: Did the student attend more than 90% of the classes?
3. extracurricular_participation: Did the student participate in extracurricular activities?
4. no_behavior_issues: Did the student have no major behavior issues?

Rule: No student can win a prize if they have behavior issues.
We check the other conditions ONLY if the student has no behavior issues.

'''

# Example 1:
# A student has everything they need, except they have behavior issues.

grades_above_90 = True
attendance_above_90 = True    
extracurricular_participation = True  
no_behavior_issues = False   

# Example 1: 
# This is written without parentheses. Is it working correctly?
if no_behavior_issues == True and grades_above_90 == True or attendance_above_90 == True and extracurricular_participation == True:
    print("ex1: Student wins the prize! (incorrect logic)")
else:
    print("ex1: Student does not win the prize. (incorrect logic)")

# Example 1: Corrected with parentheses.
# Now, we correctly group the conditions to match our logic: 

if no_behavior_issues == True and (grades_above_90 == True or (attendance_above_90 == True and extracurricular_participation == True)):
    print("ex2: Student wins the prize! (correct logic)")
else:
    print("ex2: Student does not win the prize. (correct logic)")


# Example 2: A student meets the attendance and extracurricular condition, but has behavior issues.
grades_above_90 = True
attendance_above_90 = False
extracurricular_participation = False
no_behavior_issues = False

if no_behavior_issues == True and (grades_above_90 == True or (attendance_above_90 == True and extracurricular_participation == True)):
    print("ex2: Student wins the prize!")
else:
    print("ex2: Student does not win the prize")

# Example 3: A student meets the attendance condition, and has no behavior issues.
grades_above_90 = False
attendance_above_90 = True
extracurricular_participation = False
no_behavior_issues = True

if no_behavior_issues == True and (grades_above_90 == True or (attendance_above_90 == True and extracurricular_participation == True)):
    print("ex3: Student wins the prize!")
else:
    print("ex3: Student does not win the prize")

# Example 4: A student meets the attendance condition and extracurricular option, and has no behavior issues.
grades_above_90 = False
attendance_above_90 = True
extracurricular_participation = True
no_behavior_issues = True

if no_behavior_issues == True and (grades_above_90 == True or (attendance_above_90 == True and extracurricular_participation == True)):
    print("ex4: Student wins the prize!")
else:
    print("ex4: Student does not win the prize")

# PRACTICE:
# Let's change the rules:
# Make it so a student can win a prize as long as they have at least one of: grades above 90, attendance above 90, extracurricular activities.
# But they still can't have behavioral issues in any case

# evaluate the student below and write the condition:
grades_above_90 = False
attendance_above_90 = False
extracurricular_participation = True
no_behavior_issues = True

if no_behavior_issues == True and (grades_above_90 == True or attendance_above_90 == True or extracurricular_participation == True):
    print("ex3: Student wins the prize!")
else:
    print("ex3: Student does not win the prize")