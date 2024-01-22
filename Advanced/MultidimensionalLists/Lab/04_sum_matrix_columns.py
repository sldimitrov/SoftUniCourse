n_rows, n_cols = [int(x) for x in input().split(', ')]

matrix = []

for row in range(n_rows):
    sub_list = []
    line = input().split()
    for el in line:
        sub_list.append(int(el))
    matrix.append(sub_list)

total_cols = 0

for col in range(n_cols):
    current_sum = 0
    for row in range(n_rows):
        current_sum += matrix[row][col]
    total_cols += current_sum
    print(current_sum)

