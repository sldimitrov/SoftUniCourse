def draw_the_map(length: int):
    """
    This function will read the matrix and will find
    the coordinates of our ship
    :return: list
    """
    matrix, player_pos = [], []
    for row in range(length):
        line = list(input())
        matrix.append(line)
        if 'S' in matrix[row]:
            player_pos = [row, matrix[row].index('S')]

    return matrix, player_pos


def move(matrix, direction, position):

    matrix[position[0]][position[1]] = '-'

    if direction == 'up':
        position[0] -= 1
    elif direction == 'down':
        position[0] += 1
    elif direction == 'left':
        position[1] -= 1
    elif direction == 'right':
        position[1] += 1

    return position


def valid_range(position, length):
    for i in range(2):
        if position[i] > length - 1:
            position[i] = 0
        if position[i] < 0:
            position[i] = length - 1


def handle_whirlpool(pos):
    print("You fell into a whirlpool! The ship sank and you lost the fish you caught."
          f" Last coordinates of the ship: [{pos[0]},{pos[1]}]")


def handle_output(board, vortex, hunt):
    if hunt >= 20:
        print("Success! You managed to reach the quota!")
    elif not vortex:
        lack_of_fish = 20 - hunt
        print(f"You didn't catch enough fish and didn't reach the quota! You need {lack_of_fish} tons of fish more.")

    if hunt:
        print(f"Amount of fish caught: {hunt} tons.")
    if not vortex:
        [print(''.join(row)) for row in board]


# Initialise variables to store info
whirlpool = False
quota = 0

# Read the size of the map
size = int(input())

# Get the matrix and the coordinates of the ship
sea_board, ship_pos = draw_the_map(size)

command = input()
while command != "collect the nets":

    # Move the player
    current_position = move(sea_board, command, ship_pos)
    valid_range(current_position, size)

    curr_el = sea_board[current_position[0]][current_position[1]]

    if curr_el.isdigit():
        quota += int(curr_el)
    elif curr_el == 'W':
        handle_whirlpool(current_position)
        whirlpool = True
        quota = 0
        break

    sea_board[current_position[0]][current_position[1]] = 'S'

    command = input()

handle_output(sea_board, whirlpool, quota)
