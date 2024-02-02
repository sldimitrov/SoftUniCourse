# Define functions to solve the problem with single responsibility
def check_indices_valid(indices):
    """
    We use this function to check if the indices
    given by the user are valid or if they within
    the range of the matrix

    params: list of indices
    returns: boolean
    """
    return {indices[0], indices[3]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


def swap_elements(command, indices):
    """
        This function calls the <check_indices_valid>
        It also validates the len of the indices and the given command.
        Then it unpacks the list of the given 2 coordinates and swaps
        their positions within the matrix.
        Print out the matrix if the operation is successful.
        Otherwise, it prints out an error message

        params: str (command)
        returns: list of indices
        """
    if len(indices) == 4 and check_indices_valid(indices) and command == "swap":
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print('Invalid input!')


# Read parameters and coordinates from the User
rows, cols = [int(i) for i in input().split()]
matrix = [input().split() for row in range(rows)]  # Matrix

# Initialise a range
valid_rows = range(rows)
valid_cols = range(cols)

# Logic
while True:
    # Read a command and a list with coordinates
    command_type, *coords = [int(x) if x.isdigit() else x for x in input().split()]

    # break condition
    if command_type == 'END':
        break

    # call a function with given arguments
    swap_elements(command_type, coords)
