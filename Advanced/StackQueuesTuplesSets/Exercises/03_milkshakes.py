from collections import deque

# Read User input
chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque(int(x) for x in input().split(', '))

milkshakes = 0

# Logic
while milkshakes != 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    cup_of_milk = cups_of_milk.pop()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.append(cup_of_milk)
    elif cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if cup_of_milk == chocolate:
        milkshakes += 1
    else:
        cups_of_milk.append(cup_of_milk)
        chocolates.append(chocolate - 5)

# Print User Output
if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")
