from collections import deque

# Read User input
queue = deque(input().split())
n_toss = int(input())

# Logic
while len(queue) > 1:
    queue.rotate(-n_toss)
    print(f"Removed {queue.pop()}")

# Print User output
print(f"Last is {''.join(queue)}")
