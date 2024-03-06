# Read the matrix parameters
rows, cols = [int(x) for x in input().split(', ')]

# Initialise variables
matrix = []
total_sum = 0

# Logic
for row in range(rows):
    line = [int(x) for x in input().split(', ')]  # each list
    matrix.append(line)  # append to the matrix
    total_sum += sum(line)  # add its sum to the total

# Print User output
print(total_sum)
print(matrix)