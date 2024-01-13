from collections import deque

# Read User Input
cups = deque([int(x) for x in input().split()])
bottles = deque([int(y) for y in input().split()])

waster_litters_of_water = 0

# Logic
while cups:
    current_liquid = bottles.pop()
    current_cup = cups.popleft()

    if current_liquid >= current_cup:  # if fills
        current_cup -= current_liquid
        if current_cup < 0:
            waster_litters_of_water += abs(current_cup)

    elif current_liquid < current_cup:  # if it's not enough
        current_cup -= current_liquid
        cups.appendleft(current_cup)

    if not bottles:  # if there are no more water
        print("Cups:", *cups)  # User output
        break

else:  # the loop breaks
    print("Bottles:", *reversed(bottles))  # User output

print(f"Wasted litters of water: {waster_litters_of_water}")  # User output
