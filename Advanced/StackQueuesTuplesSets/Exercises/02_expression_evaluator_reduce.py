from functools import reduce
from math import floor

# Read User input
expression = input().split()

# Initialize a counter for the index
idx = 0

# Functions that will be called later on
functions = {
    "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
    "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
    "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
    "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
}

# Logic in main loop
while idx < len(expression):
    element = expression[idx]

    if element in "/+-*":
        expression[0] = functions[element](idx)
        [expression.pop(1) for _ in range(idx)]
        idx = 1
    idx += 1

# Print User output
print(floor(int(expression[0])))
