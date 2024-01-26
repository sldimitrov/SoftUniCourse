# Read User input
size = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for row in range(size)]
mag_eggs_pos = []
direction = None

max_eggs = float("-inf")


# Initialise directions
directions = {
    (0, 1): "right",  # right 0
    (0, -1): "left",  # left 1
    (-1, 0): "up",  # top 2
    (1, 0): "down",   # bottom 3
}


for row in range(size):
    for col in range(size):

        if matrix[row][col] == 'B':
            for d in directions:
                current_eggs = 0
                eggs_pos = []
                pos_1 = row
                pos_2 = col
                while True:
                    pos_1 += d[0]
                    pos_2 += d[1]

                    if 0 <= pos_1 < size and 0 <= pos_2 < size:
                        if matrix[pos_1][pos_2] != "X":
                            current_eggs += matrix[pos_1][pos_2]
                            eggs_pos.append([pos_1, pos_2])
                        else:  # if its trap
                            break
                    else:  # if invalid position
                        break
                if current_eggs >= max_eggs:
                    max_eggs = current_eggs
                    mag_eggs_pos = eggs_pos
                    direction = directions.get(d)

# Print User output
print(direction)
[print(row) for row in mag_eggs_pos]
print(max_eggs)

# 75/100 result
