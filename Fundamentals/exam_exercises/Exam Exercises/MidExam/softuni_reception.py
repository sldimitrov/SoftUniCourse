# Read User input
first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
number_of_students = int(input())
# Calculate how many students are being answered per hour
students_per_hour = first_employee + second_employee + third_employee
# Initialize hour counter
counter = 0

# Initialize while loop
while True:
    if number_of_students <= 0:
        break

    if counter % 4 == 0:
        continue

    number_of_students -= students_per_hour
    counter += 1

# Print hours needed
print(f"Time needed: {counter}h.")