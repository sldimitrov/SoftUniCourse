# read the size of the square matrix
size = int(input())

# Initialise the matrix
matrix = [[0] * size for row in range(0, size)]

for x in range(0, size):
    line = list(map(int, input().split()))
    for y in range(0, size):
        matrix[x][y] = line[y]

counter = size - 1
reversed_diagonal = 0
for row in range(0, size):
    for col in range(size - 1, -1, -1):
        if col == counter:
            reversed_diagonal += matrix[row][col]
    counter -= 1

# Print User output
print(reversed_diagonal)
