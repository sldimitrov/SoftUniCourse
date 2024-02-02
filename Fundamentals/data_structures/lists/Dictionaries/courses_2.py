# Initialise a dictionary to store the data
stored_info = {}

# Take an user input until its == end:
while True:
    command = input()
    if command == 'end':
        break
    course, student = command.split(" : ")

    if course not in stored_info:
        # add course
        stored_info[course] = []

    if student not in course:
        # add student to course
        stored_info[course].append(student)

# Print User output
for course, student_list in stored_info.items():
    print(f"{course}: {len(student_list)}")
    for student in student_list:
        print(f"-- {student}")