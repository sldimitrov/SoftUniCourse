
# Read size
rows, cols = [int(x) for x in input().split()]


def check_valid_range(p_0, p_1):
    return 0 <= p_0 < rows and 0 <= p_1 < cols


def move(position, turns, turn):

    player_row, player_col = position
    r_move, c_move = turns[turn][0], turns[turn][1]

    desired_row, desired_col = player_row + r_move, player_col + c_move

    return desired_row, desired_col


# Initialise variables
matrix = []
blind_man_pos = []
other_player_positions = []  # matrix

touched_opponents = 0
moved_made = 0
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

# Initialise the matrix
for row_index in range(rows):
    line = input().split()
    matrix.append(line)
    for col_index in range(cols):
        if matrix[row_index][col_index] == 'P':
            other_player_positions.append([row_index, col_index])
        elif matrix[row_index][col_index] == 'B':
            blind_man_pos = [row_index, col_index]

while True:
    direction = input()

    if touched_opponents >= 3:
        break

    if direction == "Finish":
        break

    player_row_index, player_col_index = blind_man_pos
    row, col = move(blind_man_pos, directions, direction)


    # check valid range
    if not check_valid_range(row, col):
        continue

    element = matrix[row][col]
    # remove the coordinates if there is player
    if element == 'O':
        continue

    if element == 'P':
        moved_made += 1
        touched_opponents += 1

        matrix[row][col] = 'B'
        blind_man_pos = [row, col]
        other_player_positions.remove([row, col])
        matrix[player_row_index][player_col_index] = '-'

    elif element == '-':
        moved_made += 1
        matrix[row][col] = 'B'
        blind_man_pos = [row, col]
        matrix[player_row_index][player_col_index] = '-'

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moved_made}")
