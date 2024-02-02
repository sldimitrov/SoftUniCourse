# Initialise the dictionary
# to store the data in
courses_info = {}

command = input()
# Initialise a While loop
while command != "end":
    course_name, student = command.split(' : ')
    if course_name not in courses_info.keys():
        courses_info[course_name] = []
    courses_info[course_name].append(student)
    command = input()
# Print the output
for key, value in courses_info.items():
    print(f"{key}: {len(courses_info[key])}")
    for name in value:
        print(f"-- {''.join(name)}")
