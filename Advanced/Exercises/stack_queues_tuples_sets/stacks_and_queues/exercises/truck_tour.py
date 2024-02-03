from collections import deque

# Read User Input with comprehension
gas_stations = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

# Initialise variables
gas_stations_copy = gas_stations.copy()
tank = 0
index = 0

# Logic
while gas_stations_copy:
    petrol, distance = gas_stations_copy.popleft()

    tank += petrol

    if tank >= distance:
        tank -= distance
    else:
        gas_stations.rotate(-1)
        gas_stations_copy = gas_stations.copy()
        index += 1
        tank = 0

# Print User output
print(index)