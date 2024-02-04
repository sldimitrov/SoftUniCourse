# Read User input
following_lines = int(input())
capacity = 255
tank = 0
# Logic
for pour in range(following_lines):
    liters_of_water = int(input())
    if capacity < tank + liters_of_water:
        print('Insufficient capacity!')
    else:
        tank += liters_of_water
print(tank)
# Print User output