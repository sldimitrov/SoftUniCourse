# Read User input
deck_of_cars = input().split()
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    middle_part = len(deck_of_cars) // 2
    left_part_of_deck = deck_of_cars[0:middle_part]
    right_part_of_deck = deck_of_cars[middle_part:]
    shuffled_deck = []
    for current_index in range(len(left_part_of_deck)):
        shuffled_deck.append(left_part_of_deck[current_index])
        shuffled_deck.append(right_part_of_deck[current_index])
    deck_of_cars = shuffled_deck
print(shuffled_deck)
# Logic

# Print User output