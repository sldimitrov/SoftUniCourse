from collections import deque

# Read User input
bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

# Initiali
total_honey = 0

functions = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}

while bees and nectar:
    curr_bee = bees.popleft()
    curr_nectar = nectar.pop()

    if curr_nectar < curr_bee:
        bees.appendleft(curr_bee)
    else:
        total_honey += abs(functions[symbols.popleft()](curr_bee, curr_nectar))

# Print User output
print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
