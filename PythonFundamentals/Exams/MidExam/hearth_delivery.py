# Define a function for Cupid jump
def cupid_jumps(list_of_houses: list, cupid_index: int)-> list and int:
    if cupid_index not in range(len(list_of_houses)):
        cupid_index = 0
    if houses[cupid_index] == 0:
        print(f"Place {cupid_index} already had Valentine's day.")
    else:
        houses[cupid_index] -= 2
        if houses[cupid_index] == 0:
            print(f"Place {cupid_index} has Valentine's day.")
    return list_of_houses, cupid_index


# Read User input
houses = [int(house) for house in input().split('@')]
current_index = 0
command = input()
while command != "Love!":
    jump_length = int(command.split()[1])
    current_index += jump_length
    houses, current_index = cupid_jumps(houses, current_index)
    command = input()
print(f"Cupid's last position was {current_index}.")
if sum(houses) == 0:
    print("Mission was successful.")
else:
    houses = [int(house) for house in houses if int(house != 0)]
    print(f"Cupid has failed {len(houses)} places.")