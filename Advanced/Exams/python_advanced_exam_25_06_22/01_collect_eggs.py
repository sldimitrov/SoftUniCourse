from collections import deque

# Read collections
egg_sizes = deque([int(x) for x in input().split(', ')])
paper_pieces = deque([int(x) for x in input().split(', ')])

# Initialise a counter
fulfilled_boxes = 0

# Logic
while egg_sizes and paper_pieces:
    # Extract element from the collections
    first_egg = egg_sizes.popleft()
    last_paper = paper_pieces.pop()

    if first_egg <= 0:  # the egg is out-fresh
        paper_pieces.append(last_paper)
        continue

    elif first_egg == 13:  # an egg with bad luck occurs
        first_paper = paper_pieces.popleft()
        # reverse the first with the last element within the collection
        paper_pieces.append(first_paper)  # return the good luck back
        paper_pieces.appendleft(last_paper)
        continue

    if first_egg + last_paper <= 50:  # if the space required fits a box
        fulfilled_boxes += 1

# Print User output
if fulfilled_boxes:
    print(f"Great! You filled {fulfilled_boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if egg_sizes:
    print(f"Eggs left: {', '.join(map(str, egg_sizes))}")
if paper_pieces:
    print(f"Pieces of paper left: {', '.join(map(str, paper_pieces))}")
