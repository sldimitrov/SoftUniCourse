# Read the size of the square matrix
size = int(input())

# Initialise a list
matrix = []

# Add data to the matrix
for i in range(size):
    matrix.append(input())

# Read the searched element
searched_element = input()

# Search for the element in the matrix
for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == searched_element:
            print(f"({row_index}, {col_index})")
            exit()  # exit if found

# else print:
print(f"{searched_element} does not occur in the matrix")

