class InvalidColumnChoice(Exception):
    pass


class FullColumnError(Exception):
    pass


ROWS = 6
COLS = 7


def get_first_available_row(col_index, matrix):
    for row_index in range(ROWS-1, -1, -1):
        if board[row_index][col_index] == 0:
            return row_index
    else:
        raise FullColumnError


def validate_column_choice(col):
    if 1 <= col <= COLS:
        return True
    raise InvalidColumnChoice


def show_the_matrix(matrix):
    for i in matrix:
        print(*i)


def read_the_matrix():
    play_table = [[0 for x in range(7)] for i in range(6)]
    return play_table


# Initialise the matrix -game table
board = read_the_matrix()

turns = 1

while True:
    player = [1 if turns % 2 != 0 else 2]

    try:
        column = input(f"Player {player} is on turn: ")
        validate_column_choice(column)
        column_index = int(column) - 1
        row = get_first_available_row(column_index, board)

        turns += 1
    except FullColumnError:
        print(f"This column is full, please select another one")
        continue
