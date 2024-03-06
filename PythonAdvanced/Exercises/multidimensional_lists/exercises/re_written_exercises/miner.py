# Read the size of the matrix
SIZE = int(input())

def are_valid_coordinates(r, c) -> bool:
    # Return if they are valid or not
    return 0 <= r < SIZE and 0 <= c < SIZE


# Initialise variables
matrix = []
starting_row, starting_col = 0, 0
coal_left_to_find = 0

# Initialise directions
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def move_player(table, direction, cur_row, cur_col):
    # Extract the coordinates from the given direction
    coordinates = directions[direction]

    # Unpack the coordinates of the direction
    p_row, p_col = coordinates

    # Get future coordinates
    next_row, next_col = (
        cur_row + p_row,
        cur_col + p_col
    )

    # Validate these coordinates
    if are_valid_coordinates(next_row, next_col):
        return next_row, next_col
    return ''


# Save each command in a list
command_list = input().split()

# Read the matrix
for row in range(SIZE):
    line = input().split()

    matrix.append(line)  # append each line to the matrix

    if 'c' in line:  # save the number of coal ores
        coal_left_to_find += matrix[row].count('c')

    if 's' in line:  # save the player position
        current_row = row
        current_col = matrix[row].index('s')

# Logic
for turn in command_list:

    try:  # to the player in the given direction
        current_row, current_col = move_player(matrix, turn, current_row, current_col)
    except ValueError:  # if the coordinates are invalid
        continue

    # Search for the current element in the matrix
    element = matrix[current_row][current_col]

    if element == '*':  # continue
        continue

    if element == 'c':  # contain coal
        coal_left_to_find -= 1
        if coal_left_to_find == 0:
            print(f"You collected all coal! ({current_row}, {current_col})")
            break

    elif element == 'e':  # exit
        print(f"Game over! ({current_row}, {current_col})")
        exit()

# if there are no more turns
if coal_left_to_find > 0:  # but there is still coal to find
    print(f"{coal_left_to_find} pieces of coal left. ({current_row}, {current_col})")




