# Read User input
n_lines = int(input())

students_book = {}

# Logic
for _ in range(n_lines):
    student, grade = input().split()
    if student not in students_book:
        students_book[student] = []
    students_book[student].append(float(grade))

# Print User output
for student, grades in students_book.items():
    average_grade = sum(grades) / len(grades)
    formatted_grades = f"{' '.join([f'{g:.2f}' for g in grades])}"
    print(f"{student} -> {formatted_grades} (avg: {average_grade:.2f})")
