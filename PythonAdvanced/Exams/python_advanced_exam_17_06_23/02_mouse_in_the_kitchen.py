# Read the size
rows, cols = [int(x) for x in input().split(',')]


def check_valid_indices(r, c):
    return 0 <= r < rows and 0 <= c < cols


def find_mouse(curr_matrix):
    mouse_pos, cookies = (), []
    for c_row in range(rows):
        for c_col in range(cols):
            if curr_matrix[c_row][c_col] == 'M':
                mouse_pos = (c_row, c_col)

            elif curr_matrix[c_row][c_col] == 'C':
                cookies.append((c_row, c_col))

    return mouse_pos, cookies


# Initialise the matrix
matrix = [list(input()) for row in range(rows)]

# Initialise directions
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

# Find the mouse pos and the number of cookies
mouse, biscuits = find_mouse(matrix)
matrix[mouse[0]][mouse[1]] = "*"

while True:
    direction = input()

    if direction == 'danger':
        matrix[mouse[0]][mouse[1]] = 'M'
        print(f"Mouse will come back later!")
        break

    row, col = mouse[0] + directions[direction][0], mouse[1] + directions[direction][1]

    if not check_valid_indices(row, col):
        matrix[mouse[0]][mouse[1]] = "M"
        print(f"No more cheese for tonight!")
        break

    if matrix[row][col] == 'C':
        biscuits.remove((row, col))

        if not biscuits:
            matrix[row][col] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break

        mouse = (row, col)
        matrix[row][col] = '*'

    elif matrix[row][col] == 'T':
        matrix[row][col] = 'M'
        mouse = (row, col)
        print(f"Mouse is trapped!")
        break

    elif matrix[row][col] == "@":
        continue

    mouse = (row, col)

[print(''.join(nested)) for nested in matrix]