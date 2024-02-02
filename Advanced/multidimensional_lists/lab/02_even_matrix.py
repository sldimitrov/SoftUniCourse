# Read User input
row_count = int(input())

# Initialise the matrix
matrix = []

# Logic
for i in range(row_count):
    data = [int(el) for el in input().split(', ') if int(el) % 2 == 0]
    matrix.append(data)

# Print User output
print(matrix)
