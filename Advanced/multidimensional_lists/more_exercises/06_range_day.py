# Define a function
def valid_coordinates(coord_1: int, coord_2: int):
    """
    This functions validates coordinates within a matrix
    """
    if 0 <= coord_1 < 5 and 0 <= coord_2 < 5:
        return True
    return False


# Initialise variables
matrix = []
player_pos = []
targets_left = 0
targets_hit = 0
targets_hit_pos = []

# Initialise the matrix
for row in range(5):
    matrix.append(input().split())  # NUMBERS are STR!
    # find the player pos
    if 'A' in matrix[row]:
        player_pos = [row, matrix[row].index('A')]
    # find the number of targets
    if 'x' in matrix[row]:
        targets_left += matrix[row].count('x')

# Initialise the directions
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

# Read commands n times
for i in range(int(input())):
    command = input().split()

    if command[0] == 'move':
        direction, steps = command[1], command[2]
        pos_1, pos_2 = player_pos  # player coordinates
        r, c = directions[direction]  # direction

        # taking the coords of the new position
        for step in range(int(steps)):
            pos_1 += r
            pos_2 += c

        if valid_coordinates(pos_1, pos_2) and matrix[pos_1][pos_2] == '.':
            player_pos = [pos_1, pos_2]  # if valid coordinates change player's position

    elif command[0] == 'shoot':
        direction = command[1]
        pos_1, pos_2 = player_pos  # player coordinates
        r, c = directions[direction]  # direction coordinates
        while True:  # while valid range
            pos_1 += r
            pos_2 += c
            if valid_coordinates(pos_1, pos_2):
                if matrix[pos_1][pos_2] == '.':  # if steps on '*' - continue
                    continue
                elif matrix[pos_1][pos_2] == 'x':  # if step on 'x' - shoot it
                    targets_left -= 1
                    targets_hit += 1
                    targets_hit_pos.append([pos_1, pos_2])  # take its coordinates
                    matrix[pos_1][pos_2] = '.'  # change its value
                    break  # after shooting a target
            else:
                break  # if invalid coords

        if not targets_left:
            print(f"Training completed! All {targets_hit} targets hit.")
            break  # if there are no targets left

# Print User output
if targets_left:
    print(f"Training not completed! {targets_left} targets left.")

print(*targets_hit_pos, sep='\n')

