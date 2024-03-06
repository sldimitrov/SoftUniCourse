# Initialise a dictionary
data = {}
# Save the given info
n = int(input())
for _ in range(n):
    piece, composer, key = input().split('|')
    data[piece] = {'composer': composer, 'key': key}

# Initialise a while loop
while True:
    command = input()
    if command == 'Stop':
        break
    command = command.split('|')
    action = command[0]

    if action == 'Add':
        piece, composer, key = command[1], command[2], command[3]
        if piece not in data.keys():
            data[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == 'Remove':
        piece = command[1]
        if piece in data.keys():
            data.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == 'ChangeKey':
        piece, new_key = command[1], command[2]
        if piece in data.keys():
            for match, info in data.items():
                if match == piece:
                    info['key'] = new_key
                    print(f"Changed the key of {piece} to {new_key}!")
                    break
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

# Print User output
for piece, info in data.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")
