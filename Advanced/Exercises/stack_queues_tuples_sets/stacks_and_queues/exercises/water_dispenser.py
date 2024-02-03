from collections import deque

# Read User input
total_amount = int(input())

is_end = False
queue = deque()

# Logic
while True:
    command = input()
    if command == "Start":
        while True:
            action = input().split()
            if action[0] == "End":
                is_end = True
                break
            if action[0] == "refill":
                total_amount += int(action[1])
            else:
                if total_amount >= int(action[0]):
                    total_amount -= int(action[0])
                    print(f"{queue.popleft()} got water")
                else:
                    print(f"{queue.popleft()} must wait")
    if is_end:
        break
    queue.append(command)

# Print User output
print(f"{total_amount} liters left")