# Read User input
number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendances = 0

# Initialize a for loop
for student in range(number_of_students):
    current_student_attendances = int(input())
    current_student_bonus = current_student_attendances / number_of_lectures * (5 + additional_bonus)
    if current_student_bonus > max_bonus:
        max_bonus = round(current_student_bonus)
        max_attendances = current_student_attendances

# Print User output
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_attendances} lectures.")
