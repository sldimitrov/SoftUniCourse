# Read parameters
n_rows, n_cols = [int(x) for x in input().split()]

# Initialise the matrix
matrix = [[int(y) for y in input().split()] for x in range(n_rows)]

# Initialise the variables for the output
max_sum = float('-inf')
sub_matrix = []

# Logic
for row in range(n_rows - 2):  # loop through the matrix in valid range
    for col in range(n_cols - 2):
        upper_line = matrix[row][col:col + 3]
        middle_line = matrix[row + 1][col:col + 3]
        down_line = matrix[row + 2][col:col + 3]
        # 3*3 square sum
        current_sum = sum(upper_line) + sum(middle_line) + sum(down_line)

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [upper_line, middle_line, down_line]

# Print User output
print(f"Sum = {max_sum}")
[print(*row) for row in sub_matrix]