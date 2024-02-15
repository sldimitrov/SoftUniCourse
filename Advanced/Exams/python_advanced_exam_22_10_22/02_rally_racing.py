
# Read the size
size = int(input())
# Read the racer's number
racer_number = input()


def move(position: list, turns: dict, turn: str) -> int:
    # Unpack given coordinates
    r, c = position

    # Extract the coordinates of the given direction
    r_move, c_move = turns[turn][0], turns[turn][1]

    # Find the new position
    desired_row, desired_col = r + r_move, c + c_move

    return desired_row, desired_col


# Initialise variables
is_finished = False
matrix = []
kilometres = 0
car_position = [0, 0]
tunnels_position = []
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

# Initialise the matrix
for row in range(size):
    line = input().split()
    matrix.append(line)
    for col in range(size):
        if matrix[row][col] == 'T':
            tunnels_position.append(row)
            tunnels_position.append(col)

# Logic
while True:
    direction = input()

    if direction == "End":
        print(f"Racing car {racer_number} DNF.")
        break

    # Save the last position
    row_index, col_index = car_position

    # Move in the given direction
    current_row, current_col = move(car_position, directions, direction)

    # Find the element on the current coordinates
    element = matrix[current_row][current_col]

    if element == 'T':
        kilometres += 30  # add kilometers

        matrix[current_row][current_col] = '.'  # mask the previous position of the tunnel

        tunnels_position.remove(current_row)  # remove tunnel's coordinates
        tunnels_position.remove(current_col)

        current_row, current_col = tunnels_position  # move the car to the end of the tunnel

        matrix[current_row][current_col] = '.'  # mask the position of the tunnel

    elif element == '.':
        kilometres += 10  # add kilometers

    elif element == 'F':
        kilometres += 10  # add kilometers
        is_finished = True
        print(f"Racing car {racer_number} finished the stage!")
        break
    car_position = [current_row, current_col]

# Print User output
print(f"Distance covered {kilometres} km.")

# Show the car on the map
matrix[current_row][current_col] = "C"
[print(''.join(row)) for row in matrix]
