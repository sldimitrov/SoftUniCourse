# Read User input
size = int(input())

matrix = []
alis_pos = []
total_tea_collected = 0

# Initialise directions
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1],
}

# Initialise the matrix and find player positions
for row in range(size):
    matrix.append([int(x) if x.isdigit() else x for x in input().split()])
    if "A" in matrix[row]:
        alis_pos = [row, matrix[row].index('A')]
        matrix[alis_pos[0]][alis_pos[1]] = '*'

while True:
    command = input()
    # direction
    r, c = directions[command]
    # new coordinates
    pos_1, pos_2 = [alis_pos[0] + r, alis_pos[1] + c]
    # validation of the coordinates
    if 0 <= pos_1 < size and 0 <= pos_2 < size:
        if matrix[pos_1][pos_2] == "R":
            matrix[pos_1][pos_2] = '*'
            print("Alice didn't make it to the tea party.")
            break
        elif matrix[pos_1][pos_2] == "." or matrix[pos_1][pos_2] == '*':
            pass
        else:
            total_tea_collected += matrix[pos_1][pos_2]

        alis_pos[0] = pos_1
        alis_pos[1] = pos_2
        matrix[pos_1][pos_2] = '*'

    else:
        print("Alice didn't make it to the tea party.")
        break

    if total_tea_collected >= 10:
        print("She did it! She went to the party.")
        break

[print(*row) for row in matrix]

