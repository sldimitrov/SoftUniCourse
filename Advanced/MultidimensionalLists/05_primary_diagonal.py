row = int(input())

matrix = []

for _ in range(row):
    matrix.append([int(el) for el in input().split()])

diagonal_sum = 0
for row_index in range(row):
    for col_index in range(row):
        if row_index == col_index:
            diagonal_sum += matrix[row_index][col_index]

print(diagonal_sum)