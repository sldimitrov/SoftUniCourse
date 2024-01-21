# Read User input
rows_count = int(input())
matrix = [map(int, input().split(', ')) for _ in range(rows_count)]
# Flatten the matrix
flattened = [num for row in matrix for num in row]
# Print User output
print(flattened)
