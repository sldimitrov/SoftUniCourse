# Initialization of the matrix
n = int(input())
matrix = [[int(c) for c in input().split()] for r in range(n)]

# Find the sum of diagonal values
first = 0
second = 0
for r in range(n):
    first += matrix[r][r]
    second += matrix[r][n - r - 1]

# Print User output
print(abs(first - second))