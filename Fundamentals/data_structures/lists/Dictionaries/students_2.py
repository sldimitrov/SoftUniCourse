students = []
course_to_search = None

while True:
    command = input()
    if ':' not in command:
        course_to_search = command
        break

    name, ID, course = command.split(':')
    students.append({'name': name, 'ID': ID, 'course': course})

for student in students:
    if student['course'].startswith(course_to_search[:3]):
        print(f"{student['name']} - {student['ID']}")