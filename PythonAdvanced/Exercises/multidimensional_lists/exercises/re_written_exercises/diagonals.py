# First solution

# # Read the size of the matrix
# size = int(input())
#
# # Read the matrix
# matrix = [[int(x) for x in input().split(', ')] for row in range(size)]
#
# # Initialise variables
# primary_diagonal, secondary_diagonal = 0, 0
# primary_diagonal_nums, secondary_diagonal_nums = [], []
#
# # Find the sum of each diagonal
# counter = size - 1
# for row in range(size):
#     # Sum the primary diagonal
#     column = row
#     number = matrix[row][column]
#     primary_diagonal += number
#     primary_diagonal_nums.append(number)
#     # Sum the secondary diagonal
#     second_number = matrix[row][counter]
#     secondary_diagonal += second_number
#     secondary_diagonal_nums.append(second_number)
#     counter -= 1
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal_nums)}. Sum: {primary_diagonal}")
# print(f"Secondary diagonal: {', '.join(str(y) for y in secondary_diagonal_nums)}. Sum: {secondary_diagonal}")

# Second solution
# Read the size
n = int(input())

# Read the matrix lines
matrix = [[int(x) for x in input().split(', ')] for row in range(n)]

# Find the primary diagonal numbers
primary_diagonal = [matrix[x][x] for x in range(n)]
# Find the secondary diagonal numbers
secondary_diagonal = [matrix[x][n - x - 1] for x in range(n)]

# Print User output
print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(y) for y in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")


