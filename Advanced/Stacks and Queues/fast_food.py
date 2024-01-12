from collections import deque

# Read User input
total_food = int(input())
orders = deque([int(x) for x in input().split()])

# Logic
is_end = False
biggest_order = max(orders)
print(biggest_order)

for order in orders.copy():
    if order <= total_food:
        total_food -= order
        orders.popleft()
    else:
        is_end = True
        break

# Print User output
if not is_end:
    print('Orders complete')
else:
    print('Orders left:', *orders)