from collections import deque

# Read User input
rows, cols = [int(x) for x in input().split()]

# Initialise collections
word = list(input())
word_copy = deque(word)

# Logic
for row in range(rows):
    while len(word_copy) < cols:
        word_copy.extend(word)

    # Print User output
    if row % 2 == 0:
        print(*[word_copy.popleft() for _ in range(cols)], sep='')
    else:
        print(*[word_copy.popleft() for _ in range(cols)][::-1], sep='')