# Initialise the matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_index_to_change, col_index_to_change = 1, 1

matrix[row_index_to_change][col_index_to_change] = 100

# Logic
for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if row_index_to_change == row_index and col_index_to_change == col_index:
            matrix[row_index][col_index] = 100

