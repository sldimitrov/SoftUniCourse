# Read the size of square matrix
size = int(input())

# Initialise the size of matrix with zero values
matrix = [[0] * size for i in range(0, size)]

# Change the values
for x in range(0, size):
    line = [str(x) for x in input()]
    for y in range(0, size):
        matrix[x][y] = line[y]

# Read the special symbol
special_symbol = input()

# Check for special symbol occurrence
special_symbol_coords = ''
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == special_symbol:
            special_symbol_coords = f'({row}, {col})'

# Print User output
print(special_symbol_coords if special_symbol_coords
      else f'{special_symbol} does not occur in the matrix')
