from collections import deque

# Read User input
worms = [int(x) for x in input().split()]
apples = deque(int(x) for x in input().split())

# Save the number of worms into a variable
total_worms = len(worms)
# Initialise another for these who find a whole for themselves
worms_with_holes = 0

# Iterate while we have both worms and apples
while worms and apples:
    # Take an element from a collection
    curr_worm = worms.pop()
    curr_apple = apples.popleft()

    # check if the worm lower or equal to 0
    if curr_worm <= 0:
        apples.appendleft(curr_apple)  # append the apple to its collection
        continue

    # check if we have a match between the apple and the worm
    if curr_worm == curr_apple:
        worms_with_holes += 1  # increase the worm_with_holes count
        continue
    else:  # if we don't have a match append to the list the word decreased by 3
        worms.append(curr_worm - 3)

# Print User output
if worms_with_holes:
    print(f"Matches: {worms_with_holes}")
else:  # if there are no worms with holes
    print("There are no matches.")

if not worms:  # if there are no worms in the list
    if total_worms == worms_with_holes:  # if total worm count is equal to the count of worms with holes
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:  # if there are any worms left
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if apples:  # if there are any apples
    print(f"Holes left: {', '.join(str(x) for x in apples)}")
else:  # if there are not
    print("Holes left: none")
