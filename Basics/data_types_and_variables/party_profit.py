from math import floor
# Read User input
group = int(input())
days = int(input())
coins = 0

# Logic
for day in range(1, days + 1):
    if day % 10 == 0:
        group -= 2
    if day % 15 == 0:
        group += 5
    if day % 3 == 0:
        coins -= (group * 3)
    if day % 5 == 0:
        coins += group * 20
        if day % 3 == 0:
            coins -= group * 2
    coins = coins + 50
    coins -= group * 2
each_companion = floor(coins / group)
print(f"{group} companions received {each_companion} coins each.")

# Print User output