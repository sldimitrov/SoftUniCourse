# Read User input
quantity = int(input())
remaining_days = int(input())
# Logic
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
christmas_spirit = 0
money_spent = 0
for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        money_spent += quantity * ornament_set
        christmas_spirit += 5
    if current_day % 3 == 0:
        money_spent += quantity * (tree_skirt + tree_garland)
        christmas_spirit += 10 + 3
    if current_day % 5 == 0:
        money_spent += quantity * tree_lights
        christmas_spirit += 17
        if current_day % 3 == 0:
            christmas_spirit += 30
    if current_day % 10 == 0:
        christmas_spirit -= 20
        if remaining_days == 10:
            christmas_spirit -= 10
        money_spent += tree_skirt + tree_garland + tree_lights
if remaining_days % 10 == 0:
    christmas_spirit -= 30
print(f"Total cost: {money_spent}")
print(f"Total spirit: {christmas_spirit}")
# Print User output
