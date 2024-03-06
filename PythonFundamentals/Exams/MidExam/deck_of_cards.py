# Define the functions
def add_card_function(card_name: str, cards_list):
    if card_name not in cards_list:
        cards_list.append(card_name)
        print("Card successfully added")
        return cards_list
    else:
        print("Card is already in the deck")
        return True


def remove_card_function(card_name: str, cards_list):
    if card_name in cards_list:
        cards_list.remove(card_name)
        print("Card successfully removed")
        return cards_list
    else:
        print("Card not found")
        return True


def remove_at_index_function(index: int, cards_list):
    if 0 <= index < len(cards_list):
        cards_list.remove(cards_list[index])
        print("Card successfully removed")
        return cards_list
    else:
        print("Index out of range")


def insert_card_function(index: int, card_name: str, cards_list):
    if 0 <= index < len(cards_list):
        if card_name not in cards_list:
            cards_list.insert(index, card_name)
            print("Card successfully added")
        else:
            print("Card is already added")
    else:
        print("Index out of range")
    return cards_list


# Read User input
card_input_list = input().split(", ")
n_lines = int(input())
for i in range(n_lines):
    command = input()
    if 'Add' in command:
        name_of_the_card = (command.split(', ')[1])
        add_card_function(name_of_the_card, card_input_list)

    elif 'Remove At' in command:
        command_index = int(command.split(', ')[1])
        remove_at_index_function(command_index, card_input_list)

    elif 'Remove' in command:
        card_to_remove = (command.split(', ')[1])
        remove_card_function(card_to_remove, card_input_list)

    elif 'Insert' in command:
        command_index = int(command.split(', ')[1])
        chosen_card = (command.split(', ')[2])
        insert_card_function(command_index, chosen_card, card_input_list)


for i in card_input_list:
    if i != card_input_list[-1]:
        print(i, end=', ')
    else:
        print(i)
