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

# ==================
# NESTED IF PRACTICE
# ==================

# 1. WRITE A PROGRAM TO GIVE A GRADE BOOST
# You are creating a simple grading system for a course.
# The course has two exams: a midterm exam and a final exam.
# Students can also earn a grade boost if they completed a special project.

# Prompt the user for three pieces of information:

# 1. Their score on the midterm exam (out of 100).
# 2. Their score on the final exam (out of 100).
# 3. Whether they completed the special project (yes or no).

# The grade will be determined as follows:

# 1. If the average score of the two exams is 90 or above, they get an 'A'.
# 2. If the average is 80 or above (but less than 90), they get a 'B'.
# 3. If the average is 70 or above (but less than 80), they get a 'C'.
# 4. If the average is 60 or above (but less than 70), they get a 'D'.
# 5. Otherwise, they get an 'F'.

# However, if they completed the special project,
# they can get a one-grade boost
# (e.g., a 'B' becomes an 'A', a 'C' becomes a 'B', etc.).
# An 'A' remains an 'A' even with the bonus.

# Your program should output the final grade of the student.
# the first part is completed for you just to save time. 

# Get input from the user
midterm_score = float(input("Enter your midterm exam score (out of 100): "))
final_score = float(input("Enter your final exam score (out of 100): "))
completed_project = input("Did you complete the special project? " 
                       +  "(yes or no): ").lower()

# Calculate the average score
average_score = (midterm_score + final_score) / 2

# Determine the grade based on the average score
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Check if the special project was completed to boost the grade
# Hint: try nested if statements

if completed_project == "yes":
    if grade == "B":
        grade = "A"
    if grade == "C":
        grade = "B"
    if grade == "D":
        grade = "C"
    if grade == "F":
        grade = "D"

# Print the final grade
print(f"Your final grade is {grade}")