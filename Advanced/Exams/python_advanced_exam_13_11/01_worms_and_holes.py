from collections import deque

worms = [int(x) for x in input().split()]
apples = deque(int(x) for x in input().split())

total_worms = len(worms)
worms_with_holes = 0

while worms and apples:
    curr_worm = worms.pop()
    curr_apple = apples.popleft()

    if curr_worm <= 0:
        apples.appendleft(curr_apple)
        continue

    if curr_worm == curr_apple:
        worms_with_holes += 1
        continue
    else:
        worms.append(curr_worm - 3)

if worms_with_holes:
    print(f"Matches: {worms_with_holes}")
else:
    print("There are no matches.")

if not worms:
    if total_worms == worms_with_holes:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if apples:
    print(f"Holes left: {', '.join(str(x) for x in apples)}")
else:
    print("Holes left: none")
