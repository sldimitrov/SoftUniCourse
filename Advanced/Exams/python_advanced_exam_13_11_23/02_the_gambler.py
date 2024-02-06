def valid_coordinates(x: int, y: int) -> bool:
    """
    This functions takes: two int params.
    They are coordinates, and we check if they are in the valid range of our matrix and return: True if so,
    otherwise return: False.
    """
    if 0 <= x < size and 0 <= y < size:
        return True
    return False


# Read the size of the matrix
size = int(input())

# Initialise variables for the matrix and for player position
matrix = []
player_pos = []

# Initialise variable for the player's initial entering - 100$
money = 100

# Initialise a for loop to read the matrix
for row in range(size):
    line = list(input())  # each line is a list of elements

    matrix.append(line)  # append each line to the matrix

    if 'G' in matrix[row]:  # check if 'G' is in the current row of the matrix
        # Save the coordinates of the position of the player
        player_pos = [row, matrix[row].index('G')]
        # Change its symbol with dash in the matrix
        matrix[player_pos[0]][player_pos[1]] = '-'

# Initialise the directions within a dictionary
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

# Initialise a boolean to determine if the player had lost or won at the end
is_lost = False

# Read command until 'end'
command = input()
while command != "end":
    # Taking the coordinates of the future position
    pos_0 = player_pos[0] + directions[command][0]
    pos_1 = player_pos[1] + directions[command][1]

    # Check if the coordinates are in the valid range
    if valid_coordinates(pos_0, pos_1):
        # Save the future position symbol in a variable
        position = matrix[pos_0][pos_1]

        # Check which one of these is our symbol
        if position == 'W':  # Win
            money += 100
        elif position == 'P':  # Penalty
            money -= 200
        elif position == 'J':  # JACKPOT
            print("You win the Jackpot!")
            money += 100000
            break  # we break after winning the jackpot
        if money <= 0:
            is_lost = True
            break  # we also break if the player run out of money

    else:  # invalid coords
        is_lost = True
        break  # last but not least, we break if the curr coordinates are invalid

    # We change the last player position with dash
    matrix[player_pos[0]][player_pos[1]] = '-'
    # Move the player to the current position
    player_pos = [pos_0, pos_1]

    # Read command
    command = input()

# Move the player to the last position after the break
matrix[pos_0][pos_1] = 'G'

if is_lost:  # the player has lost
    print("Game over! You lost everything!")
else:  # he has won
    print(f"End of the game. Total amount: {money}$")
    [print(''.join(row)) for row in matrix]