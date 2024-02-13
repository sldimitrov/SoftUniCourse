from collections import deque

fuel = [int(x) for x in input().split()]
consumption = deque([int(x) for x in input().split()])
peaks = deque([int(x) for x in input().split()])

elevation = 0
is_won = False

while True:
    if not peaks:
        is_won = True
        break
    current_fuel = fuel.pop()
    current_consumption = consumption.popleft()
    needed = peaks.popleft()

    if (current_fuel - current_consumption) >= needed:
        elevation += 1
        print(f"John has reached: Altitude {elevation}")

    else:
        print(f"John did not reach: Altitude {elevation + 1}")
        break

if not is_won:
    if elevation:
        print(f"John failed to reach the top. \n"
              f"Reached altitudes: {', '.join([f'Altitude {x}'for x in range(1, elevation+1)])}")
    else:
        print("John failed to reach the top. John didn't reach any altitude.")

else:
    print(f"John has reached all the altitudes and managed to reach the top!")
