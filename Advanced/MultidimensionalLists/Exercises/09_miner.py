# Read User input
n = int(input())
commands = input().split()

# Initialise directions
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1]
}

# Initialise
matrix = []  # the matrix
player_pos = []  # player position
total_coal, collected_coal = 0, 0  # counters

# Logic
for row in range(n):  # Matrix
    matrix.append(input().split())

    if "s" in matrix[row]:  # player pos
        r, c = row, matrix[row].index("s")
        player_pos = [r, c]
        matrix[r][c] = '*'

    if "c" in matrix[row]:  # coal count
        total_coal += matrix[row].count("c")

# Player moves
for m in commands:
    # Calculate new coordinates for the player
    r, c = player_pos[0] + directions[m][0], player_pos[1] + directions[m][1]

    # Validate these new coordinates
    if not (0 <= r < n and 0 <= c < n):
        continue  # if not valid

    # Change the position of the player
    player_pos = [r, c]

    if matrix[r][c] == "c":  # if mining
        collected_coal += 1
        if collected_coal == total_coal:  # if won
            print(f"You collected all coal! ({player_pos[0]}, {player_pos[1]})")
            break

    if matrix[r][c] == "e":  # if leaving
        print(f"Game over! ({player_pos[0]}, {player_pos[1]})")
        break

    matrix[r][c] = "*"

else:  # if lost
    print(f"{total_coal - collected_coal} pieces of coal left. ({player_pos[0]}, {player_pos[1]})")
