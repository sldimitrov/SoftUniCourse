# Define a function
def valid_coordinates(coord_1: int, coord_2: int):
    """
    Initialise a function to check whether the given coordinates
    are within the borders of the matrix or not.
    returns: boolean
    """
    if 0 <= coord_1 < size and 0 <= coord_2 < size:
        return True
    return False


# Read User input
count_of_presents = int(input())
size = int(input())

# Initialise variables
matrix = []  # neighborhood
santa_pos = []
nice_kids_left = 0
nice_kids_given = 0
last_position = []

# Initialise the matrix
for row in range(size):
    matrix.append(input().split())
    # Find Santa's position in the neighborhood
    if 'S' in matrix[row]:
        santa_pos = [row, matrix[row].index('S')]
        matrix[row][santa_pos[1]] = '-'
    if 'V' in matrix[row]:
        nice_kids_left += matrix[row].count('V')

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

    # Validate coordinates
    if valid_coordinates(pos_1, pos_2):

        # Good kid lives here
        if matrix[pos_1][pos_2] == 'V':
            count_of_presents -= 1
            nice_kids_left -= 1
            nice_kids_given += 1
            matrix[pos_1][pos_2] = 'S'
            santa_pos = [pos_1, pos_2]

            # break condition
            if not count_of_presents:  # if Santa runs out of presents
                break
            last_position = [pos_1, pos_2]
            # matrix[pos_1][pos_2] = '-'  # change value

        # Naughty kid lives here
        elif matrix[pos_1][pos_2] == 'X':
            santa_pos = [pos_1, pos_2]
            matrix[pos_1][pos_2] = 'S'
            last_position = [pos_1, pos_2]

            # matrix[pos_1][pos_2] = '-'

        # Everyone receive present! Cookie was found
        elif matrix[pos_1][pos_2] == 'C':
            for direction, coords in directions.items():
                # Return deer to Santa Claus after delivery
                deer_pos_1 = pos_1
                deer_pos_2 = pos_2

                # new coordinates
                deer_pos_1 += coords[0]
                deer_pos_2 += coords[1]

                # If coordinates are valid - deer deliver
                if valid_coordinates(deer_pos_1, deer_pos_2):

                    if matrix[deer_pos_1][deer_pos_2] == 'V':
                        count_of_presents -= 1
                        nice_kids_left -= 1
                        nice_kids_given += 1
                        if not count_of_presents:  # if Santa runs out of presents
                            break
                        last_position = [pos_1, pos_2]
                        # matrix[pos_1][pos_2] = '-'
                    elif matrix[deer_pos_1][deer_pos_2] == 'X':
                        last_position = [pos_1, pos_2]
                        # matrix[pos_1][pos_2] = '-'



    if not count_of_presents:
        break
    command = input()


# Print User output
[print(*row) for row in matrix]

if not count_of_presents:
    print("Santa ran out of presents!")
if nice_kids_left <= 0:
    print(f"Good job, Santa! {nice_kids_given} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")