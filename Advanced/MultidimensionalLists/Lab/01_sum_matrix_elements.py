# Read User input
n_rows, n_cols = [int(x) for x in input().split(', ')]

# Initialise the matrix
matrix = []
total_sum = 0

# Logic
for i in range(n_rows):
    line = [int(x) for x in input().split(', ')]
    matrix.append(line)
    # calculate the numbers and add them to the sum
    total_sum += sum(line)

# Print User output
print(total_sum)
print(matrix)