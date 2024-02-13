
from collections import deque

# Read Input
time_spent = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]

duck_bath = {'Darth Vader Ducky': 0, 'Thor Ducky': 0, 'Big Blue Rubber Ducky': 0, 'Small Yellow Rubber Ducky': 0}

# Logic
while time_spent and tasks:
    time_needed = time_spent.popleft()
    task = tasks.pop()

    result = time_needed * task

    if result > 240:
        tasks.append(task - 2)
        time_spent.append(time_needed)
        continue

    if 0 <= result <= 60:
        duck_bath['Darth Vader Ducky'] += 1
    elif 61 <= result <= 120:
        duck_bath['Thor Ducky'] += 1
    elif 121 <= result <= 180:
        duck_bath['Big Blue Rubber Ducky'] += 1
    elif 181 <= result <= 240:
        duck_bath['Small Yellow Rubber Ducky'] += 1

# Print User output
print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, count in duck_bath.items():
    print(f"{duck}: {count}")