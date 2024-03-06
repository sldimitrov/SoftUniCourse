# Read User input
n_rows, n_cols = [int(x) for x in input().split(', ')]
# The size of the square we will search within
size = int(input())
matrix = []

for i in range(n_rows):
    line = [int(x) for x in input().split(', ')]
    sub_list = []
    for j in line:
        sub_list.append(j)
    matrix.append(sub_list)

biggest_sum = float('-inf')
highest_score_matrix = []

# Iterate through the valid range of the matrix
for row in range(n_rows - (size - 1)):
    for col in range(n_cols - (size - 1)):
        # Initialise variables for the sub matrix
        current_cell = matrix[row][col]
        sub_matrix = []
        current_sum = 0
        for r in range(size):
            matrix_line = []
            for c in range(size):
                matrix_line.append(matrix[r][c])
                current_sum += matrix[r][c]
            sub_matrix.append(matrix_line)

        if current_sum > biggest_sum:
            biggest_sum = current_sum
            highest_score_matrix = sub_matrix

# Print User output
for matrix in highest_score_matrix:
    print(*matrix)
print(biggest_sum)
