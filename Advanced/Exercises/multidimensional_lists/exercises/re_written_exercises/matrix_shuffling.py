
# Read User data
rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for row in range(rows)]

VALID_ROWS = range(rows)
VALID_COLS = range(cols)


# Define functions
def valid_coords(positions):

    return {positions[0], positions[2]}.issubset(VALID_ROWS) and {positions[2], positions[3]}.issubset(VALID_COLS)


def swap_elements(command, indices):
    if command == 'swap' and indices and len(indices) == 4 and valid_coords(indices):
        r_1, c_1, r_2, c_2 = indices
        matrix[r_1][c_1], matrix[r_2][c_2] = matrix[r_2][c_2], matrix[r_1][c_1]
        [print(*row) for row in matrix]
        return True
    print("Invalid input!")
    return False


# Logic
while True:
    command_type, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command_type == 'END':
        break

    swap_elements(command_type, coordinates)