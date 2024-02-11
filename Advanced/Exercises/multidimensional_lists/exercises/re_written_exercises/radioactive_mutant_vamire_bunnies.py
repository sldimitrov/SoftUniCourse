
# Read the size of the matrix
ROWS, COLS = [int(x) for x in input().split()]


def are_valid_coordinates(pos_0, pos_1):
    return 0 <= pos_0 < ROWS and 0 <= pos_1 < COLS


# Initialise variables
player_pos = []
matrix = []
bunny_positions = []
bunny_expansion = 0


STRAIGHTS = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1],
}

DIAGONALS = {
    "up-right": [-1, 1],
    "down-right": [1, 1],
    "down-left": [1, -1],
    "up-left": [-1, -1],
}


def expand_died_cells(sign, current_r, current_c, expansion_level):
    if sign == 'up-right':
        died_cell_r_1, died_cell_c_1 = current_r - 1, current_c
        died_cell_r_2, died_cell_c_2 = current_r, current_c + 1

    elif sign == 'down-right':
        died_cell_r_1, died_cell_c_1 = current_r + 1, current_c
        died_cell_r_2, died_cell_c_2 = current_r, current_c + 1

    elif sign == 'down-left':
        died_cell_r_1, died_cell_c_1 = current_r, current_c - 1
        died_cell_r_2, died_cell_c_2 = current_r + 1, current_c

    elif sign == 'up-left':
        died_cell_r_1, died_cell_c_1 = current_r - 1, current_c
        died_cell_r_2, died_cell_c_2 = current_r, current_c - 1

    if are_valid_coordinates(died_cell_r_1, died_cell_c_1):
        matrix[died_cell_r_1][died_cell_c_1] = 'B'

    if are_valid_coordinates(died_cell_r_2, died_cell_c_2):
        matrix[died_cell_r_2][died_cell_c_2] = 'B'

    return matrix


def expand_diagonals(expansion_level, coordinates, current_r, current_c):
    for jump in range(expansion_level):  # current coordinates of the expansion
        step_r, step_c = coordinates  # the coordinates of the given direction

        current_r += step_r
        current_c += step_c

        # Expand the bunny on the given cell
        if are_valid_coordinates(current_r, current_c):
            matrix[current_r][current_c] = 'B'

        return current_r, current_c



def expand_bunnies(matrix, positions, expansion_level):
    """
    This function expands each bunny in the matrix in every direction progressively.
    :param garden: multidimensional list
    :param positions: M-list
    :param expansion_level: int
    :return: multidimensional-L
    """
    # FOR EACH BUNNY
    for bunny_pos in positions:
        r, c = bunny_pos  # original coordinates of the bunny

        # MOVE EACH BUNNY TO THE SIDES
        for side, coordinates in STRAIGHTS.items():
            current_r, current_c = r, c
            for jump in range(1):  # current coordinates of the expansion
                step_r, step_c = coordinates  # the coordinates of the given direction

                # Expand on base expansion level
                if side == 'U':
                    step_r -= expansion_level
                elif side == 'D':
                    step_r += expansion_level
                elif side == 'L':
                    step_c -= expansion_level
                elif side == 'R':
                    step_c += expansion_level

                # Get the next cell coordinates
                current_r += step_r
                current_c += step_c

                # Expand the bunny on the given cell
                if are_valid_coordinates(current_r, current_c):
                    matrix[current_r][current_c] = 'B'

        # MOVE EACH BUNNY TO THE DIAGONALS
        for side, coordinates in DIAGONALS.items():
            current_r, current_c = r, c
            expand_diagonals(expansion_level, coordinates, current_r, current_c)

        if expansion_level >= 2:
            for side, coordinates in DIAGONALS.items():
                current_r, current_c = r, c
                step_r, step_c = coordinates
                current_r += step_r
                current_c += step_c
                matrix = expand_died_cells(side, current_r, current_c, expansion_level)

    return matrix


def move_player(board, player_position, direction):
    # Get the coordinates for the given direction
    direction_coords = STRAIGHTS[direction]

    # Unpack coordinates
    player_row, player_col = player_position
    dir_row, dir_col = direction_coords

    current_r, current_c = player_row + dir_row, player_col + dir_col

    if are_valid_coordinates(current_r, current_c):
        if board[current_r][current_c] != 'B':
            board[current_r][current_c] = 'P'

            if board[player_row][player_col] != 'B':
                board[player_row][player_col] = '.'
            player_position = [current_r, current_c]
            return player_position
        else:
            handle_lost(current_r, current_c)
    else:
        board[player_row][player_col] = '.'
        handle_win(player_row, player_col, current_r, current_c)


def handle_lost(r, c):
    [print(''.join(r)) for r in matrix]
    print(f"dead: {r} {c}")
    exit()


def handle_win(last_r, last_c, r, c):
    if not (0 <= r < ROWS and 0 <= c < COLS):
        [print(''.join(r)) for r in matrix]
        print(f"won: {last_r} {last_c}")
        exit()


# Read the matrix
for row in range(ROWS):
    line = list(input())
    matrix.append(line)
    # Save the position of each bunny
    if line.count('B') > 1:
        for el_index in range(len(line)):
            if line[el_index] == 'B':
                bunny_positions.append([row, el_index])
    elif line.count('B') == 1:
        bunny_positions.append([row, matrix[row].index('B')])

    # Save the position of the player
    if 'P' in line:
        player_pos = [row, matrix[row].index('P')]

# Read the given directions
list_of_turns = list(input())

for turn in list_of_turns:
    # Expand each bunny
    matrix = expand_bunnies(matrix, bunny_positions, bunny_expansion)
    # Increase the level of expansion by each turn
    bunny_expansion += 1

    # Move the player
    player_pos = move_player(matrix, player_pos, turn)


