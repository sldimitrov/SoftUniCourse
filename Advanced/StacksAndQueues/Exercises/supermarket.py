from collections import deque

# Import a queue
queue = deque()

# Read User input
command = input()

# Logic
while command != "End":
    if command == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)
    command = input()

# Print User output
print(f"{len(queue)} people remaining.")