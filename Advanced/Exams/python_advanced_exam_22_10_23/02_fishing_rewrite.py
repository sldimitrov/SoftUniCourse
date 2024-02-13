
# Read the size
size = int(input())


def move(sea, positions, turn, ways):
    # Current coordinates
    current_row, current_col = positions
    # Direction +-
    row_move, col_move = ways[turn][0], ways[turn][1]
    # Future coordinates
    desired_row, desired_col = current_row + row_move, current_col + col_move

    if 0 <= desired_row < size and 0 <= desired_col < size:
        return desired_row, desired_col

    if desired_row >= size:
        desired_row = 0
    elif desired_row < 0:
        desired_row = size - 1

    if desired_col >= size:
        desired_col = 0
    elif desired_col < 0:
        desired_col = size - 1

    return desired_row, desired_col


# Initialise variables
matrix = []
boat_pos = []
collected_fish = 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

# Read the matrix
for row in range(size):
    line = list(input())
    matrix.append(line)
    if 'S' in line:
        boat_pos = [row, matrix[row].index('S')]

# Logic
while True:
    direction = input()
    if direction == 'collect the nets':
        break

    current_row_index, current_col_index = boat_pos

    row, col = move(matrix, boat_pos, direction, directions)

    element = matrix[row][col]
    matrix[row][col] = "S"
    matrix[current_row_index][current_col_index] = '-'
    boat_pos = [row, col]

    if element.isdigit():
        collected_fish += int(element)
    elif element == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
              f" Last coordinates of the ship: [{row},{col}]")
        exit()

if collected_fish >= 20:
    print("Success! You managed to reach the quota!")
else:
    print("You didn't catch enough fish and didn't reach the quota! "
          f"You need {20 - collected_fish} tons of fish more.")

if collected_fish > 0:
    print(f"Amount of fish caught: {collected_fish} tons.")

[print(''.join(row)) for row in matrix]
