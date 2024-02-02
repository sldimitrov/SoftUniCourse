from collections import deque
from math import floor

# Read User input
expression = deque(input().split())

# Initialize an index counter
idx = 0

# Logic
while idx < len(expression):
    element = expression[idx]
    if element == "*":
        for i in range(idx - 1):
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif element == "+":
        for i in range(idx - 1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
    elif element == "-":
        for i in range(idx - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
    elif element == "/":
        for i in range(idx - 1):
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))

    # Check if next element is symbol and remove it from expression
    if expression[1] in "*+-/":
        del expression[1]
        idx = 1
    idx += 1

# Print User output
print(floor(expression[0]))