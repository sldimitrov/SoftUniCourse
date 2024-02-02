fires = input().split('#')
water = int(input())

effort = 0
total_fire = 0
put_out_cells = []

print('Cells:')
# Logic
for fire in fires:
    args = fire.split(' = ')
    fire_type = args[0]
    level = int(args[1])
    valid = False

    if water < level:
        continue

    if fire_type == 'High' and 81 <= level <= 125:
        valid = True
    elif fire_type == 'Medium' and 51 <= level <= 80:
        valid = True
    elif fire_type == 'Low' and 1 <= level <= 50:
        valid = True

    if valid:
        put_out_cells.append(level)
        water -= level
        total_fire += level
        effort += level * 0.25

for each in put_out_cells:
    print(f' - {each}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')

