def softuni_students(*args, **kwargs):
    course_students = {}
    invalid_students = set()

    for arg in args:
        course_id, username = arg
        if course_id not in kwargs:
            invalid_students.add(username)
        else:
            course_name = kwargs[course_id]
            course_students[username] = course_name

    sorted_students = sorted(course_students.items())

    result = []

    for username, course in sorted_students:
        message = f"*** A student with the username {username} has successfully finished the course {course}!"
        result.append(message)

    if invalid_students:
        message = f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"
        result.append(message)

    return '\n'.join(result)


print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
