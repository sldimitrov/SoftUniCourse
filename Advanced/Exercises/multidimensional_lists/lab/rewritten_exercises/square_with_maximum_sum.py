# Initialise the directions
DIRECTIONS = {
    "right": [0, 1],
    "down": [1, 0],
    "primary_diagonal": [1, 1],
}


def check_square_sum(start_pos):
    """
    This function calculates the sum of the square of given coordinates.
    :param start_pos: list    :return:  and int
    """
    # Unpack the coordinates of the starting point
    current_row, current_col = start_pos
    # Initialise variables for the return
    square_sum = matrix[current_row][current_col]
    square_numbers = [matrix[current_row][current_col]]

    # Move into every direction and save the elements and their values
    for direction, direction_coordinates in DIRECTIONS.items():
        # The coordinates of the direction
        dir_row, dir_col = direction_coordinates

        # The next coordinates
        next_row, next_col = (
            current_row + dir_row,
            current_col + dir_col
        )

        # Save the values of the step in the given direction
        square_numbers .append(matrix[next_row][next_col])
        square_sum += matrix[next_row][next_col]

    return square_sum, square_numbers


# Read the matrix size
rows, cols = [int(x) for x in input().split(', ')]

# Initialise the matrix
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

# Initialise variables
biggest_square = []
biggest_sum_of_square = 0

# Logic - find the square with maximum sum
for r in range(0, rows-1):
    for c in range(0, cols-1):
        # Starting coordinates
        coordinates = [r, c]
        # Call the function which return the sum of the current square
        current_sum, current_square = check_square_sum(coordinates)

        # If the sum of the current square is greater than the biggest
        if current_sum > biggest_sum_of_square:  # it becomes the biggest square - we save its values
            biggest_sum_of_square = current_sum
            biggest_square = current_square


# Print User output
print(f"{biggest_square[0]} {biggest_square[1]}")
print(f"{biggest_square[2]} {biggest_square[3]}")
print(biggest_sum_of_square)
