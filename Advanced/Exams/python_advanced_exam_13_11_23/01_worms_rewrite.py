from collections import deque


# Read User input
worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

# Initialise variables for the output
number_of_worms = len(worms)
worms_with_holes = 0

# Logic
while worms and holes:
    last_worm = worms.pop()
    first_hole = holes.popleft()

    if last_worm == first_hole:
        worms_with_holes += 1
        continue

    else:
        last_worm -= 3
        if last_worm > 0:
            worms.append(last_worm)

if worms_with_holes:
    print(f"Matches: {worms_with_holes}")
else:
    print("There are no matches.")

if not worms and worms_with_holes == number_of_worms:
    print("Every worm found a suitable hole!")
elif not worms and worms_with_holes < number_of_worms:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join([str(x) for x in holes])}")
