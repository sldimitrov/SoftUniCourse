# Read User input
size = int(input())

matrix = []
best_path = []
bunny_pos = []

max_collected_eggs = float("-inf")
best_direction = None

# Initialise directions
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

# Initialise the matrix
for row in range(size):
    matrix.append(input().split())
    if "B" in matrix[row]:  # find the bunny position
        bunny_pos = [row, matrix[row].index('B')]

# loop through every direction
for direction, coordinates in directions.items():
    row, col = [
        bunny_pos[0] + coordinates[0],
        bunny_pos[1] + coordinates[1]
    ]

    current_path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size: # while valid coords
        if matrix[row][col] == "X":  # break condition
            break

        collected_eggs += int(matrix[row][col])
        current_path.append([row, col])

        # move the bunny
        row += coordinates[0]
        col += coordinates[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_path = current_path
        best_direction = direction

# Print User output
print(best_direction)
print(*best_path, sep='\n')
print(max_collected_eggs)
