# Initialise directions
directions = {

}

# Read size of the matrix
size = int(input())

# Initialise the matrix and variable to store player position
game_board = []
player_pos = []

# Read the matrix
for row in range(size):
    game_board.append(list(input()))

    if 'G' in game_board[row]:  # Find player pos
        player_pos = [row, game_board[row].index('G')]
        game_board[row][player_pos[1]] = '-'

# ['W', '-', '-', 'W'] ['W', '-', '-', 'W'] ['-', '-', 'P', '-'] ['-', '-', '-', '-']
# [0, 2]

# Logic
command = input()
while command != 'end':


    command = input()

# Print User output
