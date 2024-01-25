# Read data and initialise the matrix
matrix = [[int(x) for x in i.split()] for i in input().split('|')]

# Print the matrix backwards
[print(*sub_matrix, sep=' ') for sub_matrix in matrix[::-1]]