def move(matrix, direction, pos) -> list:
    future_pos = [pos[0], pos[1]]
    if direction == 'up':
        future_pos[0] -= 1
    elif direction == 'down':
        future_pos[0] += 1
    elif direction == 'left':
        future_pos[1] -= 1
    elif direction == 'right':
        future_pos[1] += 1

    valid_boundaries(future_pos, row_len, col_len)
    if matrix[future_pos[0]][future_pos[1]] != '*':
        pos = future_pos
    return pos


def valid_boundaries(pos, r, c):
    curr_row, curr_col = pos
    return 0 <= curr_row < r and 0 <= curr_col < c


# Read the size of the matrix
row_len, col_len = [int(x) for x in input().split()]

# Initialise a boolean
is_out = False

# Save the matrix and the position of the boy
neighborhood = []
boy_pos = []
for row in range(row_len):
    line = list(input())
    neighborhood.append(line)
    if 'B' in neighborhood[row]:
        boy_pos = [row, neighborhood[row].index('B')]

position = [boy_pos[0], boy_pos[1]]

while True:
    command = input()

    position = move(neighborhood, command, position)

    if not valid_boundaries(position, row_len, col_len):
        is_out = True
        break

    row, col = position
    element = neighborhood[row][col]

    if element == '*':
        continue
    elif element == 'P':
        neighborhood[row][col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
    elif element == 'A':
        neighborhood[row][col] = 'P'
        break
    else:
        neighborhood[position[0]][position[1]] = '.'

if is_out:
    neighborhood[boy_pos[0]][boy_pos[1]] = ' '
    print("The delivery is late. Order is canceled.")
else:
    print("Pizza is delivered on time! Next order...")

[print(''.join(row)) for row in neighborhood]



