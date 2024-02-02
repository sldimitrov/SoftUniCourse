# Read User input
n_rows = int(input())

# Initialise the matrix
flatten = []

# Logic
for i in range(n_rows):
    line = [int(x) for x in input().split(', ')]
    flatten.extend(line)  # unpack a list

# Print User output
print(flatten)

