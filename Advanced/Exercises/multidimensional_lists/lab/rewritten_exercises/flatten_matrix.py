# Read the rows
rows = int(input())

# Initialise the matrix
matrix = [input().split(', ') for x in range(rows)]

# Convert the matrix to a list
flattened = [int(num) for row in matrix for num in row]

# Print to the User
print(flattened)
