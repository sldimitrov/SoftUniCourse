from collections import deque

# Read collections
daily_supplies = list(map(int, input().split(', ')))
daily_stamina = deque(list(map(int, input().split(', '))))

# Initialise variables
day = 1
peaks_conquered = []
peaks = deque([
    ('Vihren', 80),
    ('Kutelo', 90),
    ('Banski Suhodol', 100),
    ('Polezhan', 60),
    ('Kamenitza', 70),
])

# Logic
while True:
    if len(peaks_conquered) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    if day > 7 or not daily_stamina or not daily_supplies:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    # Extract elements from the collections
    supply = daily_supplies.pop()
    stamina = daily_stamina.popleft()

    # Calculate the energy for the day
    daily_energy = supply + stamina
    # Get the name and the energy needed for the current peak
    peak = peaks.popleft()

    if daily_energy >= peak[1]:
        peaks_conquered.append(peak[0])
        day += 1

    else:
        peaks.appendleft(peak)
        day += 1

if peaks_conquered:
    print("Conquered peaks:")
    print("\n".join(peaks_conquered))
