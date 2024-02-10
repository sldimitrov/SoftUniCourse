# Read the size
s = int(input())

# Initialise the matrix
matrix = [[int(x) for x in input().split()] for i in range(s)]

# Find the numbers within each diagonal
primary_diagonal = [matrix[r][r] for r in range(s)]
secondary_diagonal = [matrix[r][s - r - 1] for r in range(s)]

# Find the sum of each diagonal
primary_diagonal_sum = sum(primary_diagonal)
secondary_diagonal_sum = sum(secondary_diagonal)

# Calculate the absolute difference between the diagonals
difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

# Print User output
print(difference)