# Read matrix parameters
rows, cols = [int(x) for x in input().split()]

# Read the matrix
matrix = [[int(x) for x in input().split()] for row in range(rows)]

maximum_sum = float(f"-inf")
greater_matrix = []

# Logic
for row in range(0, rows - 2):
    for col in range(0, cols - 2):

        first_row = matrix[row][col:col + 3]
        second_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        # Check if the current_sum is bigger than the maximum
        if current_sum > maximum_sum:
            maximum_sum = current_sum
            greater_matrix = [first_row, second_row, third_row]

# Print User output
print(f"Sum = {maximum_sum}")
[print(*row) for row in greater_matrix]
