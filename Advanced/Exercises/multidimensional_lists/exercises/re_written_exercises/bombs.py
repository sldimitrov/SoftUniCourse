
# Read the size
size = int(input())

# Initialise directions
directions = {
    "up": [-1, 0],
    "up-right": [-1, 1],
    "right": [0, 1],
    "right-down": [1, 1],
    "down": [1, 0],
    "down-left": [1, -1],
    "left": [0, -1],
    "left-up": [-1, -1],
}


def valid_coordinates(size, *coordinates: list) -> bool:
    coord_1, coord_2 = coordinates
    return 0 <= coord_1 < size and 0 <= coord_2 < size


def bomb_explosion(board, *bomb_coordinates: list) -> bool:
    """
    In this function we will explode the bomb with the given coordinates and also will decrease the value
    of each cell that is nearby
    receive:   /   :return:
    """
    # Unpack coordinates
    bomb_row, bomb_col = bomb_coordinates
    # Search for the power of the bomb
    bomb_power = board[bomb_row][bomb_col]

    # If the bomb power is 0 or lower it cannot explode so return false immediately
    if bomb_power <= 0:
        return False

    for direction, nearby_cell in directions.items():
        # Unpack the direction to the nearby cell
        cell_row, cell_col = nearby_cell

        # Find the coordinates of the nearby cell
        cell_row, cell_col = bomb_row + cell_row, bomb_col + cell_col

        if valid_coordinates(size, cell_row, cell_col):

            # Find its value
            value = board[cell_row][cell_col]

            if value > 0:

                # Decrease the value of the given cell with the power of the bomb
                value -= bomb_power

                # Return the value to its original position
                matrix[cell_row][cell_col] = value

    matrix[bomb_row][bomb_col] = 0
    return True


# Initialise the matrix
matrix = [[int(x) for x in input().split()] for row in range(size)]
# Initialise a matrix with the coordinates of each bomb
bombs = [[int(x) for x in pair.split(',')] for pair in input().split()]

# Logic
for current_bomb in bombs:
    # Call the function that will make the explosion
    bomb_explosion(matrix, *current_bomb)

# Print User output
alive_cells = 0
sum_of_alive_cells = 0
for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            sum_of_alive_cells += el

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_alive_cells}")
[print(*row) for row in matrix]
