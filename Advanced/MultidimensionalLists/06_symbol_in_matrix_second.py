size = int(input())

matrix = []

for i in range(size):
    matrix.append(input())

searched_element = input()

is_found = False

for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == searched_element:
            print(f"({row_index}, {col_index})")
            break
    if is_found:
        break

if not is_found:
    print(f"{searched_element} does not occur in the matrix")

