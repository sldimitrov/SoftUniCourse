# Read matrix params
rows, cols = [int(x) for x in input().split(', ')]

# Initialise a variable for the matrix
matrix = []

# Logic
for row in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)

# Iterate though every column
for c in range(cols):
    sum_of_current_column = 0  # calculate its values
    for r in range(rows):
        sum_of_current_column += matrix[r][c]
    print(sum_of_current_column)  # and print them to the User



