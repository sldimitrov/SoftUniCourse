
def valid_coordinates(x_pos, y_pos) -> bool:
    if 0 <= x_pos < size and 0 <= y_pos < size:
        return True
    return False


# Read size of the matrix
size = int(input())

# Initialise the matrix and variable to store player position
game_board = []
player_pos = []
money = 100

# Initialise directions
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

# Read the matrix
for row in range(size):
    game_board.append(list(input()))

    if 'G' in game_board[row]:  # Find player pos
        player_pos = [row, game_board[row].index('G')]
        game_board[row][player_pos[1]] = '-'

# ['W', '-', '-', 'W'] ['W', '-', '-', 'W'] ['-', '-', 'P', '-'] ['-', '-', '-', '-']
# [0, 2]

is_lost = False
# Logic
command = input()
while command != 'end':
    pos_0 = player_pos[0] + directions[command][0]
    pos_1 = player_pos[1] + directions[command][1]
    if valid_coordinates(pos_0, pos_1):
        if game_board[pos_0][pos_1] == 'W':
            money += 100
        elif game_board[pos_0][pos_1] == 'P':
            money -= 200
        elif game_board[pos_0][pos_1] == 'J':
            print("You win the Jackpot!")
            money += 100000
            break

        if money <= 0:
            is_lost = True
            break

    else:  # if player not in game_board range
        is_lost = True

    game_board[player_pos[0]][player_pos[1]] = '-'
    player_pos = [pos_0, pos_1]

    command = input()

game_board[pos_0][pos_1] = 'G'

# Print User output
if is_lost:
    print("Game over! You lost everything!")
else:
    print(f"End of the game. Total amount: {money}$")
    [print(''.join(row)) for row in game_board]
