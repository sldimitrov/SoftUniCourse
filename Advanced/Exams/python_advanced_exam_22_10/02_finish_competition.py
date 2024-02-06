import string


def transfer_ship_abroad(p_0, p_1):
    if p_0 < 0:
        p_0 = size
    elif p_0 >= size:
        p_0 = 0
    if p_1 < 0:
        p_1 = size
    elif p_1 >= size:
        p_1 = 0
    return p_0, p_1


directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1],
}

# Read User input - length
size = int(input())
# Initialise variables the matrix and the player coordinates
player_pos = []
matrix = []

# Read the Matrix
for row in range(size):
    line = list(input())
    matrix.append(line)
    if 'S' in matrix[row]:
        player_pos = [row, matrix[row].index('S')]
        matrix[player_pos[0]][player_pos[1]] = '-'

# The quota is 20tons of fish
QUOTA = 20
tons_fish_collected = 0
is_drowned = False

# Logic
command = input()
while command != "collect the nets":
    pos_0 = player_pos[0] + directions[command][0]
    pos_1 = player_pos[1] + directions[command][1]

    pos_0, pos_1 = transfer_ship_abroad(pos_0, pos_1)

    position = matrix[pos_0][pos_1]

    if position in string.digits:
        tons_fish_collected += int(position)

    elif position == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{pos_0},{pos_1}]")
        tons_fish_collected = 0
        is_drowned = True
        break
        # whirlpool

    player_pos[0], player_pos[1] = pos_0, pos_1
    matrix[pos_0][pos_1] = '-'

    command = input()


matrix[pos_0][pos_1] = 'S'

if not is_drowned:
    if tons_fish_collected >= QUOTA:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {QUOTA - tons_fish_collected}"
              f" tons of fish more.")

if tons_fish_collected:
    print(f"Amount of fish caught: {tons_fish_collected} tons.")

if not is_drowned:
    [print(''.join(row)) for row in matrix]
