def valid_coordinates(x, y):
    if 0 <= x < size and 0 <= y < size:
        return True
    return False


size = int(input())
matrix = []
player_pos = []
money = 100

for row in range(size):
    line = list(input())

    matrix.append(line)

    if 'G' in matrix[row]:
        player_pos = [row, matrix[row].index('G')]
        matrix[player_pos[0]][player_pos[1]] = '-'

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

is_lost = False

command = input()
while command != "end":
    pos_0 = player_pos[0] + directions[command][0]
    pos_1 = player_pos[1] + directions[command][1]

    if valid_coordinates(pos_0, pos_1):
        position = matrix[pos_0][pos_1]

        if position == 'W':
            money += 100
        elif position == 'P':
            money -= 200
        elif position == 'J':
            print("You win the Jackpot!")
            money += 100000
            break
        if money <= 0:
            is_lost = True
            break

    else:  # invalid coords
        is_lost = True
        break

    matrix[player_pos[0]][player_pos[1]] = '-'
    player_pos = [pos_0, pos_1]

    command = input()

matrix[pos_0][pos_1] = 'G'

if is_lost:
    print("Game over! You lost everything!")
else:
    print(f"End of the game. Total amount: {money}$")
    [print(''.join(row)) for row in matrix]