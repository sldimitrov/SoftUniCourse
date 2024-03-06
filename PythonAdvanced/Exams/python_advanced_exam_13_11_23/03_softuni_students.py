# *args is used for passing a variable number of non-keyword arguments,
# while **kwargs is used for passing a variable number of keyword arguments

# Define a function
def softuni_students(*args, **kwargs):
    # Initialise variables
    course_students = {}
    invalid_students = set()

    # For each non-keyword argument
    for arg in args:
        course_id, username = arg  # unpack set of the id and name
        # check if the course is not in kwargs
        if course_id not in kwargs:
            invalid_students.add(username)  # add the student to the invalid ones
        else: # in case the id is there
            course_name = kwargs[course_id]  # take the course name from the kwargs with the id
            course_students[username] = course_name  # add the student to the dict with the name of his course

    # Sort each student alphabetically
    sorted_students = sorted(course_students.items())

    # Initialise a list for the return
    result = []

    # Iterate through the tuple of sorted students and append each one with his course into the result
    for username, course in sorted_students:
        message = f"*** A student with the username {username} has successfully finished the course {course}!"
        result.append(message)

    # In case there are invalid students sort and join them into a message appending them to the result
    if invalid_students:
        message = f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"
        result.append(message)

    # Return every row on a new line
    return '\n'.join(result)


print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))

# *args is used for passing a variable number of non-keyword arguments,
# while **kwargs is used for passing a variable number of keyword arguments

# add a comment here

