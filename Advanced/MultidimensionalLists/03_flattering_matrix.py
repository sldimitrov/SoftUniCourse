# Read User input
n_rows = int(input())

# Initialise the matrix
matrix = []

# Logic
for i in range(n_rows):
    line = [int(x) for x in input().split(', ')]

# Print User output
print(matrix)
