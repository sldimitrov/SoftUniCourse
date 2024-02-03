~from collections import deque

# Read User input
bullet_price = int(input())
barrel_size = int(input())

bullets = deque([int(i) for i in input().split()])
locks = deque([int(x) for x in input().split()])

price_of_intelligence = int(input())

# Logic
counter_of_bullets = 0
counter = 0
is_opened = False
while bullets:
    current_lock = locks.popleft()

    bullet = bullets.pop()
    if bullet <= current_lock:
        print("Bang!")

    else:
        print("Ping!")
        locks.appendleft(current_lock)

    counter += 1
    counter_of_bullets += 1
    if counter == barrel_size and bullets:
        print(f"Reloading!")
        counter = 0
    if not locks:
        is_opened = True
        break


# Calculations
bullets_left = len(bullets)
bullets_cost = counter_of_bullets * bullet_price
earned = price_of_intelligence - bullets_cost

# Print User output
if is_opened:
    print(f"{bullets_left} bullets left. Earned ${earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")


