from collections import deque

# Read User input
chocolate = [int(x) for x in input().split(', ') if int(x) > 0]
cups_of_milk = deque(int(x) for x in input().split(', ') if int(x) > 0)

# Initialise a counter for the milkshakes
counter_of_milkshakes = 0

# While we have chocolate and milk and counter is lower than 5
while chocolate and cups_of_milk and counter_of_milkshakes < 5:
    liquid = chocolate[-1]
    cup = cups_of_milk.popleft()  # popleft the cup

    if liquid == cup:
        counter_of_milkshakes += 1
        chocolate.pop()  # remove the liquid from the list
    else:
        cups_of_milk.append(cup)  # append it in case the liquid is not enough
        chocolate[-1] -= 5  # decrease the chocolate value

if counter_of_milkshakes >= 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print(f"Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print(f"Milk: empty")
