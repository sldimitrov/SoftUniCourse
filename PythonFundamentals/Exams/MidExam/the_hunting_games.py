# Read User input
days_of_adventure = int(input())
count_of_players = int(input())
group_energy = float(input())
water_for_person = float(input())
food_for_person = float(input())
current_water = water_for_person * count_of_players * days_of_adventure
current_food = food_for_person * count_of_players * days_of_adventure
is_run_out_of_energy = False

# Logic
for day in range(1, days_of_adventure + 1):
    energy_loss = float(input())
    # Chopping wood
    group_energy -= energy_loss
    if group_energy <= 0:
        is_run_out_of_energy = True
        break

    # Drink water
    if day % 2 == 0:
        group_energy += group_energy * 0.05
        current_water -= current_water * 0.3

    # Group eat
    if day % 3 == 0:
        food_lose = current_food / count_of_players
        current_food -= food_lose
        group_energy += group_energy * 0.1


if is_run_out_of_energy:
    print(f'You will run out of energy. You will be left with {current_food:.2f} food and {current_water:.2f} water.')
else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
# Print User output
