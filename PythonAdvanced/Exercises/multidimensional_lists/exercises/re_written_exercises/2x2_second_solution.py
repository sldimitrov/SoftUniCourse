rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for row in range(rows)]

counter_of_squares = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        element = matrix[row][col]

        if element == matrix[row + 1][col] and element == matrix[row][col + 1] and element == matrix[row + 1][col + 1]:
            counter_of_squares += 1

print(counter_of_squares)