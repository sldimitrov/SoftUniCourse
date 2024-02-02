# Initialise the matrix
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[print(*row) for row in mat]

print()

# Get the transpose of a matrix
res = [[row[i] for row in mat] for i in range(len(mat[0]))]
# Print to the user
[print(*row) for row in res]
