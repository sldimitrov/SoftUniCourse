# Read User input
n_rows, n_cols = [int(x) for x in input().split(', ')]
size = int(input())
matrix = []

for i in range(n_rows):
    line = [int(x) for x in input().split(', ')]
    sub_list = []
    for j in line:
        sub_list.append(j)
    matrix.append(sub_list)

biggest_sum = float('-inf')
sub_matrix = []  # and sub matrix

# Iterate through the valid range of the matrix
for row in range(n_rows - (size - 1)):
    for col in range(n_cols - size):
        # Initialise variables for the square corners
        current_space = matrix[row][col]
        right_space = matrix[row][col + 1]
        down_space = matrix[row +1][col]
        diagonal_space = matrix[row +1][col + 1]
        # Calculate the sum of its numbers
        current_sum = current_space + right_space + down_space + diagonal_space
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            sub_matrix = [[current_space, right_space], [down_space, diagonal_space]]

# Print User output
for matrix in sub_matrix:
    print(*matrix)
print(biggest_sum)
# TODO: find a way to make it work with n square
