import os

# Initialise the name of the file we search for
file = "numbers.txt"
# Find his relative path
path = os.path.join("resources", file)

# Initialise a counter
total_sum = 0

# Open the file -read_only-
with open(path, 'r') as f:
    # For every line in the file
    for line in f.readlines():
        # Add the sum of the number to the total
        total_sum += int(line.strip())

# Print User output
print(total_sum)