
# Read the size of the matrix
size = int(input())


def is_valid_range(p_0: int, p_1: int) -> bool:
    """
    This function take two params and check if they are in the range
    of the matrix of if they are not.
    """
    return 0 <= p_0 < size and 0 <= p_1 < size


def move(position: list, turns: dict, turn: str) -> int:
    """
    This function take a position and a given direction and returns
    the new position moved in the desired direction
    """

    # Unpack the coordinates
    r, c = position
    # Extract the direction coordinates
    r_move, c_move = turns[turn][0], turns[turn][1]
    # Concatenate the coordinates
    desired_row, desired_col = r + r_move, c + c_move

    return desired_row, desired_col


# Initialise variables
matrix = []
ships_pos = []
submarine_pos = []
submarine_damage = 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


# Initialise the matrix
for row in range(size):
    line = list(input())
    matrix.append(line)
    for col in range(size):
        if matrix[row][col] == 'S':
            submarine_pos = [row, col]
        elif matrix[row][col] == 'C':
            ships_pos.append([row, col])

# Logic
while True:
    # Read User input
    direction = input()

    # Save the last position
    row_index, col_index = submarine_pos

    # Get the position with the desired direction
    current_row, current_col = move(submarine_pos, directions, direction)

    # Check if the new coordinates are within the valid range of the matrix
    if not is_valid_range(current_row, current_col):
        print('Out of range')
        continue

    # Get the element of the new coordinates
    element = matrix[current_row][current_col]

    # Check what is the element
    if element == '-':
        submarine_pos = [current_row, current_col]

    elif element == '*':
        submarine_pos = [current_row, current_col]
        submarine_damage += 1

        if submarine_damage >= 3:
            matrix[current_row][current_col] = 'S'
            matrix[row_index][col_index] = '-'
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{current_row}, {current_col}]!")
            break

    elif element == 'C':
        submarine_pos = [current_row, current_col]
        ships_pos.remove([current_row, current_col])

        if not ships_pos:
            matrix[current_row][current_col] = 'S'
            matrix[row_index][col_index] = '-'
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    matrix[current_row][current_col] = 'S'
    matrix[row_index][col_index] = '-'

# Print User output
[print(''.join(row)) for row in matrix]


