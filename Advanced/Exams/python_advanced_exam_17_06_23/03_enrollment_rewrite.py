def gather_credits(number_of_credits_needed, *courses_info):
    enrolled_courses = []
    total_credits_gathered = 0

    for course, number_of_credits in courses_info:
        if total_credits_gathered >= number_of_credits_needed:
            break
        elif course in enrolled_courses:
            continue
        enrolled_courses.append(course)
        total_credits_gathered += number_of_credits

    if total_credits_gathered >= number_of_credits_needed:
        return f"""Enrollment finished! Maximum credits: {total_credits_gathered}.
Courses: {', '.join(sorted(enrolled_courses))}"""
    return (f"You need to enroll in more courses! You have to gather"
            f" {number_of_credits_needed - total_credits_gathered} credits more.")


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
