def gather_credits(number_of_credits_required, *course_data):
    attended_courses_info = []
    credits_gathered = 0

    for course, number_of_credits in course_data:
        if credits_gathered >= number_of_credits_required:
            break
        elif course in attended_courses_info:
            continue
        attended_courses_info.append(course)
        credits_gathered += number_of_credits

    if credits_gathered >= number_of_credits_required:
        return f"""Enrollment finished! Maximum credits: {credits_gathered}.
Courses: {', '.join(sorted(attended_courses_info))}"""
    return (f"You need to enroll in more courses!"
            f" You have to gather {number_of_credits_required - credits_gathered} credits more.")


print(gather_credits(
    80,
    ("Basics", 27),
))


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
