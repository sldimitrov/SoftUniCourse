# Read User input
count_of_presents = int(input())
size = int(input())

# Initialise variables
matrix = []  # neighborhood
santa_pos = []
last_position = []
nice_kids_total = 0
nice_kids_given = 0
total_presents_given = 0

# Initialise the matrix
for row in range(size):
    matrix.append(input().split())
    # Find Santa's position in the neighborhood
    if 'S' in matrix[row]:
        santa_pos = [row, matrix[row].index('S')]
        matrix[row][santa_pos[1]] = '-'

    nice_kids_total += matrix[row].count('V')

# Initialise directions
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

# Logic
command = input()

while command != "Christmas morning":
    # delete last position
    if last_position:
        matrix[last_position[0]][last_position[1]] = '-'

    # direction
    r, c = directions[command]

    # new coordinates
    pos_1 = santa_pos[0] + r
    pos_2 = santa_pos[1] + c

    santa_pos = [
        pos_1,
        pos_2
    ]

    # Good kid lives here
    if matrix[pos_1][pos_2] == 'V':
        count_of_presents -= 1
        total_presents_given += 1
        nice_kids_given += 1

        # break condition
        if total_presents_given >= count_of_presents:
            break

    # Naughty kid lives here
    elif matrix[pos_1][pos_2] == 'X':
        pass

    # Everyone receive present! Cookie was found
    elif matrix[pos_1][pos_2] == 'C':
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        for direction, coords in directions.items():
            # Return deer to Santa Claus after delivery
            deer_pos_1 = pos_1
            deer_pos_2 = pos_2

            # new coordinates
            deer_pos_1 += coords[0]
            deer_pos_2 += coords[1]

            if matrix[deer_pos_1][deer_pos_2] == 'V':
                nice_kids_given += 1
                total_presents_given += 1
                count_of_presents -= 1

                if not count_of_presents:  # if Santa runs out of presents
                    break

            elif matrix[deer_pos_1][deer_pos_2] == 'X':
                total_presents_given += 1

            matrix[deer_pos_1][deer_pos_2] = '-'

    matrix[santa_pos[0]][santa_pos[1]] = '-'

    if total_presents_given >= count_of_presents:
        break
    command = input()

matrix[santa_pos[0]][santa_pos[1]] = 'S'
# Print User output
if total_presents_given >= count_of_presents and nice_kids_total:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]

if nice_kids_given >= nice_kids_total:
    print(f"Good job, Santa! {nice_kids_given} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_total - nice_kids_given} nice kid/s.")
