# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

# Add the int() function before input() function
exam_two = int(input("Input exam grade two: "))

# Add the str() function before the input() function
exam_3 = int(input("Input exam grade three: "))

# Add commas to seperate the values within the list and rename variable 'exam_three' to 'exam_3'
grades = [exam_one, exam_two, exam_3]
sum = 0
for grade in grades:  # Rename 'grade' variable to 'grades'
    sum = sum + grade

avg = sum / len(grades)  # Rename 'grdes' to 'grades'

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:  # Added a ":" after 90
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"  # Replaced the single quote with a double quote
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:  # Replaced elif statement with else statement
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":  # Renamed 'letter-grade' varaible with 'letter_grade' and replaced 'is' operator with the '=='operator
    print("Student is failing.")  # Added parenthesis
else:
    print("Student is passing.")  # Added parenthesi
