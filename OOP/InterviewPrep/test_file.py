import os

path = os.path.join(r"D:\github_repositories\SoftUniCourse\OOP\InterviewPrep\text.txt")

try:
    os.remove(path)
except FileNotFoundError as f:
    print(f)
else:
    print(f"File was successfully removed.")
finally:
    print(f"Final statement..")
