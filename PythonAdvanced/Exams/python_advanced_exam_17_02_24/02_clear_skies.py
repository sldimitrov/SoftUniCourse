
# Read the size of the matrix
size = int(input())


def move(position, turns, turn):
    # Unpack the coordinates
    r, c = position

    # Search for the direction coordinates
    r_move, c_move = turns[turn]

    # Calculate the desired coordinates
    desired_row, desired_col = r + r_move, c + c_move

    return desired_row, desired_col


# Initialise variables
matrix = []
jet_position = []
enemy_positions = []
jet_armor = 300
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

# Read the matrix
for row in range(size):
    line = list(input())  # read every line
    matrix.append(line)
    for col in range(size):
        if matrix[row][col] == 'J':
            jet_position = [row, col]
        elif matrix[row][col] == 'E':
            enemy_positions.append([row, col])

# Logic
while True:
    # Read the direction
    direction = input()

    # Save the last position
    row_index, col_index = jet_position

    # Move the coordinates in the given direction
    current_row, current_col = move(jet_position, directions, direction)

    # Find the element on the current coordinates
    element = matrix[current_row][current_col]

    if element == "E":  # Enemy detected
        matrix[row_index][col_index] = '-'
        enemy_positions.remove([current_row, current_col])  # Destroy the enemy jet

        if enemy_positions:  # Check if they are any enemies left
            jet_armor -= 100  # decrease the armor
            if jet_armor <= 0:  # if the armor or our jet go below 1
                print(f"Mission failed, your jetfighter was shot down! "
                      f"Last coordinates [{current_row}, {current_col}]!")
                matrix[row_index][col_index] = '-'
                jet_position = [current_row, current_col]
                break

        else:  # if all enemies are dead
            matrix[row_index][col_index] = '-'
            jet_position = [current_row, current_col]

            print("Mission accomplished, you neutralized the aerial threat!")
            break

    elif element == "R":  # Repair points
        jet_armor = 300

    jet_position = [current_row, current_col]
    matrix[row_index][col_index] = '-'

# Show the position of the jet on the map
matrix[current_row][current_col] = 'J'

# Print the matrix row by row
[print(''.join(row)) for row in matrix]

