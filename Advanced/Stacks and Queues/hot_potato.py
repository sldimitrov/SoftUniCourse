from collections import deque

queue = deque(input().split())

# Read User Input
# Tracy Emily Daniel
# 2

moves = int(input())
queue.reverse()

# Logic
while len(queue) > 1:
    queue.rotate(moves)
    print(f"Removed {queue.popleft()}")
    queue.rotate(1)

# Print User output
print(f"Last is {''.join(queue)}")