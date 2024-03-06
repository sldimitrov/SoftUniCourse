# Read the range of the matrix
n = int(input())
# Use list comprehension to initialise the matrix
matrix = [[int(y) for y in input().split(', ')] for x in range(n)]
# Find the diagonals
primary = [matrix[r][r] for r in range(n)]
secondary = [matrix[r][n - r - 1] for r in range(n)]
# Print diagonals data
print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")

