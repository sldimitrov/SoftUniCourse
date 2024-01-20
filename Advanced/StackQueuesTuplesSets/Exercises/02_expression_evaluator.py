from collections import deque
from math import floor

expression = deque(input().split())

idx = 0


while idx < len(expression):
    element = expression[idx]
    if element == "*":
        for _ in range(idx - 1):  # everything but the symbol
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))

    elif element == "/":
        for _ in range(idx - 1):  # everything but the symbol
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))

    elif element == "-":
        for _ in range(idx - 1):  # everything but the symbol
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))

    elif element == "+":
        for _ in range(idx - 1):  # everything but the symbol
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))

    if element in "*/+-":
        del expression[1]
        idx = 1
    idx += 1

print(floor(int(expression[0])))

