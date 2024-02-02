from math import ceil
# Read User input
people = int(input())
capacity = int(input())
# Logic
courses = ceil(people / capacity)
print(courses)
# Print User output