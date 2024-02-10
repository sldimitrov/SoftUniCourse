# Read rows
rows = int(input())

# Initialise a variable
matrix = []

# Logic
for row in range(rows):
    # Read every line - only the even numbers
    line = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    # Append each line to the matrix
    matrix.append(line)

# Print User output
print(matrix)
