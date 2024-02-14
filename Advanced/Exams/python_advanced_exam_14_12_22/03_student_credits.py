
def students_credits(*courses_info):

    # Initialise variables
    course_book = {}
    credits_gathered = 0
    is_graduated = False

    # Iterate through the course data
    for course in courses_info:
        name, course_credits, max_points, our_points = course.split('-')

        # Calculate the credits for each course
        delimiter = int(our_points) / int(max_points)
        course_credits = int(course_credits) * delimiter

        # Save info for the attended course and its credits
        course_book[name] = course_credits

        # Check if Deyan graduate
        credits_gathered += course_credits
        if credits_gathered >= 240:
            is_graduated = True

    # Initialise a variable for the function return
    result = []

    # Append message about graduating to the result
    if is_graduated:
        result.append(f"Diyan gets a diploma with {credits_gathered:.1f} credits.")
    else:
        result.append(f"Diyan needs {240 - credits_gathered:.1f} credits more for a diploma.")
    sorted_courses = sorted(course_book.items(), key=lambda x: -x[1])

    # Append every course
    for course, credits in sorted_courses:
        result.append(f"{course} - {credits:.1f}")

    return '\n'.join(result)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
