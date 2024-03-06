from collections import deque

# Read collections
milligrams_of_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])

# Initialise variables
caffeine_initial_value = 0

# Logic
while milligrams_of_caffeine and energy_drinks:
    # Pop values from the collections
    current_milligrams = milligrams_of_caffeine.pop()
    current_drink = energy_drinks.popleft()

    # Find the product of their multiplication
    total_caffeine = current_milligrams * current_drink

    if caffeine_initial_value + total_caffeine <= 300:
        caffeine_initial_value += total_caffeine
    else:
        energy_drinks.append(current_drink)
        caffeine_initial_value -= 30
        if caffeine_initial_value < 0:
            caffeine_initial_value = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(i) for i in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_initial_value} mg caffeine.")
