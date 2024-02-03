def softuni_students(*args, **kwargs):
    course_students = {}
    invalid_students = set()

    for arg in args:
        course_id, student_name = arg
        if course_id not in kwargs:
            invalid_students.add(student_name)
        else:
            course_name = kwargs[course_id]
            course_students[student_name] = course_name

    sorted_students = sorted(course_students.items())

    result = []

    for student, course in sorted_students:
        result.append(f"*** A student with the username {student} has successfully finished the course {course}!")

    if invalid_students:
        message = f"!!! Invalid course students: {', '.join(invalid_students)}"
        result.append(message)

    return '\n'.join(result)


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
