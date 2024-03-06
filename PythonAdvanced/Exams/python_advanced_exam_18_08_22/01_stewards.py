from collections import deque

# Read User input
passenger_seats = input().split(', ')
first_sequence = deque([int(x) for x in input().split(', ')])
second_sequence = deque([int(x) for x in input().split(', ')])

# Initialise variables
seat_that_has_been_matched = []
seat_matches = 0  # if 3 == End
rotations = 0  # if 10 == End

# Logic
while first_sequence and second_sequence:
    equality = False
    if seat_matches == 3:
        break
    elif rotations == 10:
        break

    number_1 = first_sequence.popleft()
    number_2 = second_sequence.pop()

    combination = number_1 + number_2

    first_match = f"{number_1}{chr(combination)}"
    if first_match in passenger_seats:
        passenger_seats.remove(first_match)
        seat_that_has_been_matched.append(first_match)
        seat_matches += 1
        rotations += 1
        continue
    second_match = f"{number_2}{chr(combination)}"
    if second_match in passenger_seats:
        passenger_seats.remove(second_match)
        seat_that_has_been_matched.append(second_match)
        seat_matches += 1
        rotations += 1
        continue

    rotations += 1
    first_sequence.append(number_1)
    second_sequence.appendleft(number_2)

# Print User output
print(f"Seat matches: {', '.join(seat_that_has_been_matched)}")
print(f"Rotations count: {rotations}")
