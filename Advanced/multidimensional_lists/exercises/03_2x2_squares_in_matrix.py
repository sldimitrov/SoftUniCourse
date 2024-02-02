# Read parameters
n_rows, n_cols = [int(x) for x in input().split()]

# Initialise the matrix
matrix = [[c for c in input().split()] for r in range(n_rows)]

# Initialise a counter fo the 2x2 squares
square_counter = 0

# Logic
for r in range(n_rows - 1):
    for c in range(n_cols - 1):
        current_cell = matrix[r][c]
        right_cell = matrix[r][c + 1]
        down_cell = matrix[r + 1][c]
        diagonal_cell = matrix[r + 1][c + 1]
        if current_cell == right_cell and current_cell == right_cell \
                and current_cell == down_cell and current_cell == diagonal_cell:
            square_counter += 1

# Print User output
print(square_counter)
