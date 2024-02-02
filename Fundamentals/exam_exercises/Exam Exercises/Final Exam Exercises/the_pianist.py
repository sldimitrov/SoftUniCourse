def add_function(piece: str, composer: str, key: str, collection: list):
    is_added = False
    for dictionary in collection:
        if piece in dictionary.values():
            is_added = True
            break

    if not is_added:
        collection.append({'part': piece, 'artist': composer, 'key': key})
        print(f"{piece} by {composer} in {key} added to the collection!")
        return True
    print(f"{piece} is already in the collection!")
    return True


def remove_piece(piece: str, collection: list):
    for dictionary in collection:
        if piece in dictionary.values():
            collection.remove(dictionary)
            print(f"Successfully removed {piece}!")
            return True
    print(f"Invalid operation! {piece} does not exist in the collection.")
    return True


def change_key(artist: str, new_key: str, collection: list):

    for dictionary in collection:
        if artist in dictionary.values():
            dictionary['key'] = new_key
            print(f"Changed the key of {artist} to {new_key}!")
            return True
    print(f"Invalid operation! {artist} does not exist in the collection.")


def main_func():
    num = int(input())
    piano_pieces = []

    # Read User info
    for _ in range(num):
        part = input().split('|')
        part, artist, key = part[0], part[1], part[2]
        piano_pieces.append({'part': part, 'artist': artist, 'key': key})

    while True:
        command = input()
        if command == "Stop":
            break
        command = command.split("|")
        action = command[0]

        if action == "Add":
            part, artist, key = command[1], command[2], command[3]
            element = add_function(part, artist, key, piano_pieces)

        elif action == 'Remove':
            part = command[1]
            remove_piece(part, piano_pieces)

        elif action == 'ChangeKey':
            string, substring = command[1], command[2]
            change_key(string, substring, piano_pieces)

    for dictionary in piano_pieces:
        print(f"{dictionary['part']} -> Composer: {dictionary['artist']}, Key: {dictionary['key']}")


main_func()


