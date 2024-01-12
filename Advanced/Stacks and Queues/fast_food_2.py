from collections import deque

# Read User input
food = int(input())
orders = deque([int(x) for x in input().split()])

# First output
print(max(orders))

# Initialise a while loop
while orders:
    order = orders.popleft()
    if food >= order:
        food -= order
    else:
        print(f"Orders left:", order, *orders)

else:
    print("Orders complete ")