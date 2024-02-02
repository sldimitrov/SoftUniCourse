# Read User input
list_with_numbers = input().split()
opposite_numbers = []
# Logic
for number in list_with_numbers:
    current_number = -int(number)
    opposite_numbers.append(current_number)
print(opposite_numbers)
# Print User input