import re

# Initialise variables
matrix = []


def move(position, turns, turn):
    pos_1, pos_2 = position

    # Extract the direction
    turn = turn[0]

    # Find the move in the direction
    r_move, c_move = turns[turn][0], turns[turn][1]

    # Move to the new coordinates
    desired_row, desired_col = pos_1 + r_move, pos_2 + c_move

    return desired_row, desired_col


# Initialise directions
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

# Initialise the matrix
for row in range(6):
    matrix.append(input().split())

# Read starting position
starting_pos = input()
starting_pos_numbers = re.findall(r'\d', starting_pos)  # save all the number
starting_pos_numbers = list(map(int, starting_pos_numbers))  # parse them into integers


# Logic
while True:
    command = input()

    if command == 'Stop':
        break

    # Split the command
    command_type, *direction = command.split(', ')

    # Get the new coordinates
    current_row, current_col = move(starting_pos_numbers, directions, direction)

    # Get the current element
    element = matrix[current_row][current_col]

    # Check the command
    if command_type == "Create":
        value = direction[1]
        if element == '.':
            matrix[current_row][current_col] = value

    elif command_type == "Update":
        value = direction[1]
        if element.isalnum():
            matrix[current_row][current_col] = value

    elif command_type == "Delete":
        if element.isalnum():
            matrix[current_row][current_col] = '.'

    elif command_type == "Read":
        if element.isalnum():
            print(element)

    # Save current coordinates
    starting_pos_numbers = [current_row, current_col]

# Print every row of the matrix
[print(*row) for row in matrix]
