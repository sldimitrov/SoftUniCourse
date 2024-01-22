# Read User input
row = int(input())

# Initialise matrix
matrix = []

# Read data for the matrix
for _ in range(row):
    matrix.append([int(el) for el in input().split()])

# Initialise a counter
diagonal_sum = 0

# Sum diagonal
for row_index in range(row):
    diagonal_sum += matrix[row_index][row_index]

# Print User output
print(diagonal_sum)
