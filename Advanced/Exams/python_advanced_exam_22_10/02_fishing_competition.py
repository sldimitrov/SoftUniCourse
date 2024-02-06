def initialise_finish_map(size):
    matrix = []
    player_pos = []
    for row in range(size):
        line = list(input())
        matrix.append(line)
        if 'S' in matrix[row]:
            player_pos = [row, matrix[row].index('S')]

    return matrix, player_pos


def move(matrix, position, direction):
    # Change last position with dash
    row, col = position
    matrix[row][col] = '-'

    # Move the ship in the current direction
    if direction == 'up':
        position[0] -= 1
    elif direction == 'down':
        position[0] += 1
    elif direction == 'right':
        position[1] += 1
    elif direction == 'left':
        position[1] -= 1

    return position


def check_boundaries(coordinates, length):
    for i in range(2):
        if coordinates[i] < 0:
            coordinates[i] = length - 1
        if coordinates[i] >= length:
            coordinates[i] = 0


def handle_whirlpool(position):
    pos_1, pos_2 = position
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
          f" Last coordinates of the ship: [{pos_1},{pos_2}]")


def handle_results(tons_of_fish, vortex, fishing_map):
    if tons_of_fish >= 20:
        print("Success! You managed to reach the quota!")
    elif not vortex:
        lack = 20 - tons_of_fish
        print(f"You didn't catch enough fish and didn't reach the quota! You need {lack} tons of fish more.")

    if tons_of_fish > 0:
        print(f"Amount of fish caught: {tons_of_fish} tons.")

    if not vortex:
        for row in fishing_map:
            print("".join(row))


size = int(input())
fishing_range, ship_pos = initialise_finish_map(size)
quota = 0
whirlpool = False


while True:
    command = input()

    if command == 'collect the nets':
        break

    current_position = move(fishing_range, ship_pos, command)
    check_boundaries(current_position, size)

    current_char = fishing_range[current_position[0]][current_position[1]]

    if current_char.isdigit():
        quota += int(current_char)
    elif current_char == 'W':
        handle_whirlpool(current_position)
        whirlpool = True
        quota = 0
        break
    fishing_range[current_position[0]][current_position[1]] = 'S'

handle_results(quota, whirlpool, fishing_range)
