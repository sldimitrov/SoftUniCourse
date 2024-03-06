# Read User input
players_names = [x for x in input().split(', ')]

dictionary_turns = {players_names[0]: False, players_names[1]: False}

# Initialise variables
matrix = []
row_counter = 0
is_shocked = False

for row in range(6):
    matrix.append(input().split())


def players_turn(counter):
    result = [1 if counter % 2 != 0 else 0]
    return result[0]


while True:
    # Get player future coordinates
    player_coordinates = input()

    # Unpack current coordinates
    row, column = map(int, player_coordinates.strip('(').strip(')').split(', '))

    # Get the name of the current player
    index = players_turn(row_counter)
    current_player = players_names[index]

    if not dictionary_turns[current_player]:

        # Find the element of the given coordinates
        element = matrix[row][column]

        if element == "E":  # exit found
            print(f"{current_player} found the Exit and wins the game!")
            break

        elif element == "T":  # player trapped
            if current_player == 'Jerry':
                print(f"{current_player} is out of the game! The winner is Tom.")
            if current_player == 'Tom':
                print(f"{current_player} is out of the game! The winner is Jerry.")
            break

        elif element == "W":  # player break into a wall
            print(f"{current_player} hits a wall and needs to rest.")
            dictionary_turns[current_player] = True
            row_counter += 1
            continue

    dictionary_turns[current_player] = False
    row_counter += 1
