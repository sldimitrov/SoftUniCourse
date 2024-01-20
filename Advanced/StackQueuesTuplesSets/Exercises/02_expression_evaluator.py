from collections import deque
from math import floor

expression = deque(input().split())

idx = 0

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

    if expression[1] in "*+-/":
        del expression[1]
        idx = 1
    idx += 1

print(floor(expression[0]))