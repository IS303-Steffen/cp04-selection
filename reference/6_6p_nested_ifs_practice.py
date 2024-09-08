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

# Practice:
'''
You are creating a simple grading system for a course.
The course has two exams: a midterm exam and a final exam.
Students can also earn a bonus boost if they have completed a special project.

Prompt the user for three pieces of information:

1. Their score on the midterm exam (out of 100).
2. Their score on the final exam (out of 100).
3. Whether they completed the special project (yes or no).

The grade will be determined as follows:

1. If the average score of the two exams is 90 or above, they get an 'A'.
2. If the average is 80 or above (but less than 90), they get a 'B'.
3. If the average is 70 or above (but less than 80), they get a 'C'.
4. If the average is 60 or above (but less than 70), they get a 'D'.
5. Otherwise, they get an 'F'.

However, if they completed the special project, they can get a one-grade boost
(e.g., a 'B' becomes an 'A', a 'C' becomes a 'B', etc.). An 'A' remains an 'A' even with the bonus.

Your program should output the final grade of the student.  '''
# the first part is completed for you just to save class time. 
#  Note: you can highlight the text and use ctrl + / (windows) or cmd + / to comment or uncomment things in bulk

# Get input from the user
fMidtermScore = float(input("Enter your midterm exam score (out of 100): "))
fFinalScore = float(input("Enter your final exam score (out of 100): "))
sCompletedProject = input("Did you complete the special project? (yes or no): ").lower()

# Calculate the average score
fAverageScore = (fMidtermScore + fFinalScore) / 2

# Determine the grade based on the average score
if fAverageScore >= 90:
    sGrade = 'A'
elif fAverageScore >= 80:
    sGrade = 'B'
elif fAverageScore >= 70:
    sGrade = 'C'
elif fAverageScore >= 60:
    sGrade = 'D'
else:
    sGrade = 'F'

# Check if the special project was completed to boost the grade
# hint: try nested if statements

# Print the final grade

if sCompletedProject == "yes":
    if sGrade == "B":
        sGrade = "A"
    if sGrade == "C":
        sGrade = "B"
    if sGrade == "D":
        sGrade = "C"
    if sGrade == "F":
        sGrade = "D"

print(f"your final grade is {sGrade}")