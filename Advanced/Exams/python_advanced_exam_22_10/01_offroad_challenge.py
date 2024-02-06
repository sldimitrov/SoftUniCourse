from collections import deque

fuel_packs = [int(x) for x in input().split()]
consumption_idx = deque([int(x) for x in input().split()])
peaks = deque([int(x) for x in input().split()])

counter_of_peaks = 1
list_of_peaks = []
is_won = False

while True:
    if not peaks:
        is_won = True
        break

    curr_fuel = fuel_packs.pop()
    curr_consumption = consumption_idx.popleft()
    curr_peak = peaks.popleft()

    fuel_left = curr_fuel - curr_consumption
    if fuel_left >= curr_peak:
        print(f"John has reached: Altitude {counter_of_peaks}")
        list_of_peaks.append(f'Altitude {counter_of_peaks}')
        counter_of_peaks += 1
    else:
        print(f"John did not reach: Altitude {counter_of_peaks}")
        break

if not is_won :
    print("John failed to reach the top.")
    if list_of_peaks:
        print(f"Reached altitudes: {', '.join(list_of_peaks)}")
    else:
        print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")
