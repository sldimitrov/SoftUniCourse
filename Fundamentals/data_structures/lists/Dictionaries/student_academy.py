# Initialise a dictionary
# to store information.
student_book = {}
number_of_rows = int(input())

# Initialise a for loop to iterate N times.
for line in range(number_of_rows):
    student_name = input()
    grade = float(input())
    # if name is not in the list initialise
    # it with blank list
    if student_name not in student_book.keys():
        student_book[student_name] = []
    # append the grade in every scenario
    student_book[student_name].append(grade)

clone_dict = student_book.copy()

for key, value in clone_dict.items():
    # calculate the average
    average = 0
    for v in value:
        average += v
    average = average / len(value)
    # delete the students who are below 4.5
    # from the dict
    if average < 4.5:
        student_book.pop(key)

# Print the output
for key, value in student_book.items():
    average = 0
    for v in value:
        average += v
    average = average / len(value)
    print(f"{key} -> {average:.2f}")