from collections import deque

# Read User input
worms = [int(x) for x in input().split()]
apples = deque(int(x) for x in input().split())

# Initialise a counter
matches = 0
# Save the number of the worms
number_of_worms = len(worms)

# while we have something in collections
while worms and apples:

    # get current element
    curr_worm = worms.pop()
    curr_apple = apples.popleft()

    # check if worm is equal or lower than 0
    if curr_worm <= 0:
        apples.appendleft(curr_apple)  # append the apple to the deque
        continue

    # if elements are equal to each other
    if curr_worm == curr_apple:
        matches += 1  # increase the counter and remove elements by simply continuing
        continue

    # if they are not equal
    else:  # append the current worm decreased by 3 to the list
        worms.append(curr_worm - 3)

# Print User output
if matches:
    print(f"Matches: {matches}")
else:
    print(f"There are no matches.")

if not worms and matches == number_of_worms:
    print("Every worm found a suitable hole!")
else:
    if worms:
        print(f"Worms left: {', '.join([str(x) for x in worms])}")
    else:
        print("Worms left: none")

if not apples:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join([str(x) for x in apples])}")

