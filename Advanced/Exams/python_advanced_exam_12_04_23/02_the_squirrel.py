from collections import deque

# Read size
SIZE = int(input())
# Read a list with the directions
list_with_direction = deque(input().split(', '))
# Initialise directions
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def is_valid_coords(check_row, check_col):
    return 0 <= check_row < SIZE and 0 <= check_col < SIZE


def move(board, positions, turns, turn):

    r, c = positions

    r_move, c_move = turns[turn][0], turns[turn][1]

    desired_row, desired_col = r + r_move, c + c_move

    return desired_row, desired_col


# Initialise variables
matrix = []
squirrel_pos = []
is_trapped = False
is_out_of_bounds = False
is_won = False
hazelnuts = 0

# Initialise matrix
for row in range(SIZE):
    line = list(input())
    matrix.append(line)
    if 's' in line:
        squirrel_pos = [row, matrix[row].index('s')]

# Logic
while True:
    if not list_with_direction:  # if there are no more commands
        break

    direction = list_with_direction.popleft()

    # Save the last coordinates
    row_index, col_index = squirrel_pos

    # Get the desired coordinates
    current_row, current_col = move(matrix, squirrel_pos, directions, direction)

    if not (is_valid_coords(current_row, current_col)):  # if the coordinates are out of bounds
        is_out_of_bounds = True
        break

    # Get the current element of the position
    element = matrix[current_row][current_col]

    if element == 'h':
        hazelnuts += 1

        if hazelnuts >= 3:
            is_won = True
            break

    elif element == 't':
        is_trapped = True
        break

    squirrel_pos = (current_row, current_col)

if is_out_of_bounds:
    print("The squirrel is out of the field.")
elif is_trapped:
    print("Unfortunately, the squirrel stepped on a trap...")
elif not is_won:
    print("There are more hazelnuts to collect.")
elif is_won:
    print("Good job! You have collected all hazelnuts!")

print(f"Hazelnuts collected: {hazelnuts}")

