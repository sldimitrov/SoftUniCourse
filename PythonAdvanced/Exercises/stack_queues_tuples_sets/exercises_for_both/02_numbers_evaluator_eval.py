from collections import deque
from math import floor

# Read User input
expression = deque(input().split())  # [6, 5, -, 4, 5, +]

# Initialize a counter for the index
idx = 0

# Logic
while idx < len(expression):
    element = expression[idx]

    if element in "/*+-":
        for _ in range(idx - 1):
            expression.appendleft(eval(f"{expression.popleft()} {element} {expression.popleft()}"))

        del expression[1]
        idx = 1

    idx += 1

# Print User output
print(floor(int(expression[0])))
