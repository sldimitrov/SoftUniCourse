# Read User data
size = int(input())
commands = input().split()

# Initialize
matrix = []  # the matrix
player_coords = []  # player coordinates
total_coal, current_coal = 0, 0  # counters

moves = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}

# Matrix logic
for r in range(size):
    line = input().split()
    if 's' in line:  # find player's position
        player_coords = [r, line.index('s')]
        row, col = player_coords
    if 'c' in line:  # count down the coal
        total_coal += line.count('c')
    matrix.append(line)

# Move around the matrix
for command in commands:
