
# Read the size of the matrix
rows, cols = [int(x) for x in input().split()]


def are_valid_coordinates(pos_0, pos_1):
    return 0 <= pos_0 < rows and 0 <= pos_1 < cols


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


def expand_bunnies(garden, positions, expansion_level):
    # EACH BUNNY
    for bunny_pos in positions:
        r, c = bunny_pos  # original coordinates of the bunny

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
                    garden[current_r][current_c] = 'B'

    return garden


# Read the matrix
for row in range(rows):
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
    bunny_expansion += 1
    # Move the player

[print(*row) for row in matrix]
