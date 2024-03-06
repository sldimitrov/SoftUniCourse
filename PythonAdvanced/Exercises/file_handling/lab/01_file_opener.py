import os

# We initialise relative path like so
# path = os.path.join("resources", "text.txt")

# Find the absolute current path
ABSOLUTE_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# The name of the file we search for
file = 'text.txt'
# Drive the cursor into its path
path = os.path.join("..", "..", file)


try:
    open(path, 'r')  # open the file for reading
    print("File found")

# throws an exception if the file cannot be found
except FileNotFoundError:
    print("File not found")
