def gather_credits(quota, *course_data):

    courses_history = []
    credits_gathered = 0

    for course, course_credits in course_data:
        if credits_gathered >= quota:
            break
        if course in courses_history:
            continue
        courses_history.append(course)
        credits_gathered += course_credits

    if credits_gathered >= quota:
        return f"""Enrollment finished! Maximum credits: {credits_gathered}.
Courses: {', '.join(sorted(courses_history))}"""
    return f"You need to enroll in more courses! You have to gather {quota - credits_gathered} credits more."


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

