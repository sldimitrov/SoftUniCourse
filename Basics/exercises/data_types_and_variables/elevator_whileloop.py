# Read User input
people = int(input())
capacity = int(input())
courses = 0
# Logic
while people > 0:
    people -= capacity
    courses += 1
print(courses)
# Print User output