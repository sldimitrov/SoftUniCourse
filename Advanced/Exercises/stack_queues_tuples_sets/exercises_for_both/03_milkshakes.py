from collections import deque

# Read User input
chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque(int(x) for x in input().split(', '))

# Initialize a counter for the milkshakes
milkshakes = 0

# Logic
while milkshakes != 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    cup = cups_of_milk.popleft()

    if chocolate <= 0 and cup <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(cup)
        continue
    elif cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup:
        milkshakes += 1
    else:
        cups_of_milk.append(cup)
        chocolates.append(chocolate - 5)

# Print User output
if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join([str(x) for x in chocolates]) or 'empty'}")
print(f"Milk: {', '.join([str(x) for x in cups_of_milk]) or 'empty'}")

