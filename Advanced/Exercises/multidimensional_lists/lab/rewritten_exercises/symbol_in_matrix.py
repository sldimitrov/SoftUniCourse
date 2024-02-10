# Read the size
size = int(input())
# Initialise the matrix
matrix = []

# Logic
for i in range(size):
    matrix.append(input())

# Read the searched symbol
searched_symbol = input()

# Iterate over the matrix
for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == searched_symbol:  # check for matches
            # Print the coordinates of the symbol
            print(f"({row_index}, {col_index})")
            exit()  # Exit

# Print the case where we don't have occurrences
print(f"{searched_symbol} does not occur in the matrix")
