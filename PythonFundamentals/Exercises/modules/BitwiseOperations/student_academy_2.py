# Initialise a dictionary to store kids grades
grades_data = {}

# Read User input
n = int(input())
for _ in range(n):
    student = input()
    grade = float(input())
    if student not in grades_data:
        grades_data[student] = []
    grades_data[student].append(grade)

excellent_students = {}
# Calculate the average grade and keep only the students
# with 4.50 or above
for student, list_of_grades in grades_data.items():
    average = 0
    for grade in list_of_grades:
        average += grade
    average = average / len(list_of_grades)
    if average >= 4.5:
        excellent_students[student] = f'{average:.2f}'

# Print User output
for student, grade in excellent_students.items():
    print(f"{student} -> {grade}")