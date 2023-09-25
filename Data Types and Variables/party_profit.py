from math import floor
# Read User input
group = int(input())
days = int(input())
coins = 0

# Logic
for day in range(1, days + 1):
    if day == 10:
        group -= 2
    if day == 15:
        group += 5
    coins = coins + 50 - (group * 2)
    if day == 3:
        coins = coins - (group * 3)
    if day == 5:
        coins = coins + (20 * group) - (group * 2)

each_companion = coins / group
print(f"{group} companions received {each_companion} coins each.")

# Print User output