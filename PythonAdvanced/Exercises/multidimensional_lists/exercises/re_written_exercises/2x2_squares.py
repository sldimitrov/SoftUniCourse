DIRECTIONS = {
    "right": [0, 1],
    "down": [1, 0],
    "diagonal": [1, 1],
}


# Read matrix parameters
rows, cols = (int(x) for x in input().split())

# Read the matrix
matrix = [input().split() for i in range(rows)]

# Initialise a counter for the output
number_of_squares = 0

# Logic
for current_row in range(0, rows - 1):
    for current_col in range(0, cols - 1):
        is_not_equal = False

        # Save the current element into a variable
        current_element = matrix[current_row][current_col]
        # Initialise a counter for the number of matches within the current square
        match_counter = 0
        # Travel in every direction until a different element is found then continue
        for direction, coordinates in DIRECTIONS.items():
            # unpack direction coordinates
            pos_0, pos_1 = coordinates

            # initialise next coordinates
            row, col = (
                current_row + pos_0,
                current_col + pos_1,
            )

            next_element = matrix[row][col]

            if next_element != current_element:  # if the element does not match the current one
                is_not_equal = True
                break  # continue searching with the next square

            match_counter += 1  # else: increase the number of matches

            if match_counter >= 3:  # if there are more than 3 matches
                number_of_squares += 1  # we increase the number of valid squares

        if is_not_equal:  # if there is no equal element continue with the next square
            continue

# Print User output
print(number_of_squares)
