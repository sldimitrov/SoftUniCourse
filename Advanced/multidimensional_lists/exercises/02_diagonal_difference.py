# # Initialization of the matrix
# n = int(input())
# matrix = [[int(c) for c in input().split()] for r in range(n)]
#
# # Find the sum of diagonal values
# first = 0
# second = 0
# for r in range(n):
#     first += matrix[r][r]
#     second += matrix[r][n - r - 1]
#
# # Print User output
# print(abs(first - second))


# sol 2
n = int(input())

primary, secondary = 0, 0

for i in range(n):
    line = [int(x) for x in input().split()]
    primary += line[i]
    secondary += line[n - i - 1]

print(abs(primary - secondary))